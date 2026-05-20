# PRD

## Overview

This document defines the problem, goals, scope, requirements, and success metrics for the product initiative.

## Context

| Field | Value |
|---|---|
| Product | Guided onboarding and lifecycle nudges |
| Owner | Product Manager |
| Stakeholders | Design, Engineering, Marketing, Support |
| Date | 2026-05-20 |
| Status | Draft |

## Problem statement

| Item | Details |
|---|---|
| User problem | New users do not know how to reach first value. |
| Business problem | Low activation reduces retention and monetization. |
| Evidence | Funnel drop-off, support tickets, interview feedback. |

## Goals

| Goal | Success measure |
|---|---|
| Improve activation | Increase first-week activation from 32% to 50%. |
| Improve retention | Increase D7 retention from 18% to 25%. |
| Reduce support load | Reduce setup-related tickets by 15%. |

## Non-goals

| Non-goal | Reason |
|---|---|
| Enterprise onboarding | Not the target segment. |
| Full UX redesign | Too large for this release. |
| Billing improvements | Not related to the core problem. |

## User stories

| User story | Priority |
|---|---|
| As a new user, I want to see the next step so I can get started quickly. | High |
| As a new user, I want contextual help so I do not get stuck. | High |
| As a returning user, I want a reminder if I stop halfway. | Medium |

## Requirements

| Requirement | Details | Priority |
|---|---|---|
| Onboarding checklist | Show the 3 most important setup steps. | High |
| Tooltips | Provide contextual guidance on key actions. | High |
| Lifecycle nudges | Send reminder emails to stalled users. | Medium |
| Analytics tracking | Track step completion and drop-off. | High |

## UX considerations

| Area | Details |
|---|---|
| Simplicity | Keep steps short and clear. |
| Timing | Show nudges only after meaningful inactivity. |
| Accessibility | Tooltips and copy must be easy to read. |

## Dependencies

| Dependency | Owner | Status |
|---|---|---|
| Event tracking | Analytics | Open |
| Email automation | Marketing Ops | Open |
| UI changes | Engineering | Open |

## Success metrics

| Metric | Baseline | Target |
|---|---:|---:|
| Activation rate | 32% | 50% |
| D7 retention | 18% | 25% |
| Setup completion rate | 24% | 40% |
| Support tickets | 100/week | 85/week |

## Risks

| Risk | Mitigation |
|---|---|
| Users ignore checklist | Keep it brief and contextual. |
| Tooltips overwhelm users | Limit to high-value actions. |
| Email nudges feel spammy | Add frequency caps and targeting. |

## Rollout plan

| Phase | Details |
|---|---|
| Beta | 10% of new users |
| Full rollout | After metrics improve and guardrails hold |

## Open questions

| Question | Owner |
|---|---|
| Which 3 steps are most important in onboarding? | Product / Research |
| What is the best timing for lifecycle nudges? | Marketing / Analytics |

## Notes

- This PRD should stay linked to the experiment plan and research summary.
- Update requirements as you learn.
