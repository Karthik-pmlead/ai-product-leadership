# 03 - System Overview

## High-Level Architecture

The system is a **real-time event-driven recommendation engine**.

---

## Architecture Flow

User Action → Event API → Session/Profile Update → Ranking Engine → A/B Testing → WebSocket → UI

---

## Core Components

### 1. Frontend (React)
- Simulates user behavior
- Displays recommendations
- Shows metrics and explanations

---

### 2. Backend (FastAPI)
- Event ingestion
- Recommendation engine
- Session tracking
- A/B testing logic

---

### 3. Recommendation Engine
- Long-term profile model
- Session-based model
- Collaborative filtering model
- Hybrid ranking system

---

### 4. Explainability Layer
- Generates reasons for recommendations
- Improves transparency

---

### 5. Streaming Layer
- WebSocket-based real-time updates
- Pushes updated recommendations instantly

---

## Data Flow

1. User triggers event
2. Backend updates:
   - user profile
   - session memory
3. Ranking engine recalculates results
4. A/B test assigns variant
5. Explainability layer attaches reasoning
6. Results streamed to frontend

---

## Key Design Principles

- Low latency updates
- Modular recommendation logic
- Real-time feedback loop
- Experimentation-first architecture
