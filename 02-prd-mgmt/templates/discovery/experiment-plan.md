# Experiment Plan

## Overview

This document defines the hypothesis, setup, metrics, and success criteria for a product experiment.

## Experiment details

| Field | Value |
|---|---|
| Experiment | Guided onboarding checklist |
| Owner | Product Manager |
| Date | 2026-05-20 |
| Duration | 3 weeks |

## Hypothesis

| Item | Details |
|---|---|
| Hypothesis | If we add a guided onboarding checklist, then more new users will complete setup and reach first value. |
| Why we believe it | Users often leave before knowing what to do next. |

## Audience

| Segment | Details |
|---|---|
| Target users | New self-serve users |
| Exclusions | Existing power users, enterprise accounts |

## Variations

| Variant | Description |
|---|---|
| Control | Current onboarding flow |
| Variant A | Current flow + checklist |
| Variant B | Checklist + tooltips |

## Metrics

| Metric | Baseline | Target |
|---|---:|---:|
| Activation rate | 32% | 45% |
| Setup completion rate | 24% | 40% |
| D7 retention | 18% | 22% |

## Guardrails

| Metric | Threshold |
|---|---:|
| Support tickets | No increase over 10% |
| Bounce rate | No increase over 5% |
| Time to load | No increase over 200ms |

## Success criteria

| Condition | Decision |
|---|---|
| Variant improves activation without hurting guardrails | Roll out |
| Mixed results | Iterate and retest |
| Negative results | Stop and reassess |

## Timeline

| Step | Date |
|---|---|
| Design complete | 2026-05-25 |
| Launch experiment | 2026-05-27 |
| Review results | 2026-06-17 |

## Notes

- Keep the hypothesis measurable.
- Use guardrails to avoid false wins.
- Define the decision before launch.
