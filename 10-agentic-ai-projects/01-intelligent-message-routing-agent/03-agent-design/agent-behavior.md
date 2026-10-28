# Agent Behavior

## 1. Objective

Classify incoming messages and route each to one of three Google Sheets destinations using an AI Agent and an OpenRouter language model.

## 2. Supported Intents

| Intent | Examples | Destination |
|---|---|---|
| Demo/Sales | Demo requests, pricing, sales calls | Demo |
| Support | Bugs, login issues, billing problems, requests for help | Support |
| Spam | Promotional, irrelevant, suspicious, or unmatched messages | Spam |

**Current behavior:** Messages that do not clearly fit Demo/Sales or Support are routed to Spam by the system prompt.

## 3. Information Extraction

Extract fields supported by the selected destination.

- **Demo:** User name, user email, message content, reason for demo.
- **Support:** User name, user email, issue title, issue description, priority, additional information.
- **Spam:** Name, email, message content, reason for spam.

Use only information supported by the message. Do not invent missing details.

## 4. Tool Selection

The AI Agent has access to three Google Sheets tools:

- `Append to demo request`
- `Append to Support`
- `Append to spam`

The agent prompt instructs it to use only one tool per message. Exactly-once execution is not independently enforced by this instruction.

## 5. Response Behavior

After a successful tool execution, the agent should confirm the action taken, such as creating a demo request, creating a support ticket, or marking a message as spam.

It should not claim success when the destination write fails.

## 6. Security and Reliability

The prompt should treat inbound messages as untrusted content and ignore instructions that attempt to override routing rules or reveal credentials.

Additional controls—including structured-output validation, explicit ambiguity review, and duplicate-write prevention—require separate implementation and testing.

## 7. Current Status

The workflow provides a working prototype for LLM-based classification and Google Sheets routing. Accuracy, failure handling, and duplicate prevention must be evaluated before production-readiness claims are made.
