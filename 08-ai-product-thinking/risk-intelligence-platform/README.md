# FinTech Risk Intelligence Platform

An AI-assisted real-time FinTech Risk Intelligence Platform designed to simulate how modern fraud monitoring systems detect suspicious transactions, compute explainable risk scores, and surface operational alerts for analysts.

---

# Overview

This project demonstrates:

- Real-time transaction monitoring
- AI-assisted risk scoring
- Explainable fraud intelligence
- Event-driven architecture
- Operational alert workflows
- WebSocket streaming
- Human-in-the-loop review systems

---

# Architecture Diagram

```text
                        ┌────────────────────┐
                        │ Transaction Stream │
                        │   Simulator/API    │
                        └─────────┬──────────┘
                                  │
                                  ▼
                    ┌─────────────────────────┐
                    │ Risk Scoring Engine     │
                    │ - Velocity Analysis     │
                    │ - Geo Risk              │
                    │ - Device Trust          │
                    │ - Amount Anomaly        │
                    └─────────┬───────────────┘
                              │
                              ▼
                    ┌─────────────────────────┐
                    │ Explainability Engine   │
                    │ - Risk Reasons          │
                    │ - Confidence Score      │
                    │ - Recommended Actions   │
                    └─────────┬───────────────┘
                              │
                              ▼
                    ┌─────────────────────────┐
                    │ Alert Generation Layer  │
                    └─────────┬───────────────┘
                              │
                              ▼
                    ┌─────────────────────────┐
                    │ WebSocket Broadcast     │
                    └─────────┬───────────────┘
                              │
                              ▼
                    ┌─────────────────────────┐
                    │ React Risk Dashboard    │
                    │ - Live Transactions     │
                    │ - Alert Feed            │
                    │ - Charts                │
                    │ - Analyst Workflow      │
                    └─────────────────────────┘

```

## Tech Stack
| Layer     | Technology             |
| --------- | ---------------------- |
| Frontend  | React                  |
| Backend   | FastAPI                |
| Streaming | WebSockets             |
| Charts    | Recharts               |
| AI Logic  | Heuristic Risk Scoring |


## Features
- Real-time streaming
- Explainable AI alerts
- Confidence scoring
- Fraud simulation
- Risk analytics
- Operational dashboard

## Running Locally

#### Backend
```
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

#### Frontend
```
cd frontend

npm install

npm run dev
```

### Future Enhancements
- Kafka streaming
- PostgreSQL persistence
- Graph fraud analysis
- LLM investigation assistant
- RBAC
- Audit logging
