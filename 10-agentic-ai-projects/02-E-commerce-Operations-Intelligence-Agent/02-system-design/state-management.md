# Decision Logic

## Severity Rules

The agent prompt defines these conditions:

| Condition | Severity | Command |
|---|---|---|
| Payment-step failure | HIGH | `ALERT` |
| Significantly high cart value | HIGH | `ALERT` |
| Failure rate exceeds baseline | HIGH | `ALERT` |
| Multiple mobile failures | HIGH | `ALERT` |
| Low-value, isolated event with no high-severity condition | LOW | `LOG` |

## Evaluation Inputs

- Checkout step
- Cart value
- Device
- Event timestamp
- Baseline rate for the checkout step
- Other available checkout events

## Command Output

Each decision should contain:

`command_id`, `action`, `severity`, `reason`, `checkout_step`, `cart_value`, `device`, `baseline_rate`, `timestamp`

The command is appended to the agent sheet and sent through the configured HTTP POST webhook.

## Rules Requiring Explicit Definitions

- **High cart value:** Define a numeric threshold.
- **Failure rate:** Specify the numerator, denominator, and observation window. Counting failure rows alone does not establish a true failure rate.
- **Multiple mobile failures:** Define the event count and time window.
- **Command ID:** Use a stable, unique event identifier or deterministic idempotency key to support duplicate prevention.

## Decision Principle

Use explicit, testable business rules to distinguish critical incidents from routine events. Validate decisions against expected outcomes before relying on them for operational escalation.
