# Assumptions and Constraints

## Assumptions

- Google Sheets provides checkout events, baseline metrics, processing state, and command logging.
- Each checkout event includes a timestamp, checkout step, cart value, and device.
- Payment failures are treated as high severity.
- Baseline metrics and business thresholds are available for evaluating events.
- Downstream systems consume commands through an HTTP POST webhook.

## Constraints

- The prototype uses n8n, Google Sheets, and GPT-4o-mini.
- The current workflow uses a manual trigger.
- Timestamp-based filtering may not prevent duplicates when timestamps match.
- High-value thresholds and mobile-failure aggregation rules require explicit definitions.
- Webhook delivery and state updates require failure handling and verification.
- Production throughput, reliability, and business impact have not yet been established.

## Out of Scope

- Automatic checkout remediation.
- Production incident management and root-cause resolution.
- Claims of quantified revenue savings without measured evidence.
