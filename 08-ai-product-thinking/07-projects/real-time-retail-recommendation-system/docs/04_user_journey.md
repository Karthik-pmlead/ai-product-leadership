# 04 - User Journey

## Overview

This system simulates how a user interacts with an e-commerce platform and how recommendations adapt in real time.

---

## Step 1: User Lands on Platform

- User opens homepage
- System loads initial recommendations (baseline or hybrid via A/B test)

---

## Step 2: User Browses Products

User actions:
- view product
- click product
- add to cart
- purchase

Each action generates an event.

---

## Step 3: Event Capture

- Frontend sends event to backend
- Example:
  - category: Electronics
  - event_type: click

---

## Step 4: Real-Time Learning

System updates:
- user preference profile
- session memory

---

## Step 5: Recommendation Update

System recalculates:
- ranking scores
- session influence
- collaborative signals

---

## Step 6: Explainability Display

User sees:
- “Why recommended” section
- Signals influencing ranking

---

## Step 7: A/B Testing Assignment

User is assigned:
- Variant A → baseline ranking
- Variant B → hybrid ranking

---

## Step 8: Real-Time UI Update

- WebSocket pushes updates
- UI refreshes instantly

---

## Outcome

User experiences:
- personalized feed
- adaptive recommendations
- transparent reasoning
