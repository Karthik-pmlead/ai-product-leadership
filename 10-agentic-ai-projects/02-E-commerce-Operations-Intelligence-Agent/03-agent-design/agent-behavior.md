# Agent Behavior

## Purpose
Evaluate checkout events, identify potential incidents, and produce actionable commands for downstream systems.

## Inputs
- **Checkout events:** Timestamp, checkout step, cart value, and device.
- **Baseline metrics:** Reference failure rates for comparison.
- **Processing state:** Timestamp checkpoint used to filter events.

## Decision Behavior

| Condition | Severity | Action |
|---|---|---|
| Payment-step event | HIGH | ALERT |
| Significantly high cart value | HIGH | ALERT |
| Failure rate exceeds baseline | HIGH | ALERT |
| Multiple mobile failures | HIGH | ALERT |
| No high-severity condition detected | LOW | LOG |

Thresholds and evaluation windows must be explicitly defined before production use.

## Expected Outputs
For each evaluated event, the agent is instructed to generate a command containing:

- `command_id`
- `action`
- `severity`
- `reason`
- `checkout_step`
- `cart_value`
- `device`
- `baseline_rate`
- `timestamp`

## Tool Responsibilities
The agent is configured to use Google Sheets tools to retrieve baseline metrics, append command records, and update processing state. An HTTP Request tool is configured to POST commands to a webhook.

## Behavioral Constraints
- Use baseline data when evaluating failure rates.
- Provide a reason for each generated command.
- Preserve the required command fields.
- Avoid treating configured tool calls as proof of successful delivery or persistence.

## Known Gaps
- Failure-rate denominators and time windows are undefined.
- “Significantly high” cart value and “multiple” mobile failures lack explicit thresholds.
- One-command-per-event behavior, tool-call ordering, and failure recovery are not guaranteed by the current agent configuration.

**Status:** These behaviors are specified in the agent prompt and workflow configuration; consistent classification and reliable execution require testing.
