from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import asyncio

from simulator import generate_transaction
from scoring import calculate_risk
from scoring import explain_risk
from scoring import get_risk_level

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

transactions = []
alerts = []
active_connections = []


@app.get('/')
def root():
    return {
        'message': 'FinTech Risk Intelligence API Running'
    }


@app.get('/transactions')
def get_transactions():
    global transactions

    if len(transactions) < 15:
        for i in range(15):
            tx = generate_transaction(i + 1)

            tx['risk_score'] = calculate_risk(tx)

            transactions.append(tx)

    return transactions


@app.get('/alerts')
def get_alerts():
    global alerts
    global transactions

    alerts = []

    for tx in transactions:
        score = tx['risk_score']

        level = get_risk_level(score)

        if level in ['HIGH', 'MEDIUM']:
            alerts.append({
                'id': tx['id'],
                'transaction_id': tx['id'],
                'risk_score': score,
                'risk_level': level,
                'reasons': explain_risk(tx),
                'confidence': round(score / 100, 2),
                'recommended_action': 'Escalate for analyst review'
            })

    return alerts


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    active_connections.append(websocket)

    try:
        while True:
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        active_connections.remove(websocket)


async def broadcast_transaction(tx):
    disconnected = []

    for connection in active_connections:
        try:
            await connection.send_json(tx)

        except:
            disconnected.append(connection)

    for connection in disconnected:
        active_connections.remove(connection)


@app.post('/simulate')
async def simulate_transaction():
    tx_id = len(transactions) + 1

    tx = generate_transaction(tx_id)

    tx['risk_score'] = calculate_risk(tx)

    transactions.insert(0, tx)

    score = tx['risk_score']

    level = get_risk_level(score)

    if level in ['HIGH', 'MEDIUM']:
        alerts.insert(0, {
            'id': tx['id'],
            'transaction_id': tx['id'],
            'risk_score': score,
            'risk_level': level,
            'reasons': explain_risk(tx),
            'confidence': round(score / 100, 2),
            'recommended_action': 'Escalate for analyst review'
        })

    await broadcast_transaction(tx)

    return tx
