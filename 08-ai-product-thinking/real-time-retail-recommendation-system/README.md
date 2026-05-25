# 🚀 Real-Time Personalized Retail Recommendation System

A real-time, event-driven recommendation system that simulates how modern e-commerce platforms (like Amazon or Netflix) personalize user experiences using session behavior, collaborative filtering, and hybrid ranking models — with A/B testing and explainability.

---

# 📌 Overview

This project demonstrates a **production-style recommendation system MVP** that:

- Captures real-time user behavior (clicks, views, cart, purchase)
- Builds dynamic user profiles
- Uses session + long-term + collaborative signals
- Ranks products using a hybrid scoring engine
- Supports A/B testing for experimentation
- Provides explainable recommendations (“Why this item?”)
- Streams updates in real time using WebSockets

> This simulates core systems used in Amazon, Netflix, YouTube, and Meta.

---

# 🎬 Demo

## Live Flow

1. Click **Simulate Event**
2. User event is sent to backend
3. System updates user profile + session memory
4. Ranking engine recalculates recommendations
5. Explainability layer generates reasons
6. UI updates in real time via WebSocket

---

# 🧱 Architecture Diagram

```text
User Action (Frontend)
        ↓
FastAPI Event API
        ↓
Session + Profile Update Layer
        ↓
Hybrid Recommendation Engine
   ├── Long-term Profile Model
   ├── Session-based Model
   ├── Collaborative Filtering
        ↓
A/B Testing Router
        ↓
Explainability Engine
        ↓
WebSocket Streaming Layer
        ↓
React Frontend UI

```

# 🛠 Tech Stack
### Backend
- FastAPI
- Python
- WebSockets
- Pydantic
  
### Frontend
- React.js
- JavaScript
- Recharts (charts)

### System Design Concepts
- Event-driven architecture
- Real-time streaming
- Hybrid ranking systems
- A/B testing framework
- Explainable AI (XAI)

## 🌍 Real-World Use Cases

This system mirrors production systems used in:

- 🛒 Amazon (product recommendations)
- 🎬 Netflix (content personalization)
- ▶️ YouTube (video ranking)
- 🛍 Shopify / e-commerce platforms
- 📱 Meta feed ranking systems

## 📊 Metrics Layer

The system tracks:

- CTR (Click Through Rate)
- Conversion Rate
- Event Processing Count
- Recommendation Update Frequency
- Session activity intensity

## 🧠 Explainability Layer

Each recommendation includes:

- Long-term preference signals
- Session-based behavior signals
- Collaborative filtering signals

Example:
```
Why recommended:
- Strong interest in Electronics
- Recently interacted with Electronics
- Users with similar behavior engaged
```

# 🔄 System Workflow
```
1. User performs action (click/view/cart)
2. Event is sent to backend
3. User profile is updated
4. Session memory is updated
5. Recommendation engine recalculates scores
6. A/B testing selects ranking strategy
7. Explainability layer generates reasons
8. WebSocket pushes updates
9. UI updates instantly
```

# ✨ Features

### Core Features
- Real-time event ingestion
- Dynamic user profiling
- Hybrid recommendation engine
- Session-based personalization
- Collaborative filtering simulation
  
### Advanced Features
- A/B testing framework
- Explainability layer (XAI)
- WebSocket real-time updates
- Ranking score visualization

# 🚀 How to Run
### Backend

```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### Frontend
```
cd frontend
npm install
npm run dev
```

### Open App
```
http://localhost:5500/
```

## 🔌 API Endpoints

1. Get Recommendations

```GET /recommendations?user_id=u1```

#### Response
- ranked product list
- user profile
- A/B variant

3. Send User Event
   
```POST /event
Payload
{
  "user_id": "u1",
  "event_type": "click",
  "category": "Electronics"
}
```

3. WebSocket Stream
```ws://localhost:8000/ws```

#### Streams real-time updates:
- recommendations
- metrics
- profile updates
- latest event

## 🔮 Future Enhancements

### ML Improvements
- CTR prediction model (Logistic Regression / XGBoost)
- Neural ranking model (two-tower architecture)
- Embedding-based similarity search

### System Improvements
- Kafka-based event streaming
- Redis session store
- Microservices architecture
- Feature store (Feast)

### Experimentation
- Multi-armed bandits
- Dynamic A/B/n testing
- Statistical significance dashboard

### Explainability
- SHAP-based feature attribution
- LLM-generated explanations
- "Why not recommended" insights

### Scalability
- Distributed ranking service
- Caching layer (Redis)
- Horizontal scaling of event pipeline
