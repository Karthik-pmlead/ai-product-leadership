# Observability

## Objective
Make event processing, incident decisions, and integration failures traceable.

## Recommended Signals

| Signal | Purpose |
|---|---|
| Events read and processed | Processing coverage |
| Commands by action and severity | Decision distribution |
| Classification errors | Decision quality |
| Webhook success/failure rate | Delivery reliability |
| Duplicate command count | Idempotency monitoring |
| Processing duration | Workflow performance |
| Checkpoint and replay status | Recovery visibility |

## Logging
Capture the event ID, command ID, decision reason, processing timestamp, webhook outcome, and error details. Avoid logging sensitive data unnecessarily.

## Alerts
Flag repeated workflow failures, elevated webhook errors, stalled checkpoints, and unexpected drops or spikes in command volume.

## Dashboard
Use the collected signals to monitor operational health and evaluate proposed success metrics.

**Status:** Monitoring requirements are proposed; instrumentation and measured baselines are not yet verified.
