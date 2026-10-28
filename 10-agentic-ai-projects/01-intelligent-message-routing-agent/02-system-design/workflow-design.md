# Workflow Design

## 1. Objective

Classify inbound messages and append the extracted information to the appropriate Google Sheets destination.

## 2. Workflow Steps

1. **Receive:** The n8n Chat Trigger receives the message.
2. **Interpret:** The AI Agent passes the message to the connected OpenRouter model.
3. **Classify:** The agent determines whether the message concerns Demo/Sales, Support, or Spam.
4. **Select tool:** The agent chooses the corresponding Google Sheets tool.
5. **Write record:** The selected tool appends destination-specific fields.
6. **Respond:** The agent returns a short confirmation of the action.

## 3. Routing Configuration

| Intent | Tool | Destination fields |
|---|---|---|
| Demo/Sales | `Append to demo request` | User name, user email, message content, reason for demo |
| Support | `Append to Support` | User name, user email, issue title, issue description, priority, additional information |
| Spam or unmatched | `Append to spam` | Name, email, message content, reason for spam |

The current workflow uses the Spam category as its fallback for messages that do not clearly fit the other two categories.

## 4. Execution Rules

- Select one intended destination tool.
- Preserve the original message content.
- Extract only supported information.
- Leave unavailable fields empty rather than inventing values.
- Confirm successful writes only when execution evidence supports the confirmation.

## 5. Failure and Edge Cases

| Scenario | Required verification |
|---|---|
| Missing sender details | Confirm empty fields are handled correctly |
| Mixed-intent message | Check whether the selected destination matches the primary need |
| Unmatched message | Verify the current Spam fallback |
| Model failure | Inspect how n8n surfaces the error |
| Google Sheets write failure | Verify the execution does not falsely report success |
| Repeated execution | Test whether duplicate records can occur |

## 6. Future Improvements

- Add structured-output parsing and validation.
- Introduce a review path for ambiguous messages.
- Implement duplicate-write protection using a stable message identifier.
- Define explicit retry and error-handling behavior.
- Evaluate routing accuracy using labeled test cases.

## 7. Implementation Status

The trigger, AI Agent, model connection, three destination tools, and field mappings are present in the exported workflow. The additional reliability controls listed above should be marked complete only after implementation and testing.
