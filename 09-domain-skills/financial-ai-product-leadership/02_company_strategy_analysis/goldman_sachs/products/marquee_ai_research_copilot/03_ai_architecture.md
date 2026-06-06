# AI Architecture — Marquee AI Research Copilot

## 1. System Overview

Marquee AI Copilot is a multi-layer AI system designed to generate **grounded, explainable investment intelligence**.

---

## 2. High-Level Architecture

User Query
   ↓
Context Builder
   ↓
Retrieval Layer (RAG + structured data)
   ↓
Multi-Agent Reasoning Layer
   ↓
Risk & Compliance Filter
   ↓
Response Generator
   ↓
Explanation Layer
   ↓
User Output

---

## 3. Context Builder

Inputs:

- Portfolio holdings
- User role (PM, analyst, risk)
- Market conditions
- Historical queries
- Asset class exposure

Purpose:

> Ensure AI outputs are context-aware, not generic.

---

## 4. Retrieval Layer (RAG)

Sources:

- Goldman research reports
- Market data feeds
- Macro indicators
- Internal notes and insights

Responsibilities:

- Semantic retrieval
- Source ranking
- Freshness filtering

---

## 5. Multi-Agent Reasoning Layer

### Agents:

- Market Intelligence Agent
- Macro Analysis Agent
- Portfolio Risk Agent
- Sector Specialist Agent

Each agent:
- Processes query independently
- Produces structured reasoning outputs

---

## 6. Aggregation Layer

Combines outputs from agents into:

- Unified narrative
- Conflicting signal resolution
- Ranked insights

---

## 7. Risk & Compliance Layer

Ensures:

- No hallucinated financial facts
- Traceability of all claims
- Regulatory compliance checks
- Audit logging of outputs

---

## 8. Response Generation Layer

Outputs:

- Investment summary
- Key drivers
- Risks
- Portfolio impact
- Action recommendations

---

## 9. Explanation Layer

Every output includes:

- Data sources
- Reasoning steps
- Confidence score
- Alternative viewpoints

---

## 10. Key Design Principle

> LLMs are reasoning interfaces, not decision authorities.

Final decisions remain human-controlled.
