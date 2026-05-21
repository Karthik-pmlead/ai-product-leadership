# PM Workflow

A lightweight operating system for day-to-day product management.

---

# Workflow Overview

```text
Customer Insights
    ↓
Discovery
    ↓
Product Definition
    ↓
Planning
    ↓
Communication
    ↓
Execution
    ↺
```

---

# PM Lifecycle

```mermaid
flowchart LR

A[Customer Feedback]
--> B[Data Exploration]
--> C[Competitor Research]
--> D[Brainstorm Ideas]
--> E[UX Ideation]
--> F[PRD]
--> G[User Stories]
--> H[Roadmap]
--> I[Stakeholder Communication]
--> J[Meeting Summary]

J --> A
```

---

# Repository Structure

```text
product-os/
│
├── pm-workflow.md
├── backlog.md
├── roadmap.md
├── decisions.md
├── weekly.md
│
├── 01_customer-insights/
│   ├── feedback/
│   ├── interviews/
│   └── data-exploration/
│
├── 02_discovery/
│   ├── competitor-research/
│   ├── brainstorms/
│   └── ux-ideation/
│
├── 03_product-definition/
│   ├── prds/
│   ├── user-stories/
│   └── requirements/
│
├── 04_planning/
│   ├── roadmaps/
│   ├── prioritization/
│   └── releases/
│
├── 05_communication/
│   ├── stakeholder-updates/
│   ├── meeting-notes/
│   └── decision-logs/
│
├── 06_execution/
│   ├── sprints/
│   ├── launches/
│   └── retros/
│
└── templates/
```

---

# Phase Breakdown

## 01 — Customer Insights

Goal:
Understand users, pain points, and behavioral signals.

Includes:
- customer feedback
- analytics
- support trends
- data exploration

Example files:

```text
2026-05-21-mobile-dropoff-analysis.md
top-user-pain-points-q2.md
```

---

## 02 — Discovery

Goal:
Explore opportunities and possible solutions.

Includes:
- competitor research
- brainstorming
- UX ideation

Example files:

```text
notion-vs-clickup-analysis.md
ai-assistant-brainstorm.md
```

---

## 03 — Product Definition

Goal:
Convert opportunities into actionable product specs.

Includes:
- PRDs
- user stories
- requirements

Example files:

```text
checkout-flow-prd.md
onboarding-user-stories.md
```

---

## 04 — Planning

Goal:
Prioritize and align execution timelines.

Includes:
- roadmap
- release planning
- prioritization

Example files:

```text
q3-platform-roadmap.md
release-plan-v2.md
```

---

## 05 — Communication

Goal:
Keep stakeholders and teams aligned.

Includes:
- stakeholder communication
- meeting summaries
- decision logs

Example files:

```text
2026-05-21-growth-sync.md
remove-social-login-decision.md
```

---

## 06 — Execution

Goal:
Track delivery, launches, and iteration cycles.

Includes:
- sprint tracking
- launches
- retrospectives

Example files:

```text
sprint-24-notes.md
launch-checklist-mobile-v1.md
```

---

# File Naming Convention

Use:

```text
YYYY-MM-DD_topic_type.md
```

Examples:

```text
2026-05-21_checkout-prd.md
2026-05-21_growth-sync.md
2026-05-18_q3-roadmap.md
```

---

# Operating Principles

- Keep documents lightweight
- Prefer many small docs over giant docs
- One topic per file
- Archive stale work quarterly
- Maintain decision logs
- Keep roadmap outcome-focused
- Capture insights continuously

---

# Core Operating Files

| File | Purpose |
|---|---|
| `pm-workflow.md` | Main PM operating system |
| `backlog.md` | Raw ideas and opportunities |
| `roadmap.md` | High-level planning |
| `weekly.md` | Weekly priorities and updates |
| `decisions.md` | Important product decisions |

---
