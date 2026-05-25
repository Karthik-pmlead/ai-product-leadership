# Architecture Diagram (System Overview)

## High-Level Flow

```text
                   ┌──────────────────────┐
                   │   React Frontend     │
                   │ (Event Simulator UI) │
                   └─────────┬────────────┘
                             │
                             │ User Actions
                             ↓
               ┌────────────────────────────┐
               │     FastAPI Backend        │
               │  (Event Ingestion Layer)   │
               └─────────┬──────────────────┘
                         │
     ┌───────────────────┼────────────────────┐
     │                   │                    │
     ↓                   ↓                    ↓
┌───────────┐   ┌──────────────┐   ┌────────────────┐
│ User      │   │ Session Store │   │ Collaborative  │
│ Profile   │   │ (Short-term)  │   │ Filtering      │
│ (Long)    │   └──────────────┘   └────────────────┘
└─────┬─────┘            │                    │
      │                 └────────┬───────────┘
      │                          ↓
      │              ┌──────────────────────┐
      └─────────────▶│ Hybrid Ranking Engine│
                     └─────────┬────────────┘
                               │
                    ┌──────────────────────┐
                    │ Explainability Layer │
                    └─────────┬────────────┘
                               │
                    ┌──────────────────────┐
                    │ A/B Testing Router   │
                    └─────────┬────────────┘
                               │
                    ┌──────────────────────┐
                    │ WebSocket Stream     │
                    └─────────┬────────────┘
                               │
                               ↓
                    ┌──────────────────────┐
                    │ Live UI Updates      │
                    └──────────────────────┘
