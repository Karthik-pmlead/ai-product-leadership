# 05 - AI/ML System Breakdown

## Overview

This system uses a hybrid recommendation approach combining:
- rule-based ranking
- session-based signals
- collaborative filtering
- explainability layer

---

## 1. User Profile Model (Long-Term Learning)

Tracks persistent preferences:
- category affinity score
- updated via weighted events

Formula:
- view = 1
- click = 3
- cart = 5
- purchase = 8

---

## 2. Session-Based Model (Short-Term Intent)

Captures:
- recent interactions
- current browsing context

Used to:
- detect intent shifts
- boost recent categories

---

## 3. Collaborative Filtering Model

Uses:
- user-item category interactions
- similarity between users

Goal:
- recommend items liked by similar users

---

## 4. Hybrid Ranking Model

Final score:
score =
0.5 * long_term_profile +
0.3 * session_signal +
0.2 * collaborative_signal


---

## 5. Explainability Layer (XAI)

For each recommendation:
- long-term reason
- session reason
- collaborative reason

---

## 6. A/B Testing Layer

- Variant A: baseline ranking
- Variant B: hybrid ranking

Used to evaluate:
- engagement impact
- conversion improvement

---

## Summary

This is a **multi-signal ranking system**, similar in structure to production recommender systems.
