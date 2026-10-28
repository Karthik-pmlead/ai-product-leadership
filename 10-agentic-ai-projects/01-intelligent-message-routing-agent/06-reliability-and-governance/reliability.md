# Reliability

## 1. Current Design

The n8n workflow connects an AI Agent to three Google Sheets append tools:

- `Append to demo request`
- `Append to Support`
- `Append to spam`

The system prompt instructs the agent to use only one tool per message.

## 2. Known Limitations

The exported JSON does not establish:

- Exactly-once execution or duplicate-write prevention.
- Enforced structured-output validation.
- A dedicated review path for ambiguous messages.
- Verified retry and recovery behavior.
- Guaranteed suppression of success messages after failed writes.

**Fallback behavior:** Unmatched messages are routed to Spam. This does not confirm that they are genuine spam.

## 3. Reliability Testing

Verify the following before broader use:

- Model and Google Sheets failures.
- Missing or incorrectly mapped fields.
- Repeated submissions and retries.
- Correct destination selection and column mapping.
- Accurate success and failure responses.

## 4. Future Improvements

Consider implementing:

- Output validation before writing records.
- Idempotency using a stable message identifier.
- Explicit retry and error-handling logic.
- A review path for ambiguous messages.

These are proposed enhancements, not existing capabilities. Update this document only after implementation and testing confirm the controls work as intended.
