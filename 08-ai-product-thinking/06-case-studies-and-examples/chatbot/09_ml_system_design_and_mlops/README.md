# ML System Design and MLOps

## Runtime design
- input handling.
- retrieval or tool calling.
- generation.
- guardrails.
- logging.
- monitoring.

## MLOps needs
- version prompts and policies.
- version knowledge sources.
- monitor failures and drift.
- refresh content regularly.
- support rollback.

## Operational controls
- store prompt versions.
- store retrieval index versions.
- store model version.
- record response traces.
- capture escalation events.

## Monitoring
Track latency, retrieval quality, refusal behavior, groundedness, and hallucination trends. Production governance for AI systems also depends on traceability, access control, validation, and model history, so those controls should be built into the system rather than added later. [web:240][web:117][web:115]

## Retraining or refresh
For many chatbots, refreshing knowledge is more important than retraining the model. Update sources first, then adjust prompts or fine-tune only if behavior still needs improvement.

## Incident response
If the chatbot starts producing unsafe or unsupported answers, disable the risky path, fall back to safe behavior, and notify owners.
