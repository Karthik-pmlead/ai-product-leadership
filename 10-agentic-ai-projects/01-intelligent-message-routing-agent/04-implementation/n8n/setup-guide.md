# Setup Guide — Intelligent Message Routing Agent

## 1. Overview

This guide explains how to import, configure, and test the n8n workflow for LLM-powered message classification and routing.

**Workflow status:** Prototype. Validate routing behavior, error handling, and duplicate-write scenarios before relying on it operationally.

## 2. Prerequisites

- An n8n instance.
- Access to an OpenRouter account and a supported chat model.
- A Google account with permission to create and edit Google Sheets.
- Access to the workflow's required credentials.

## 3. Import the Workflow

1. Open n8n.
2. Import the exported workflow JSON.
3. Review the nodes and connections.
4. Confirm that the workflow contains:
   - `When chat message received`
   - `AI Agent`
   - `OpenRouter Chat Model`
   - `Append to demo request`
   - `Append to Support`
   - `Append to spam`

5. Save the workflow.

The exported workflow is inactive by default. Test it before activating it.

## 4. Configure the Language Model

1. Open the OpenRouter Chat Model node.
2. Configure your OpenRouter credentials in n8n.
3. Verify the selected model is available to your account.
4. Confirm that the model node is connected to the AI Agent.
5. Run a test message and inspect the execution output.

The exported configuration specifies `openai/gpt-4o-mini`. Change this only if you intend to use a different supported model.

## 5. Configure Google Sheets

Connect your Google Sheets credentials and verify that the configured spreadsheet and sheet tabs are accessible.

Create or verify these tabs and column headers:

### Demo tab

- User name
- User email
- Message content
- Reason for Demo

**Mapping check:** The exported workflow contains a leading space in the mapped field name `" User name"`. Verify whether this is intentional and normalize it if necessary so the mapping matches the actual sheet header.

### Support tab

- User name
- User email
- Issue title
- Issue description
- Priority
- Additional Information

### Spam tab

- Name
- Email
- Message content
- Reason for spam

Check the field mappings in each append node. The spreadsheet column names and node mappings must match.

## 6. Verify Routing

Test the workflow with representative messages.

| Test message | Expected destination |
|---|---|
| “I'd like to schedule a product demo.” | Demo |
| “Can you share your pricing?” | Demo |
| “I cannot log in to my account.” | Support |
| “The billing page returns an error.” | Support |
| “Buy followers now — limited-time promotion!” | Spam |
| An unrelated message that fits neither Demo nor Support | Spam under the current prompt |

The final case is a fallback behavior, not proof that the message is genuinely spam.

For each test, verify the selected tool, destination row, extracted values, and final response.

## 7. Test Failure Scenarios

Before operational use, test:

- Missing names or email addresses.
- Messages containing multiple intents.
- Ambiguous or irrelevant messages.
- Attempts to override the agent's instructions.
- Invalid or unavailable model credentials.
- Google Sheets permission or write failures.
- Repeated messages and workflow retries.

Do not assume duplicate-write prevention, schema validation, or robust retry handling exists unless those controls have been implemented and verified.

## 8. Security Checklist

Before publishing the workflow JSON to GitHub:

- Remove tokens, secrets, and personal information.
- Review spreadsheet IDs, URLs, credential references, and other environment-specific identifiers.
- Replace sensitive configuration values with placeholders where appropriate.
- Keep credentials in n8n's credential store rather than embedding secrets in prompts or code.
- Avoid publishing real customer messages or private spreadsheet data.

## 9. Activation

Activate the workflow only after:

- Model and Google Sheets credentials are verified.
- All three destination mappings have been tested.
- Routing behavior has been checked against a labeled test set.
- Failure behavior and repeated execution have been investigated.
- Sensitive configuration has been reviewed.

## 10. Troubleshooting

| Symptom | What to check |
|---|---|
| Model call fails | Credentials, model availability, and node configuration |
| No row appears | Google Sheets permissions, spreadsheet selection, tab name, and field mappings |
| Incorrect destination | System prompt, ambiguous intent, and test examples |
| Missing field values | Input content and destination-specific mappings |
| Duplicate rows | Repeated executions, retries, and lack of idempotency controls |
| False success response | Tool execution result and agent response behavior |

## 11. Known Limitations

The current workflow relies on prompt-based classification and tool selection. The exported JSON does not establish that it includes:

- Enforced structured-output validation.
- A separate human-review path for ambiguous messages.
- Exactly-once execution or idempotency protection.
- A fully tested retry and recovery strategy.
- Measured production-level classification accuracy.

These are potential future improvements, not capabilities to claim as implemented.

## 12. Next Step

Create a labeled test set of 15–20 messages covering Demo, Support, Spam, missing information, ambiguity, and failure scenarios. Record the expected destination and compare it with the observed workflow result before reporting evaluation metrics.
