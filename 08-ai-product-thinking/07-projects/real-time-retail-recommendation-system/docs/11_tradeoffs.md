# 11 - Tradeoffs

## Overview

This system balances simplicity (MVP) with realistic architecture patterns.

---

## 1. Simplicity vs Scalability

### Decision
- In-memory storage instead of databases

### Tradeoff
- ✔ Fast development
- ✘ Not scalable for large user base

---

## 2. Real-time vs Batch Processing

### Decision
- Fully real-time updates via WebSocket

### Tradeoff
- ✔ Immediate feedback
- ✘ Higher compute overhead

---

## 3. Rule-Based vs ML-Based Ranking

### Decision
- Rule-based hybrid ranking system

### Tradeoff
- ✔ Explainable, easy to debug
- ✘ Not as accurate as deep ML models

---

## 4. Session Memory vs Persistent Storage

### Decision
- Short-lived session_store in memory

### Tradeoff
- ✔ Simple architecture
- ✘ No persistence after restart

---

## 5. A/B Testing Simplicity

### Decision
- MD5 hash-based user bucket assignment

### Tradeoff
- ✔ Deterministic + simple
- ✘ Not dynamic or configurable

---

## Summary

This MVP intentionally prioritizes:
- clarity
- explainability
- system design demonstration

over production scalability.
