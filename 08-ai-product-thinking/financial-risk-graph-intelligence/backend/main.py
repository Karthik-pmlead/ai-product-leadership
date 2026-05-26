from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import RiskEvent

from graph_engine import get_graph_data
from risk_engine import propagate_risk, get_high_risk_nodes
from anomaly_engine import detect_anomalies
from news_engine import simulate_news_event

from websocket_manager import clients, broadcast

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

metrics = {
    "events_processed": 0,
    "high_risk_entities": 0,
    "anomalies_detected": 0,
}


# -----------------------------------
# GRAPH
# -----------------------------------
@app.get("/graph")
def graph_data():

    return {
        "graph": get_graph_data(),
        "metrics": metrics,
        "alerts": get_high_risk_nodes(),
        "anomalies": detect_anomalies(),
    }


# -----------------------------------
# RISK EVENT
# -----------------------------------
@app.post("/simulate-risk")
async def simulate_risk(event: RiskEvent):

    propagate_risk(
        event.entity_id,
        event.risk_delta
    )

    metrics["events_processed"] += 1

    alerts = get_high_risk_nodes()
    anomalies = detect_anomalies()

    metrics["high_risk_entities"] = len(alerts)
    metrics["anomalies_detected"] = len(anomalies)

    payload = {
        "graph": get_graph_data(),
        "alerts": alerts,
        "anomalies": anomalies,
        "metrics": metrics,
        "latest_event": event.dict(),
    }

    await broadcast(payload)

    return payload


# -----------------------------------
# NEWS EVENT
# -----------------------------------
@app.post("/simulate-news")
async def simulate_news():

    news = simulate_news_event()

    alerts = get_high_risk_nodes()
    anomalies = detect_anomalies()

    metrics["events_processed"] += 1
    metrics["high_risk_entities"] = len(alerts)
    metrics["anomalies_detected"] = len(anomalies)

    payload = {
        "graph": get_graph_data(),
        "alerts": alerts,
        "anomalies": anomalies,
        "metrics": metrics,
        "news": news,
    }

    await broadcast(payload)

    return payload


# -----------------------------------
# WEBSOCKET
# -----------------------------------
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            await websocket.receive_text()

    except:
        clients.remove(websocket)
