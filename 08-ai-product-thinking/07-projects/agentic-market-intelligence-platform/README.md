# 🚀 Agentic Market Intelligence Platform

A multi-agent AI system that performs **company intelligence, competitor analysis, and strategic reasoning** using dynamic agent orchestration, memory, evaluation, and streaming execution.

---

## 🧠 Overview

This platform simulates a **real-world AI decision intelligence system** that:

- Understands user intent (Router Agent)
- Dynamically builds execution graphs (Planner)
- Executes specialized AI agents
- Maintains memory across queries
- Evaluates output quality
- Streams reasoning in real time

---

## 🏗️ Architecture

User Query
   ↓
Frontend (React Dashboard)
   ↓
FastAPI Streaming Backend
   ↓
Router Agent (Intent Classification)
   ↓
Dynamic Planner (Agent Graph Builder)
   ↓
Execution Layer:
   - Risk Agent
   - Opportunity Agent
   - Recommendation Agent
   - Competitor Agent
   ↓
Memory Layer (Context Persistence)
   ↓
Evaluation Layer (Quality Scoring)
   ↓
Streaming Response (SSE)

---

## ⚙️ Features

### 🧠 Multi-Agent System
- Modular AI agents for different reasoning tasks
- Dynamic execution flow based on intent

### 🔄 Dynamic Agent Graph
- Planner decides which agents to execute
- Supports conditional workflows

### 📊 Evaluation Layer
- Scores outputs on:
  - quality
  - confidence
  - coverage
  - actionability

### 🧩 Memory System
- Stores past company analysis
- Enables contextual reasoning

### ⚡ Streaming UX
- Real-time agent execution via SSE
- Live trace visualization

### 🔍 Explainability
- Full prompt, input, output tracing per agent
- Transparent AI decision-making

---

## 🧱 Tech Stack

### Backend
- FastAPI
- Python
- SSE (Streaming)

### Frontend
- React (Vite)
- JavaScript

### AI Layer
- LLM-ready (Ollama / OpenAI compatible)
- Modular prompt-based agents

---

## 📁 Project Structure

```text
backend/
  main.py
  agents/
  utils/
  models/

frontend/
  src/
    pages/
    components/

docs/
  architecture.md
  agent_flow.md
  evaluation_design.md

```

🚀 Getting Started

1. Clone repo
git clone https://github.com/your-repo/agentic-market-intelligence-platform.git
cd agentic-market-intelligence-platform

2. Backend setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

3. Frontend setup
cd frontend
npm install
npm run dev

4. Open app
http://localhost:5173

🧪 Example Queries

Try:

Tesla
Tesla vs BYD
Microsoft analysis
Apple competitive risks
NVIDIA opportunities

📡 API Endpoints
Streaming endpoint
GET /stream-analyze?query=Tesla

Health check

```
GET /
```

🧠 Key Design Principles

Dynamic agent orchestration (not fixed pipelines)
Explainable AI (trace + reasoning exposed)
Evaluation-driven intelligence system
Memory-augmented reasoning
Streaming-first UX

🔥 What makes this project special

This is not just an LLM wrapper.

It is a:

Multi-agent AI decision intelligence system with evaluation, memory, and dynamic planning.

🚀 Future Enhancements

Vector DB (FAISS / Pinecone) for RAG
Tool-using agents (web, APIs, databases)
Self-improving evaluation loop
LangGraph-style execution engine
Persistent distributed memory (Redis)

