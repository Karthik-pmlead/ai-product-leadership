# Evaluation Plan — Intelligent Message Routing Agent

## 1. Purpose

Evaluate whether the n8n-based Intelligent Message Routing Agent correctly classifies incoming messages, selects the intended Google Sheets destination, extracts relevant information, and handles failures appropriately.

This document defines the evaluation approach and proposed acceptance targets. **No performance results are claimed until testing has been executed and documented.**

## 2. System Under Evaluation

The current workflow contains:

- **Input:** n8n Chat Trigger
- **Agent:** n8n AI Agent
- **Language model:** OpenRouter Chat Model (`openai/gpt-4o-mini`)
- **Destinations:** Three Google Sheets append tools

| Intent | Tool | Destination |
|---|---|---|
| Demo/Sales | `Append to demo request` | Demo |
| Support | `Append to Support` | Support |
| Spam | `Append to spam` | Spam |

The system prompt instructs the agent to use only one tool per message. This instruction does not independently guarantee exactly-once execution.

## 3. Routing Policy

| Message category | Expected destination |
|---|---|
| Product demo, pricing, sales call | Demo |
| Bugs, login problems, billing issues, help requests | Support |
| Promotional, irrelevant, or suspicious messages | Spam |
| Messages that do not clearly fit Demo/Sales or Support | Spam under the current prompt |

**Known limitation:** Unmatched messages are routed to Spam as a fallback. This does not establish that they are genuine spam. A review or clarification path may be considered in a future iteration.

## 4. Evaluation Objectives

The evaluation will determine whether the workflow:

1. Routes messages to the expected destination.
2. Extracts destination-specific fields accurately.
3. Preserves the original message content.
4. Avoids inventing missing names, email addresses, or issue details.
5. Applies the documented fallback behavior consistently.
6. Reports tool failures without falsely confirming success.
7. Avoids unintended duplicate writes during repeated execution.
8. Resists instructions embedded in incoming messages that attempt to override routing rules.

## 5. Evaluation Metrics

The following targets are **proposed acceptance criteria, not measured outcomes**.

| Metric | Definition | Proposed target |
|---|---|---:|
| Routing accuracy | Messages routed to the expected destination ÷ total labeled messages | ≥95% |
| Field completeness | Applicable required fields correctly populated ÷ applicable required fields evaluated | ≥98% |
| Original-message preservation | Records preserving the original message as expected ÷ records evaluated | 100% |
| False success rate | Failed writes followed by a success confirmation ÷ failed write attempts | 0% |
| Duplicate-write rate | Unintended duplicate records ÷ eligible repeated-execution test cases | 0% |
| Unresolved test cases | Cases without a documented outcome | 0 |

### Metric interpretation

- Evaluate routing against expected destinations established before each test.
- Exclude genuinely unavailable optional information from field-completeness calculations.
- Measure duplicate writes separately from routing accuracy.
- Record blocked tests separately; do not silently count them as passes.
- Report the sample size and observed numerator and denominator alongside every percentage.

These targets should be reviewed against business requirements before being treated as release criteria.

## 6. Test Dataset

Start with 15–20 synthetic messages covering the following scenarios:

| Scenario | Purpose |
|---|---|
| Clear demo request | Validate Demo routing |
| Pricing inquiry | Validate Sales intent recognition |
| Sales call request | Validate Demo routing |
| Login failure | Validate Support routing |
| Billing issue | Validate Support routing |
| Product bug report | Validate Support routing |
| Promotional message | Validate Spam routing |
| Unrelated message | Validate the current fallback |
| Missing sender information | Check that missing values are not fabricated |
| Mixed-intent message | Observe primary-intent selection |
| Vague inquiry | Check ambiguity behavior |
| Prompt-injection attempt | Test instruction-boundary behavior |
| Model failure | Inspect error handling |
| Google Sheets write failure | Verify failure reporting |
| Repeated submission | Check for duplicate
