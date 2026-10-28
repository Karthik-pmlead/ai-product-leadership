# Assumptions and Constraints

## Assumptions
- Incoming messages contain enough context for initial intent classification.
- Demo, Support, and Spam cover the prototype's primary routing categories.
- Google Sheets is sufficient for recording routed messages.
- Synthetic test data can validate expected workflow behavior.

## Constraints
- **Classification:** LLM outputs may be inconsistent or misclassify ambiguous messages.
- **Fallback:** Unmatched messages currently route to Spam, potentially misclassifying legitimate inquiries.
- **Integration:** Routing depends on n8n, OpenRouter, and Google Sheets availability.
- **Reliability:** Duplicate prevention, retries, and failure recovery are not yet verified.
- **Security:** Production-grade privacy controls and prompt-injection defenses are not established by the workflow export.
- **Evaluation:** Accuracy and reliability targets remain unverified until tests are executed.

## Dependencies
- Configured n8n workflow and credentials.
- Access to the OpenRouter model.
- Authorized Google Sheets access and correctly configured destination tabs.

