# 13 - Risks, Failure Modes, Success Criteria

---

## 1. Risks

### R1: Session Memory Overflow
- session_store grows indefinitely

### R2: Ranking Instability
- small changes in events can cause large ranking shifts

### R3: Fake Event Injection
- users can simulate biased behavior

### R4: WebSocket Connection Drops
- real-time UI updates may fail

---

## 2. Failure Modes

### F1: Empty Recommendations
- caused by missing category mapping

### F2: Broken Ranking Engine
- division/logic errors in scoring function

### F3: Explainability Failure
- missing or empty reason lists

### F4: A/B Test Imbalance
- uneven traffic distribution (small sample bias)

---

## 3. System Constraints

- in-memory storage only
- single-node backend
- no distributed processing
- simulated ML logic only

---

## 4. Success Criteria

### Functional Success
- recommendations update after every event
- explainability always present
- A/B variant is assigned correctly

---

### Performance Success
- event → recommendation latency < 500ms (MVP goal)

---

### Product Success
- visible personalization effect
- user engagement increases in simulation
- clear ranking shifts after events

---

## 5. Observability (Future)

- logs for every event
- A/B test metrics dashboard
- ranking score tracking
