# Release Plan

## Overview

This document defines the release scope, dependencies, rollout steps, and readiness checks for the launch.

## Release details

| Field | Value |
|---|---|
| Release | Guided onboarding v1 |
| Owner | Product Manager |
| Date | 2026-05-20 |
| Target release | 2026-06-12 |

## Scope

| In scope | Out of scope |
|---|---|
| Onboarding checklist | Full app redesign |
| Tooltips | Enterprise onboarding |
| Lifecycle nudges | Billing changes |
| Event tracking | Mobile app rewrite |

## Dependencies

| Dependency | Owner | Status |
|---|---|---|
| UX designs | Design | In progress |
| Checklist implementation | Engineering | Not started |
| Email automation | Marketing Ops | Not started |
| Tracking validation | Data | Not started |

## Rollout plan

| Phase | Audience | Criteria |
|---|---|---|
| Beta | 10% of new users | Metrics stable and no major bugs |
| Ramp-up | 50% of new users | Activation improves and support load stable |
| Full rollout | All eligible users | Guardrails remain healthy |

## Readiness checklist

| Item | Status | Owner |
|---|---|---|
| Requirements approved | Done | Product |
| Designs complete | In progress | Design |
| QA completed | Not started | Engineering / QA |
| Support guide ready | Not started | Support |
| Release notes drafted | Not started | Product |
| Rollback plan prepared | Not started | Engineering |

## Launch-day steps

| Step | Owner | Time |
|---|---|---|
| Final readiness check | Product | T-1 day |
| Release to beta | Engineering | Launch day |
| Monitor metrics and logs | Data / Product | First 24 hours |
| Confirm support coverage | Support | Launch day |

## Rollback plan

| Condition | Action |
|---|---|
| Major bug or metric degradation | Disable feature flag and revert rollout. |

## Notes

- Keep the plan practical and current.
- Update status as dependencies move.
- Use this doc to coordinate the final release path.
