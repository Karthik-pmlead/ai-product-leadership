
---

# 📁 `docs/architecture_diagram.md`

```markdown id="ad1"
# Architecture Diagram

```text
                 ┌──────────────────────┐
                 │   React Frontend     │
                 │  Graph Dashboard UI  │
                 └──────────┬───────────┘
                            │
                            │ User Actions
                            ↓
                 ┌──────────────────────┐
                 │     FastAPI API      │
                 │  Event Ingestion     │
                 └──────────┬───────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ↓              ↓              ↓
     ┌────────────┐ ┌────────────┐ ┌────────────┐
     │ Graph      │ │ Risk       │ │ Anomaly    │
     │ Engine     │ │ Engine     │ │ Engine     │
     └─────┬──────┘ └─────┬──────┘ └─────┬──────┘
           │              │              │
           └──────────────┼──────────────┘
                          ↓
               ┌──────────────────────┐
               │ Explainability Layer │
               └──────────┬───────────┘
                          ↓
               ┌──────────────────────┐
               │ WebSocket Streaming  │
               └──────────┬───────────┘
                          ↓
               ┌──────────────────────┐
               │ Live Dashboard UI    │
               └──────────────────────┘
