# Idempotency and Recovery

## Objective
Prevent duplicate commands and lost checkout events when workflow execution fails or is repeated.

## Current Limitations
- Timestamp-based filtering can reprocess events sharing the checkpoint timestamp.
- Stable event-level idempotency is not enforced.
- Webhook delivery and checkpoint updates are not guaranteed to complete in sequence.
- Partial-failure recovery is not established.

## Recommended Design
1. Assign each checkout event a stable, unique event ID.
2. Derive a stable command ID for each event and action.
3. Check whether a command has already been processed before creating it.
4. Retry transient webhook failures with bounded retries.
5. Track failed events for replay.
6. Advance the checkpoint only after all events in the batch are successfully processed.
7. Record processing status and errors for auditability.

## Acceptance Criteria
- Replaying an event does not create duplicate commands.
- Failed webhook deliveries can be retried.
- Failed events remain recoverable.
- Checkpoints never advance past unprocessed events.

**Status:** Recommendations; not yet guaranteed by the current prototype.
