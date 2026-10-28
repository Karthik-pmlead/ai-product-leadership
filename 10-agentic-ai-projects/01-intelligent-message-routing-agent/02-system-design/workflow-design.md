# Workflow Design

## 1. Objective

Automate the classification and routing of inbound messages using an LLM-powered agent orchestrated through n8n.

## 2. Workflow

1. **Receive:** Capture an inbound message through the n8n chat trigger.
2. **Interpret:** The AI Agent uses an OpenRouter language model to identify intent and extract relevant details.
3. **Classify:** Assign one category: Demo/Sales, Support, or Spam.
4. **Route:** Append the message to the corresponding Google Sheets destination.
5. **Verify:** Inspect the execution and confirm the expected record was created.

## 3. System Components

| Component | Responsibility |
|---|---|
| n8n Chat Trigger | Receives inbound messages |
| AI Agent | Interprets intent and determines the appropriate action |
| OpenRouter LLM | Provides language understanding |
| Google Sheets tools | Store routed messages |
| n8n execution logs | Support debugging and workflow inspection |

## 4. Data Contract

Each routed record should contain:

- Message ID
- Name and email, when available
- Classified intent
- Message summary
- Priority, where applicable
- Received timestamp

Missing information should remain empty or be explicitly marked as unavailable, rather than invented.

## 5. Routing Rules

| Intent | Destination |
|---|---|
| Demo/Sales | Sales sheet |
| Support | Support sheet |
| Spam | Spam sheet |

Each message should produce exactly one intended destination write. Ambiguous messages should follow a defined fallback policy rather than being routed arbitrarily.

## 6. Design Considerations

- Validate classification and required fields before writing.
- Prevent duplicate writes when an execution is retried.
- Handle model errors and Google Sheets failures.
- Avoid including credentials or unnecessary personal data in logs.

**Implementation note:** The current prototype uses an AI Agent with Google Sheets tools. Validation, fallback behavior, and duplicate-write protection must be tested before they can be considered enforced guarantees.
