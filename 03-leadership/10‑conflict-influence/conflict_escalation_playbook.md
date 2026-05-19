# ⚖️ Conflict Escalation Playbook

> Structured escalation model used in high-performing engineering and product orgs to resolve cross-functional conflict quickly, fairly, and with clear ownership.

---

# 🎯 Objective

- Resolve conflicts with minimal delay
- Ensure clear decision ownership
- Avoid ambiguity in priorities and trade-offs
- Escalate only when required, with structured inputs

---

# 🧭 Conflict Types

| Type | Example |
|---|---|
| Priority | Competing roadmap features |
| Resource | Shared engineering/ML capacity |
| Technical | Architecture disagreements |
| Product vs Eng | Scope vs feasibility |
| Cross-team | Platform dependency conflicts |

---

# 🔄 Escalation Levels

## 🟢 Level 0 — Team Resolution
- Direct discussion between owners
- Use data + impact analysis
- Agree on trade-offs
- Document decision

**Output:** Decision log updated (no escalation)

---

## 🟡 Level 1 — Peer Alignment
- Involve both team DRIs
- Time-box discussion (30–60 mins)
- Compare options and trade-offs

**Output:** Agreement OR documented escalation

---

## 🟠 Level 2 — Manager / Program Lead
- Review OKR + delivery impact
- Evaluate resource constraints
- Make binding decision if possible

**Output:** Updated plan + decision log entry

---

## 🔴 Level 3 — Director / VP Decision
- Required for cross-org or strategic conflicts
- 1-pager required:
  - Problem
  - Options
  - Recommendation
  - Impact

**Output:** Final binding decision

---

## ⚫ Level 4 — Executive Escalation
- Strategic or multi-org conflicts
- Limited options (max 3)
- Pre-read required (no ad-hoc meetings)

**Output:** Strategic decision + org alignment update

---

# 📄 Escalation Template

````markdown
# Escalation Summary

## Problem
Brief description of conflict

## Teams Involved
List stakeholders

## Impact
- Delivery:
- Business:
- Risk:

## Options
1.
2.
3.

## Recommendation
Preferred option with rationale

## Decision Needed By
Date / milestone

## Dependencies
Blocked items or teams

````




# 💬 Example 1 — Roadmap Priority Conflict (Product vs Engineering)

## Context
Product wants Feature A in Q1. Engineering says it increases system risk and suggests deferring.

---

## ❌ Ineffective Conversation

**Product:** We really need Feature A this quarter. It’s important for growth.

**Engineering:** It will break the system stability. We can’t do it.

**Product:** But it’s a top priority.

**Engineering:** Still no.

➡ Outcome: Stalemate, no decision, escalation delayed

---

## ✅ Effective Conversation

**Product (DRI):**  
We need to decide between Feature A this quarter vs delaying it. Expected impact is +12% activation.

**Engineering (DRI):**  
Risk analysis shows a 25% increase in system load and regression risk in recommendation latency.

**Product:**  
Option 1: Ship now with reduced scope  
Option 2: Delay full launch by 1 sprint  

**Engineering:**  
Recommend Option 1 with limited rollout + feature flag.

**Decision Owner (EM/PM):**  
We proceed with Option 1, feature-flagged rollout + monitoring.

➡ Outcome: Fast decision, controlled risk, documented trade-off

---

# 💬 Example 2 — Shared Engineering Resource Conflict

## Context
Two teams need same ML engineer for critical sprint.

---

## ❌ Ineffective Conversation

**Team A:** We need them full-time.

**Team B:** We also need them full-time.

**Manager:** Let’s figure it out later.

➡ Outcome: Sprint delays + hidden prioritization

---

## ✅ Effective Conversation

**Team A:** We need 30 SP delivery dependent on ML support.

**Team B:** We have a model release impacting revenue KPI.

**Manager:**  
Capacity constraint = 1 engineer, 2 priorities.

Options:
1. Split 50/50 (risk both timelines)
2. Prioritize Team B (higher revenue impact)
3. De-scope Team A sprint

**Decision:** Option 2 approved due to revenue impact.

➡ Outcome: Explicit trade-off + aligned decision

---

# 💬 Example 3 — Architecture Disagreement

## Context
Two engineers disagree on API design.

---

## ❌ Ineffective Conversation

**Engineer A:** My design is cleaner.

**Engineer B:** No, mine is better.

➡ Outcome: Opinion-based deadlock

---

## ✅ Effective Conversation

**Engineer A:** Option 1 reduces latency by 15% but increases complexity.

**Engineer B:** Option 2 is simpler but may not scale beyond 2M users.

**Tech Lead:**  
Decision criteria:
- scalability
- maintainability
- time-to-ship

We choose Option 1 with simplified abstraction layer.

➡ Outcome: Decision based on system criteria

---

# 💬 Example 4 — Product vs Data Science Trade-off

## Context
Model improvement requires delaying feature release.

---

## ✅ Conversation

**Product:** Feature is tied to Q2 launch commitment.

**DS Team:** Model accuracy is currently 82%, target is 90% for acceptable UX.

**PM:**  
Option 1: Launch with current model  
Option 2: Delay 2 weeks for model improvement

**DS Lead:** Recommend Option 2 due to churn risk.

**Decision:** Delay launch by 2 weeks.

➡ Outcome: Quality-first decision with explicit rationale

---
