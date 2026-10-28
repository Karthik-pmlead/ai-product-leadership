# Webhook Contract

## Purpose
Transmit checkout incident commands from n8n to a downstream receiver.

## Transport
- Method: `POST`
- Content type: `application/json`
- Endpoint: Configured webhook URL

## Payload Fields

| Field | Purpose |
|---|---|
| `command_id` | Command identifier |
| `action` | `ALERT` or `LOG` |
| `severity` | `HIGH` or `LOW` |
| `reason` | Explanation for the decision |
| `checkout_step` | Checkout stage |
| `cart_value` | Cart value |
| `device` | Device type |
| `baseline_rate` | Reference failure rate |
| `timestamp` | Event timestamp |

## Receiver Expectations
The receiver should validate required fields, reject malformed payloads, and return an appropriate HTTP status.

## Reliability Requirements
- Define timeout and retry policies.
- Log response status and delivery failures.
- Use `command_id` for deduplication.
- Support safe retries without repeating downstream actions.

## Validation
Test valid payloads, malformed payloads, receiver errors, timeouts, and duplicate deliveries.

**Status:** The prototype has a configured HTTP POST tool. Receiver behavior, response handling, and reliable delivery require validation.
