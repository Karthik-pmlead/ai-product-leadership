# Engineering Tradeoffs

# Overview

The MVP intentionally prioritizes:
- architectural storytelling
- operational workflows
- rapid prototyping
- demo quality

over production completeness.

This document explains the major technical tradeoffs made during development.

---

# Tradeoff Philosophy

The goal of the MVP is to demonstrate:
- AI systems thinking
- operational intelligence
- event-driven design
- explainability
- MLOps awareness

while remaining:
- lightweight
- fast to build
- easy to demo

---

# Key Engineering Tradeoffs

# 1. Lightweight NLP vs Large Multilingual Models

## Chosen Approach
- lightweight Hugging Face inference

## Alternative
- XLM-RoBERTa large multilingual models

---

## Why

Large transformer models:
- increase setup complexity
- require large downloads
- slow local inference
- increase demo instability

The lightweight approach:
- improves reliability
- accelerates MVP delivery
- simplifies onboarding

---

# 2. Simulated Streaming vs Kafka

## Chosen Approach
- simulated review events
- WebSocket broadcasting

## Alternative
- Kafka streaming infrastructure

---

## Why

Kafka adds:
- infrastructure complexity
- operational overhead
- deployment requirements

For MVP scope:
- WebSockets sufficiently demonstrate streaming architecture.

---

# 3. In-Memory Storage vs Persistent Database

## Chosen Approach
- temporary in-memory storage

## Alternative
- PostgreSQL or distributed databases

---

## Why

Persistent storage was excluded to:
- reduce setup time
- simplify architecture
- focus on operational analytics

---

# 4. Heuristic Topic Classification vs Advanced NLP

## Chosen Approach
- keyword-based categorization

## Alternative
- semantic topic modeling
- embeddings
- LLM categorization

---

## Why

Heuristic classification:
- is faster to build
- easier to explain
- reduces infrastructure requirements

---

# 5. Simulated MLOps vs Production MLOps

## Chosen Approach
- lightweight observability panel

## Alternative
- MLflow
- feature stores
- retraining pipelines

---

## Why

The MVP demonstrates:
- architectural understanding
- operational awareness

without requiring:
- heavy ML infrastructure

---

# 6. Monolithic Backend vs Microservices

## Chosen Approach
- single FastAPI backend

## Alternative
- distributed services

---

## Why

Microservices introduce:
- deployment overhead
- orchestration complexity
- networking concerns

For MVP scope:
- modular monolith improves simplicity.

---

# Product Tradeoffs

| Tradeoff | Reason |
|---|---|
| No authentication | Faster prototyping |
| No RBAC | Focus on analytics |
| No persistence | Simpler setup |
| No retraining | MVP AI workflow focus |
| No cloud infra | Local demo optimization |

---

# UX Tradeoffs

The dashboard prioritizes:
- operational visibility
- low cognitive load
- fast issue discovery

over:
- enterprise workflow depth
- advanced customization

---

# Future Production Path

Production architecture may evolve toward:
- Kafka
- distributed inference
- Kubernetes
- model registry systems
- vector databases
- advanced observability

---

# Conclusion

The tradeoffs intentionally optimize for:
- high signal architecture
- strong demo quality
- operational AI storytelling
- scalable design patterns
- rapid implementation
