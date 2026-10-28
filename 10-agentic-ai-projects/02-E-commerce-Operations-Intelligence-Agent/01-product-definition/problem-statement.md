# Problem Statement

## Background
E-commerce teams must monitor checkout failures to identify issues that can impact revenue. As event volumes grow, manual triage becomes difficult to scale consistently, particularly for payment failures and high-value carts.

## Problem
How can checkout events be evaluated consistently against business rules and baseline metrics to identify incidents requiring operational attention, without manually reviewing every event?

## Objective
Build an n8n-based E-commerce Operations Agent that:

- Reads checkout events, baseline metrics, and processing state from Google Sheets.
- Evaluates event severity and determines `ALERT` or `LOG`.
- Records each decision in an auditable command sheet.
- Publishes a structured JSON command through an HTTP POST webhook.
- Maintains a processing checkpoint to reduce duplicate processing.

## Success Criteria
- Correctly classify representative high- and low-severity scenarios.
- Produce one command per processed event.
- Deliver a complete webhook payload for each decision.
- Track processing state and handle failures without losing or duplicating events.

**Scope:** The agent detects, classifies, logs, and signals incidents. Automated remediation is out of scope.

**Constraint:** Duplicate prevention, reliable recovery, and production-scale performance must be validated through testing before production readiness can be claimed.
