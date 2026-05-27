# 15 - System Design (Deep Dive)

## 1. System Type

This is a:

> Real-Time Event-Driven Personalized Recommendation System

---

## 2. Design Goals

- low-latency personalization (<500ms)
- continuous learning from user behavior
- explainable recommendations
- A/B experimentation support
- modular ML ranking pipeline

---

## 3. High-Level Architecture
```
Frontend (React)
↓
Event API (FastAPI)
↓
Event Processing Layer
↓
Session Store + User Profile Store
↓
Recommendation Engine
├── Long-term profile model
├── Session-based model
├── Collaborative filtering model
↓
Hybrid Ranking Engine
↓
A/B Testing Router
↓
Explainability Layer
↓
WebSocket Streaming Layer
↓
Frontend UI
```

---

## 4. Core Design Patterns

### 4.1 Event-Driven Architecture
- every user action triggers system update

### 4.2 Streaming Architecture
- WebSocket pushes updates in real-time

### 4.3 Layered ML Pipeline
- multiple ranking signals combined

---

## 5. Ranking System Design

Final scoring:
```
Score =
0.5 * User Profile Score

0.3 * Session Score
0.2 * Collaborative Score
```

---

## 6. Explainability System

Each recommendation includes:
- long-term reason
- session behavior reason
- collaborative signal reason

---

## 7. A/B Testing Design

- deterministic hashing (MD5)
- variant-based ranking engine selection
- future: multi-armed bandit upgrade

---

## 8. Bottlenecks (MVP)

- in-memory state
- single-node processing
- no persistence layer

---

## 9. Production Evolution Path

MVP → Microservices → Distributed Streaming System → ML Platform

---

## Summary

This system demonstrates **end-to-end modern recommendation system design principles used in FAANG-scale platforms**.
