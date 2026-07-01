# Agentic Market Intelligence Platform — Architecture

## Overview

A multi-agent AI system that performs company and competitor intelligence using dynamic orchestration, memory, evaluation, and streaming execution.

---

## High-Level Architecture

User Query
   ↓
Frontend (React Dashboard)
   ↓
FastAPI Backend (Streaming SSE)
   ↓
Router Agent (Intent Classification)
   ↓
Dynamic Planner (Agent Graph Builder)
   ↓
Execution Layer (Risk / Opportunity / Recommendation / Competitor Agents)
   ↓
Memory Layer (Context Persistence)
   ↓
Evaluation Layer (Quality Scoring)
   ↓
Streaming Response (Real-time UI updates)

---

## Core Components

### 1. Frontend (React + Vite)
- Dashboard UI
- Live agent trace visualization
- Reasoning panel
- Evaluation display

---

### 2. Backend (FastAPI)
- REST + SSE streaming API
- Orchestrates multi-agent workflow
- Manages execution pipeline

---

### 3. Router Agent
- Classifies intent
- Extracts entities (company, competitor)

---

### 4. Dynamic Planner
- Converts intent → execution graph
- Enables conditional agent execution

---

### 5. Agents
- Risk Agent → identifies risks
- Opportunity Agent → finds growth drivers
- Recommendation Agent → generates strategy
- Competitor Agent → comparative intelligence

---

### 6. Memory Layer
- Stores company-level historical context
- Enables contextual reasoning across queries

---

### 7. Evaluation Layer
- Scores agent outputs on:
  - quality
  - confidence
  - coverage
  - actionability

---

## Data Flow

1. User submits query
2. Router identifies intent
3. Planner builds execution graph
4. Agents execute dynamically
5. Memory enriches context
6. Evaluation scores outputs
7. Results streamed to UI

---

## Key Design Principles

- Modular agents (plug-and-play)
- Stateless backend execution
- Stateful memory layer
- Explainable AI (trace + prompts exposed)
- Streaming-first UX
