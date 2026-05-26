# 15 - System Design

# System Type

Real-time graph intelligence platform for financial risk analysis.

---

# Design Goals

- low-latency updates
- explainable risk propagation
- scalable graph modeling
- modular architecture

---

# Core Architecture

```text
User Event
    ↓
API Layer
    ↓
Graph Update Engine
    ↓
Risk Propagation
    ↓
Anomaly Detection
    ↓
Explainability Layer
    ↓
WebSocket Broadcast
    ↓
Frontend Dashboard
