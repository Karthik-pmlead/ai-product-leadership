# Error Analysis — Intelligent Message Routing Agent

## 1. Purpose

Identify routing, extraction, and execution failures during testing and document corrective actions.

## 2. Error Categories

| Error | Example | Corrective action |
|---|---|---|
| Misclassification | Demo request routed to Support | Refine routing instructions and test examples |
| Ambiguous fallback | Unmatched message routed to Spam | Consider clarification or human review |
| Extraction error | Incorrect issue title or missing known details | Improve extraction instructions |
| Field-mapping error | Data written to the wrong column | Verify Google Sheets mappings |
| Fabricated information | Agent invents a user's name | Strengthen no-invention rules |
| Tool failure | Google Sheets append fails | Verify credentials and error handling |
| False success | Agent confirms a failed write | Confirm success only after a successful write |
| Duplicate write | Repeated submission creates duplicate rows | Consider idempotency controls |
| Prompt injection | Message overrides routing instructions | Strengthen safeguards and retest |

These corrective actions are recommendations, not claims that the controls are implemented.

## 3. Investigation Process

1. Record the test case ID and input.
2. Inspect the n8n execution trace and selected tool.
3. Compare expected results with the actual destination and row.
4. Identify the error category and evidence-supported root cause.
5. Apply a targeted correction and rerun the affected tests.
6. Record the retest outcome and remaining limitations.

## 4. Error Log

For each failure, capture:
- Test case ID
- Expected and actual outcomes
- Error category
- Root cause
- Corrective action
- Retest result
- Status: Open or Resolved

## 5. Reporting

Summarize failures by category, resolved issues, and outstanding risks. Report metrics only from executed tests.

**Important:** The current workflow routes unmatched messages to Spam and does not independently guarantee exactly-once execution. Track these as design limitations until improved and verified.
