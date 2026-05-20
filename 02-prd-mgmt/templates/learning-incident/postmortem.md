# Postmortem

## Overview

This document explains what happened, why it happened, what the impact was, and what actions will prevent it from happening again. The goal is learning, not blame.

## Incident details

| Field | Value |
|---|---|
| Incident | Guided onboarding email failure |
| Incident lead | Engineering Manager |
| Date | 2026-06-12 |
| Severity | High |

## Summary

A scheduled onboarding email was sent to the wrong cohort because the segmentation rule was misconfigured. This caused some users to receive an irrelevant message and delayed the intended reminder flow.

## Impact

| Area | Details |
|---|---|
| Users affected | ~8,000 users |
| Customer impact | Confusing email experience and reduced trust |
| Business impact | Lower engagement on the reminder flow |
| Duration | 4 hours |

## Timeline

| Time | Event |
|---|---|
| 09:00 | Campaign triggered. |
| 09:20 | First user report received. |
| 09:35 | Support escalated the issue. |
| 10:00 | Campaign paused. |
| 11:15 | Root cause identified. |
| 13:00 | Fix deployed and campaign resumed with corrected segment. |

## Root cause

The audience segmentation rule used a stale field name, causing the email automation tool to target the wrong segment.

## Contributing factors

| Factor | Details |
|---|---|
| Process gap | No final audience validation before sending. |
| Tooling gap | No automated check for deprecated field names. |
| Review gap | Campaign QA did not include a sample audience test. |

## What went well

- Support identified the issue quickly.
- The campaign was paused promptly.
- The fix was small and deployable within the same day.

## What did not go well

- The audience rule was not validated end-to-end.
- The team lacked a simple pre-send checklist.
- The issue affected users before it was detected internally.

## Actions

| Action item | Owner | Due date | Status |
|---|---|---|---|
| Add pre-send audience validation checklist | Marketing Ops | 2026-06-18 | Open |
| Add automated field-name check | Data / Engineering | 2026-06-25 | Open |
| Improve campaign QA process | Support / Marketing | 2026-06-20 | Open |

## Learnings

- Campaign automation needs the same quality checks as product releases.
- Small data mistakes can create large user-facing issues.
- A short validation step can prevent a high-impact failure.

## Notes

- Keep this document factual and blameless.
- Focus on systems and process, not individuals.
- Track action items until they are complete.
