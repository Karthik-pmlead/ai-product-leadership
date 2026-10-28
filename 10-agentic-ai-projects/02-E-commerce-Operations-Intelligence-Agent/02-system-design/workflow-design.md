# Workflow Design

## Workflow Overview

The n8n workflow reads checkout events and processing state from Google Sheets, filters events by timestamp, and passes eligible events to an AI agent for severity evaluation and command generation.

## Workflow Steps

1. **Manual Trigger:** Starts workflow execution.
2. **Get State:** Reads the current processing checkpoint.
3. **Get Cart Events:** Retrieves checkout-event records.
4. **Filter Events:** Filters events using the stored timestamp.
5. **Checkout Agent:** Uses GPT-4o-mini to evaluate events and coordinate tool calls.
6. **Get Baseline Metrics:** Retrieves baseline data from Google Sheets.
7. **Append Command:** Writes decisions to the agent sheet.
8. **Broadcast Webhook:** Sends command data through an HTTP POST request.
9. **Update State:** Updates the stored processing checkpoint.
10. **Return Results:** The agent is instructed to return a JSON array of decisions.

## Integrations

- **Google Sheets:** Event input, baseline metrics, state, and command logging.
- **GPT-4o-mini:** AI-driven evaluation and tool selection.
- **HTTP POST webhook:** Downstream command handoff.

## Reliability Considerations

The agent coordinates writes, webhook calls, and state updates through tools. The current configuration does not enforce their execution order or guarantee one command per event. Timestamp filtering is inclusive, so events matching the checkpoint may be processed again.

Production hardening requires explicit execution control, failure handling, and duplicate prevention.
