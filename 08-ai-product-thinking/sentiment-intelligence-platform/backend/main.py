from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

import asyncio

from simulator import generate_review
from sentiment import analyze_sentiment
from topics import detect_topic
from mlops import update_metrics
from mlops import get_metrics

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

reviews = []
active_connections = []


@app.get('/')
def root():
    return {
        'message': 'Sentiment Intelligence API Running'
    }


@app.get('/reviews')
def get_reviews():
    return reviews


@app.get('/metrics')
def metrics():
    return get_metrics()


@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    active_connections.append(websocket)

    try:
        while True:
            await asyncio.sleep(1)

    except WebSocketDisconnect:
        active_connections.remove(websocket)


async def broadcast_review(review):
    disconnected = []

    for connection in active_connections:
        try:
            await connection.send_json(review)

        except:
            disconnected.append(connection)

    for connection in disconnected:
        active_connections.remove(connection)


@app.post('/simulate')
async def simulate_review():
    review_id = len(reviews) + 1

    review = generate_review(review_id)

    sentiment_result = analyze_sentiment(
        review["text"]
    )

    review["sentiment"] = sentiment_result["sentiment"]

    review["confidence"] = sentiment_result["confidence"]

    review["topic"] = detect_topic(
        review["text"]
    )

    update_metrics(
        review["language"],
        review["confidence"]
    )

    reviews.insert(0, review)

    await broadcast_review(review)

    return review
