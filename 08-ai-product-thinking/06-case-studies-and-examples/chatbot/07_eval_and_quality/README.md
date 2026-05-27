# Evaluation and Quality

## What to measure
- answer correctness.
- groundedness.
- usefulness.
- refusal quality.
- escalation quality.
- latency.

## Test cases
- simple FAQs.
- ambiguous questions.
- unsupported questions.
- policy-sensitive questions.
- retrieval failures.
- contradictory source content.

## Acceptance criteria
- answers must be grounded.
- unsafe prompts must be blocked.
- escalation must work.
- users must find the chatbot useful.
- latency must be acceptable.

## Evaluation approach
Use both automated checks and human review. Automated checks help with scale, while human review is important for safety, helpfulness, and nuanced response quality. Hallucination and groundedness should be tested explicitly because chatbot failures often come from unsupported statements rather than obvious bugs. [web:207][web:210][web:238][web:241]

## Monitoring
Track answer quality, fallback rate, retrieval failures, refusal rate, and user satisfaction over time.

## Red-flag signals
- rising hallucination.
- low groundedness.
- too many escalations.
- repeated unsupported answers.
