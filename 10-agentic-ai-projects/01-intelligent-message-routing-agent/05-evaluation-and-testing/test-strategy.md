# Test Strategy — Intelligent Message Routing Agent

## 1. Objective

Validate message classification, Google Sheets routing, field extraction, and failure handling in the n8n prototype.

## 2. Test Coverage

- **Functional:** Demo/Sales, Support, and Spam routing.
- **Field mapping:** Verify destination-specific columns and original-message preservation.
- **Edge cases:** Missing details, ambiguous messages, and mixed intents.
- **Security:** Test messages containing instructions that attempt to override agent rules.
- **Reliability:** Test model failures, Google Sheets write failures, and repeated submissions.

## 3. Test Environment

- Use a separate n8n test workflow and spreadsheet.
- Use synthetic messages.
- Verify credentials, sheet tabs, and column mappings.
- Check the Demo `User name` mapping for the leading space in the exported configuration.

## 4. Execution

1. Define expected outcomes in `expected-results.csv`.
2. Run each test case individually.
3. Inspect the n8n execution trace and destination sheet.
4. Record actual outcomes in `results-template.csv`.
5. Mark each case `PASS`, `FAIL`, or `BLOCKED`.
6. Investigate failures and rerun affected tests after changes.

## 5. Pass Criteria

A test passes when the observed destination, field values, and execution behavior match expectations.

The current prompt routes unmatched messages to Spam. Record this as current behavior, not proof that the message is spam.

## 6. Reporting

Summarize test counts, routing accuracy, field errors, duplicate writes, and failure-handling issues. Treat evaluation targets as proposed until verified by actual results.
