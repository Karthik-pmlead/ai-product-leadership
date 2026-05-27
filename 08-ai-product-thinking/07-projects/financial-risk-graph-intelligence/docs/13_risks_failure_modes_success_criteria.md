# 13 - Risks, Failure Modes & Success Criteria

# Risks

## 1. False Positives
Excessive alerts may overwhelm analysts.

---

## 2. Graph Complexity Explosion
Large-scale graphs may become computationally expensive.

---

## 3. Propagation Over-Amplification
Incorrect propagation logic may exaggerate risk.

---

# Failure Modes

## 1. WebSocket Disconnects
UI may stop receiving updates.

---

## 2. Invalid Event Injection
Improper events may corrupt graph state.

---

## 3. Alert Saturation
Too many anomalies reduce effectiveness.

---

# Success Criteria

## Functional Success
- graph updates correctly
- risk propagates properly
- alerts trigger accurately

---

## UX Success
- intuitive graph visualization
- understandable explainability layer

---

## Technical Success
- low-latency updates
- stable WebSocket streaming
- responsive UI interactions
