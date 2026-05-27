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

The platform simulates capabilities commonly seen in:

Stripe Radar
PayPal Fraud Systems
Revolut Risk Operations
Trust & Safety Intelligence Platforms

---
# Demo Video

1. Project overview
2. Dashboard walkthrough
3. Real-time transaction simulation
4. Explainability engine
5. Architecture explanation
6. Scaling discussion
7. Future AI enhancements

# Demo Video

👉 [ Watch demo here](https://drive.google.com/file/d/1pTD5vmzz20cE_cKC4N27J0sXj1ASb4vN/view?usp=drive_link)

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

## Real-World Use Cases

### Fraud Detection

#### Detect:

- card fraud
- suspicious transfers
- account takeover attempts
- synthetic identity fraud

### AML Monitoring

#### Monitor:

- suspicious transaction chains
- sanctions exposure
- abnormal cross-border flows
- money laundering patterns

### Trust & Safety Operations

####Used by:

- digital wallets
- ride-sharing platforms
- marketplaces
- BNPL providers
- neobanks

### Operational Intelligence

#### Enable:

- analyst triage workflows
- fraud escalation pipelines
- real-time investigations
- operational monitoring

### Explainability Layer

- The explainability engine converts raw risk signals into human-readable intelligence. Instead of returning only a numeric score, the system explains:

- why the transaction was flagged
- which signals contributed most
- confidence level
- recommended analyst action

### HIGH RISK ALERT

#### Reasons:
- High transaction velocity detected
- Geo mismatch identified
- Untrusted device fingerprint
- Large abnormal transaction amount

- Confidence: 91%
- Recommended Action: Escalate for analyst review

## System Workflow

```
1. Transaction Generated
        ↓
2. Risk Scoring Engine Evaluates Signals
        ↓
3. Explainability Layer Generates Reasons
        ↓
4. Alert Service Classifies Severity
        ↓
5. WebSocket Broadcast Streams Event
        ↓
6. React Dashboard Updates Live
        ↓
7. Analyst Reviews Alert
```

## Metrics Framework
### Business Metrics
| Metric	| Purpose |
|---------|---------|
| Fraud Detection Rate	| Measures successful fraud identification |
| False Positive Rate	| Measures alert quality |
| Analyst Resolution Time	| Operational efficiency |
| Financial Loss Prevented	| Business impact |
| Alert Escalation Rate |	Risk workload tracking |

### AI Metrics
| Metric	| Purpose |
|---------|---------|
| Precision	| Accuracy of fraud predictions |
| Recall	| Fraud coverage |
| Confidence Calibration	| AI trustworthiness |
| Explainability Coverage	| Transparency measurement |
| Drift Detection	| Model stability |
   
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

## Endpoints

| Endpoint | Purpose |
|---------|---------|
| /transactions	| Fetch transactions |
| /alerts |	Fetch alerts |
| /simulate	 | Simulate fraud transaction |
| /ws	 | Real-time streaming |


| Key AI Concepts |
|------------------|
| Explainable AI | 
| Confidence scoring | 
| Human-in-the-loop review | 
| Behavioral anomaly detection | 
| Operational intelligence | 
| Responsible AI | 


### Future Enhancements
- Kafka streaming
- PostgreSQL persistence
- Graph fraud analysis
- LLM investigation assistant
- RBAC
- Audit logging
