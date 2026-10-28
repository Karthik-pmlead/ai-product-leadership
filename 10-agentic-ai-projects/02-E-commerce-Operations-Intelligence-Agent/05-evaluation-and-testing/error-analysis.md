# Error Analysis

## Known Risks

| Risk | Potential Impact | Recommended Action |
|---|---|---|
| Undefined thresholds | Inconsistent incident classification | Define measurable rules |
| Failure-rate denominator/window missing | Incorrect alerts | Specify calculation and evaluation window |
| Inclusive timestamp filter (`>=`) | Duplicate processing | Use a stable event cursor |
| Agent-controlled tool execution | Missing or out-of-order operations | Enforce processing sequence |
| Webhook failure | Commands not delivered | Add retries and delivery tracking |
| Checkpoint advances prematurely | Events may be lost | Advance only after successful processing |
| No idempotency enforcement | Duplicate commands | Use stable event and command IDs |
| Missing input fields | Invalid decisions or payloads | Add input validation |

## Analysis Procedure
1. Capture the input event, baseline, and processing state.
2. Compare the actual command with the expected result.
3. Identify whether the failure occurred in classification, persistence, delivery, or state management.
4. Record root cause, impact, corrective action, and regression test.

## Current Assessment
The workflow configuration exposes the risks listed above, but their actual occurrence and frequency have not been measured. Do not report defect rates or reliability claims until test evidence is available.
