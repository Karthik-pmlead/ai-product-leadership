from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random
import hashlib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# DATA
# -----------------------------

products = [
    {"id": 1, "name": "Running Shoes", "category": "Sports"},
    {"id": 2, "name": "Gaming Headset", "category": "Electronics"},
    {"id": 3, "name": "Smart Watch", "category": "Electronics"},
    {"id": 4, "name": "Yoga Mat", "category": "Fitness"},
    {"id": 5, "name": "Coffee Maker", "category": "Home"},
    {"id": 6, "name": "Wireless Mouse", "category": "Electronics"},
    {"id": 7, "name": "Protein Powder", "category": "Fitness"},
]

user_profile = {
    "Sports": 1,
    "Electronics": 1,
    "Fitness": 1,
    "Home": 1,
}

session_store = {"current": []}

user_item_matrix = {
    "u1": {"Electronics": 5, "Sports": 2},
    "u2": {"Fitness": 4, "Home": 3},
    "u3": {"Electronics": 3, "Fitness": 2},
}

metrics = {
    "events_processed": 0,
    "recommendation_updates": 0,
    "ctr": 0.18,
    "conversion_rate": 0.07,
}

clients = []

# -----------------------------
# MODEL
# -----------------------------
class UserEvent(BaseModel):
    user_id: str = "u1"
    event_type: str
    category: str


# -----------------------------
# A/B TEST
# -----------------------------
def get_variant(user_id: str):
    h = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
    return "A" if h % 2 == 0 else "B"


# -----------------------------
# SESSION RANKING
# -----------------------------
def session_rank():
    category_boost = {}

    for e in session_store["current"]:
        cat = e["category"]

        wt = {
            "view": 1,
            "click": 2,
            "cart": 4,
            "purchase": 6,
        }.get(e["event_type"], 1)

        category_boost[cat] = category_boost.get(cat, 0) + wt

    ranked = []

    for p in products:
        score = category_boost.get(p["category"], 0)
        ranked.append({**p, "score": score})

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


# -----------------------------
# COLLAB FILTER
# -----------------------------
def collaborative_rank(user_id):
    prefs = user_item_matrix.get(user_id, {})

    ranked = []

    for p in products:
        score = prefs.get(p["category"], 1)
        ranked.append({**p, "score": score})

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


# -----------------------------
# EXPLAINABILITY ENGINE
# -----------------------------
def explain_product(product, user_id="u1"):
    reasons = []

    category = product["category"]

    # Long-term signal
    if user_profile.get(category, 0) > 2:
        reasons.append(f"Strong interest in {category}")

    # Session signal
    session_cats = [e["category"] for e in session_store["current"]]
    if category in session_cats:
        reasons.append(f"Recently interacted with {category}")

    # Collaborative signal
    similar_users = [
        u for u, prefs in user_item_matrix.items()
        if category in prefs
    ]
    if similar_users:
        reasons.append("Users with similar behavior engaged")

    if not reasons:
        reasons.append("Popular across users")

    return reasons


# -----------------------------
# HYBRID RANKING
# -----------------------------
def hybrid_rank():
    session_scores = session_rank()

    ranked = []

    for p in products:

        session_score = next(
            (x["score"] for x in session_scores if x["id"] == p["id"]),
            0,
        )

        score = (
            user_profile[p["category"]] * 0.5
            + session_score * 0.3
        )

        ranked.append({
            **p,
            "score": score,
            "reasons": explain_product(p)
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


# -----------------------------
# BASE RANKING
# -----------------------------
def rank_products():
    ranked = []

    for p in products:
        score = user_profile[p["category"]]

        ranked.append({
            **p,
            "score": score,
            "reasons": explain_product(p)
        })

    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


# -----------------------------
# API
# -----------------------------
@app.get("/recommendations")
def get_recommendations(user_id: str = "u1"):

    variant = get_variant(user_id)

    if variant == "A":
        ranked = rank_products()
    else:
        ranked = hybrid_rank()

    return {
        "variant": variant,
        "recommendations": ranked,
        "profile": user_profile,
        "metrics": metrics,
    }


@app.post("/event")
async def process_event(event: UserEvent):

    weight = {
        "view": 1,
        "click": 3,
        "cart": 5,
        "purchase": 8,
    }.get(event.event_type, 1)

    user_profile[event.category] += weight

    session_store["current"].append(event.dict())

    metrics["events_processed"] += 1
    metrics["recommendation_updates"] += 1

    metrics["ctr"] = round(
        min(metrics["ctr"] + random.uniform(0.001, 0.01), 1),
        2,
    )

    metrics["conversion_rate"] = round(
        min(metrics["conversion_rate"] + random.uniform(0.001, 0.005), 1),
        2,
    )

    payload = {
        "recommendations": hybrid_rank(),
        "profile": user_profile,
        "metrics": metrics,
        "latest_event": event.dict(),
    }

    await broadcast(payload)

    return payload


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()
    except:
        clients.remove(websocket)


async def broadcast(data):
    dead = []

    for c in clients:
        try:
            await c.send_json(data)
        except:
            dead.append(c)

    for d in dead:
        clients.remove(d)
