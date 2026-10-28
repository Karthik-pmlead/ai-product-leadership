# Checkout Incident Detection Agent

**An n8n-based agent for checkout incident triage, severity classification, and downstream operational signaling.**

## Overview

Checkout failures can affect revenue, particularly when they occur during payment or affect high-value carts. As event volumes increase, manually reviewing each event becomes difficult and inconsistent.

This project explores how an AI agent can use checkout events, baseline metrics, and persistent processing state to produce structured operational decisions.

The n8n workflow uses Google Sheets for event data, baseline metrics, state, and command logging. An AI agent powered by GPT-4o-mini evaluates the available events, writes decisions to a command sheet, and sends a JSON payload to a downstream webhook using HTTP POST.

The agent publishes operational intent; it does not execute remediation.

## Problem Statement

How can e-commerce operations teams consistently prioritize potentially critical checkout failures while maintaining an auditable record of decisions and a structured handoff to downstream systems?

## Product Goals

- Prioritize payment failures and other potentially high-impact checkout incidents.
- Evaluate events using baseline metrics and explicit business rules.
- Process new events using persistent state.
- Record decisions in a structured command log.
- Publish decisions to downstream systems through a webhook.
- Keep automated actions bounded to detection, classification, and signaling.

## Architecture

```text
Manual Trigger
      |
      v
Read Processing State
      |
      v
Read Checkout Events
      |
      v
Filter Using Timestamp
      |
      v
AI Agent (GPT-4o-mini)
      |
      +---- Read Baseline Metrics
      |
      +---- Append Command to Google Sheets
      |
      +---- POST Command to Webhook
      |
      +---- Update Processing State
      |
      v
Return Action Summary
```

**Implementation note:** The agent's tools are available for the model to call. The exported configuration does not guarantee that every tool is called in the required order or that every event produces exactly one command.

## Technology Stack

- **Workflow orchestration:** n8n
- **AI model:** GPT-4o-mini
- **Operational data and state:** Google Sheets
- **Downstream integration:** HTTP POST webhook
- **Decision execution:** LLM-directed tool calls

## Google Sheets Data Model

The workflow references a Google spreadsheet with four tabs.

| Sheet | Purpose |
|---|---|
| `cart_event` | Checkout events and their attributes |
| `baseline_metric` | Reference baseline rates by checkout step |
| `state` | Processing checkpoint stored as key/value data |
| `agent` | Command log containing decisions and event details |

The expected checkpoint key is `last_processed_timestamp`. Confirm that the sheet headers and initial state row match the field names used by the workflow.

## Decision Policy

The agent prompt specifies these severity rules:

- **HIGH:** Payment-step failures.
- **HIGH:** Significantly high cart values.
- **HIGH:** Failure rates exceeding the corresponding baseline.
- **HIGH:** Multiple mobile failures indicating a potential application issue.
- **ALERT:** HIGH severity.
- **LOG:** LOW severity.

The cart-value threshold, mobile-failure aggregation window, and failure-rate calculation still require explicit definitions to make the policy repeatable and testable.

## Command Contract

Each command is intended to contain nine fields:

`command_id`, `action`, `severity`, `reason`, `checkout_step`, `cart_value`, `device`, `baseline_rate`, `timestamp`

The `Broadcast webhook` tool is configured for HTTP POST and accepts a JSON payload intended to contain these fields.

The downstream system should validate the payload before acting on it. Successful webhook delivery must be verified from execution results rather than inferred from the node configuration.

## State Management

The current workflow reads the state sheet and filters checkout events against the stored timestamp. The agent prompt instructs it to update the checkpoint after processing the available events.

The current filter uses an inclusive timestamp comparison (`afterOrEquals`). Consequently, an event whose timestamp equals the checkpoint may be processed again.

A reliable production design should use a stable unique event identifier or another unambiguous cursor, advance state only after the required processing steps succeed, and handle retries and partial failures explicitly.

## Evaluation Plan

Validate the workflow against representative test cases, including:

- High-value payment failures.
- Low-severity isolated failures.
- Baseline threshold breaches.
- Multiple mobile failures within a defined time window.
- First-run state initialization and empty input.
- Equal timestamps and out-of-order events.
- Repeated workflow execution.
- Google Sheets write failures.
- Webhook failures and retries.
- Command completeness and event-to-command traceability.

Report expected outcomes separately from observed execution results. A passing test suite demonstrates behavior on the tested cases; it does not establish general production accuracy.

## Success Metrics

Proposed evaluation metrics:

- Critical-event detection and routing accuracy.
- False-positive and false-negative rates.
- Duplicate command rate.
- Required-field completeness.
- Webhook delivery success rate.
- Processing latency and unprocessed-event count.
- Reduction in manual triage effort.

Revenue protected, incident-resolution speed, and operating-cost savings require representative measurements. They should not be presented as achieved outcomes without supporting evidence.

## Current Status

**Functional workflow prototype; reliability and production-readiness validation required.**

The exported workflow has a manual trigger and is marked inactive. It includes the core integration components, but the configuration alone does not establish deterministic tool execution, duplicate-free processing, successful delivery for every command, or safe recovery from partial failures.

## Next Steps

1. Define precise thresholds and a valid failure-rate calculation.
2. Replace inclusive timestamp filtering with reliable event identity or cursor semantics.
3. Enforce command creation, webhook delivery, and state advancement through explicit workflow control.
4. Add idempotency, retry handling, and failure-path observability.
5. Run and document tests for duplicates, partial failures, and webhook delivery.
6. Validate performance and business impact before making production-scale claims.

## Key Takeaways

- Stateful event processing requires more than storing a timestamp.
- Decision policies must be measurable and unambiguous.
- Structured commands create a clear boundary between detection and execution.
- Audit logs, idempotency, recovery, and observability are central to operational reliability.
- A working workflow is a prototype milestone; production readiness must be demonstrated through evidence.
