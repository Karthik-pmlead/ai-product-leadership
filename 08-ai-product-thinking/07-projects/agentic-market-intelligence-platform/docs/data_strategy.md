# 📊 Data Strategy — Agentic Market Intelligence Platform

---

## 🎯 Objective

Define how data is collected, structured, stored, and used to power:
- multi-agent reasoning
- memory
- evaluation
- future RAG systems

---

## 🧠 1. Data Sources

### Current (MVP)
- User queries (natural language)
- Agent outputs (risk, opportunity, recommendation, competitor)
- Evaluation scores
- Execution traces

---

### Future Expansion
- Financial APIs (stocks, earnings, filings)
- Web data (news, filings, reports)
- Internal enterprise documents
- Competitor datasets

---

## 🏗️ 2. Data Types

### 2.1 Structured Data
- agent outputs (JSON)
- evaluation scores
- execution graphs

### 2.2 Semi-Structured Data
- prompts
- reasoning traces
- memory context

### 2.3 Unstructured Data
- raw LLM outputs
- user queries
- external document ingestion (future)

---

## 🧠 3. Memory Strategy

### Current Approach
- Key-value memory store per company

Example:
```json id="mem1"
{
  "Tesla": {
    "risks": [...],
    "opportunities": [...]
  }
}
```

Future (RAG Evolution)
FAISS / vector DB
semantic embeddings
retrieval-based context injection

🔄 4. Data Flow

User Query
↓
Router Agent
↓
Agents generate outputs
↓
Evaluation layer scores outputs
↓
Memory store updated
↓
Data persisted for future retrieval

📦 5. Data Storage Strategy
MVP
In-memory Python dictionary
Production Evolution
Redis → short-term memory
PostgreSQL → structured logs
Vector DB → semantic memory

📊 6. Data Usage in System
Layer	Usage
Router	intent classification
Planner	execution graph
Agents	reasoning context
Memory	historical grounding
Evaluation	quality scoring

🚀 7. Key Principle

Data is treated as a reasoning asset, not just storage.
