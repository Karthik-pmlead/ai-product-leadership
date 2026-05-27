# Model Evaluation Framework

---

# 🎯 Objective

Define how AI models are evaluated before and after deployment.

---

# 🧠 Evaluation Types

| Type | Purpose |
|---|---|
| Offline Evaluation | Pre-deployment testing |
| Online Evaluation | Production A/B testing |
| Human Evaluation | Qualitative assessment |
| Continuous Evaluation | Live monitoring |

---

# 📊 Key Metrics

## Classification Models
- accuracy
- precision
- recall
- F1-score

## Ranking Systems
- CTR
- NDCG
- MAP

## AI Systems
- response relevance
- latency
- user satisfaction

---

# 🔄 Evaluation Flow

```text
Train → Validate → Test → Deploy → Monitor → Iterate
```

# 🧠 AI-Specific Considerations
- hallucination rate
- bias detection
- drift monitoring
- robustness under noise
