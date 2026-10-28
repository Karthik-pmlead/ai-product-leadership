# Test Strategy

## Objective
Validate incident classification, command generation, webhook delivery, and processing-state reliability.

## Test Scenarios

| Scenario | Expected Result |
|---|---|
| Payment-step event | `HIGH` / `ALERT` |
| Cart value exceeds configured threshold | `HIGH` / `ALERT` |
| Failure rate exceeds baseline | `HIGH` / `ALERT` |
| Multiple mobile failures | `HIGH` / `ALERT` |
| No incident condition | `LOW` / `LOG` |
| Missing baseline data | No fabricated baseline; behavior documented |
| Webhook failure | Failure detected; checkpoint must not silently advance |
| Repeated event | Duplicate command prevented |
| Multiple events in one batch | Every event processed and accounted for |
| Repeated timestamps | No event silently missed or unnecessarily duplicated |

## Validation Dimensions
- **Classification:** Correct action, severity, and reason.
- **Payload:** All nine required fields are present and valid.
- **Persistence:** Command records are written correctly.
- **Integration:** Webhook receives the expected JSON payload.
- **State management:** Failed or incomplete processing can be recovered.
- **Repeatability:** Identical inputs produce consistent decisions.

## Execution Approach
1. Prepare representative checkout events and baseline values in Google Sheets.
2. Execute the workflow for each scenario.
3. Inspect command records, webhook responses, and state updates.
4. Compare actual results with expected outcomes.
5. Record failures, fixes, and regression results.

## Exit Criteria
Meet the agreed classification and delivery targets, validate duplicate prevention, and demonstrate safe recovery from partial failures.

**Status:** Test scenarios are proposed; passing results and production readiness have not yet been established.
