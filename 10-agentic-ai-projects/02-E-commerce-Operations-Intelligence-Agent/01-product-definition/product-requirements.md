# Product Requirements

## Functional Requirements

1. **Event Ingestion:** Read checkout events from Google Sheets.
2. **State Management:** Read the processing checkpoint and filter eligible events.
3. **Severity Evaluation:** Apply business rules for payment failures, high-value carts, baseline breaches, and repeated mobile failures.
4. **Command Generation:** Map HIGH severity to `ALERT` and LOW severity to `LOG`.
5. **Audit Logging:** Append one command per processed event with all nine required fields.
6. **Webhook Handoff:** Send each command as a JSON payload using HTTP POST.
7. **Checkpoint Update:** Advance state after successful processing to minimize duplicate or lost events.

## Non-Functional Requirements

- **Reliability:** Handle sheet-write and webhook failures.
- **Idempotency:** Prevent duplicate commands during retries or repeated runs.
- **Traceability:** Link each decision to its source event.
- **Configurability:** Maintain baseline metrics and decision thresholds externally.
- **Observability:** Track processing outcomes, failures, and webhook delivery.

## Acceptance Criteria

- Representative events receive the expected severity and action.
- Each processed event produces exactly one command.
- Every webhook payload contains all required fields.
- Repeated runs do not duplicate completed events.
- Failed processing does not silently advance the checkpoint.

*Note: These are target requirements; implementation and test evidence must establish compliance.*
