# 10 - System Architecture

# High-Level Architecture

```text
Frontend Dashboard
        ↓
FastAPI Backend API
        ↓
Graph Intelligence Layer
        ↓
Risk Propagation Engine
        ↓
Anomaly Detection Engine
        ↓
Explainability Layer
        ↓
WebSocket Streaming
        ↓
Live UI Updates
```

### Frontend

Responsibilities:

graph visualization
alerts
metrics
explainability display

#### Tech:
Backend

Responsibilities:

API handling
graph management
event processing
streaming updates

#### Tech:

FastAPI
Python
Graph Engine

Maintains:

nodes
edges
relationships
risk state
Risk Engine

Handles:

contagion propagation
risk scoring
threshold updates
Anomaly Engine

Detects:

suspicious graph concentration
highly connected risky entities
Streaming Layer

Uses:

### WebSockets

##### Enables:

live dashboard updates
real-time propagation visibility

React
Cytoscape.js
