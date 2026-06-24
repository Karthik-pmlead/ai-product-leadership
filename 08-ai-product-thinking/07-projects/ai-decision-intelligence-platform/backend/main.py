from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from models.schemas import QueryRequest

from agents.orchestrator import run_decision_workflow

from websocket.websocket_manager import (
    clients,
    broadcast
)

app = FastAPI()

# -----------------------------------
# CORS
# -----------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# HEALTH CHECK
# -----------------------------------
@app.get("/")
def home():

    return {
        "message": "AI Decision Intelligence Platform Running"
    }

# -----------------------------------
# ASK AI ANALYST
# -----------------------------------
@app.post("/analyze")
async def analyze(request: QueryRequest):

    result = run_decision_workflow(
        request.query
    )

    # broadcast to frontend
    await broadcast(result)

    return result

# -----------------------------------
# WEBSOCKET
# -----------------------------------
@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):

    await websocket.accept()

    clients.append(websocket)

    try:

        while True:
            await websocket.receive_text()

    except:

        clients.remove(websocket)

