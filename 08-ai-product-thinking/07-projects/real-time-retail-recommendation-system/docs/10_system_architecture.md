# 10 - System Architecture

## High-Level Architecture

The system is a **real-time event-driven recommendation engine with streaming updates**.

---

## Architecture Diagram

```
User Action (Frontend)
↓
Event API (FastAPI)
↓
Session Store + User Profile Update
↓
Recommendation Engine
├── Profile-based ranking
├── Session-based ranking
├── Collaborative filtering
↓
A/B Testing Layer
↓
Explainability Engine
↓
WebSocket Streaming Layer
↓
Frontend UI (React Dashboard)
```


---

## Core Components

### 1. Frontend Layer
- React UI
- Event simulation
- Live recommendation rendering

---

### 2. API Layer
- FastAPI REST endpoints
- WebSocket endpoint

---

### 3. Event Processing Layer
- /event ingestion
- session updates
- profile updates

---

### 4. Recommendation Engine
- ranking logic
- hybrid scoring model
- collaborative filtering

---

### 5. Experimentation Layer
- A/B testing (A vs B routing)

---

### 6. Explainability Layer
- generates reasoning per recommendation

---

### 7. Streaming Layer
- WebSocket broadcast system

---

## Data Flow Summary

User → Event → Processing → Ranking → Explainability → Streaming → UI
