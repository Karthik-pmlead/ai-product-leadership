# AI Decisioning

## Decision
Use a chatbot if the user need is conversational, repetitive, and bounded to a domain or workflow.

## Why this fits
A chatbot works well when users want quick answers, guided help, or task completion without needing to browse a large knowledge base manually.

## Recommended approach
Use a hybrid chatbot approach:
- prompting for response structure and tone.
- retrieval for grounded answers.
- rules for policy and safety.
- escalation when the system is uncertain.

## Why this approach
This balances usefulness, safety, and maintainability. Retrieval helps ground answers in approved content, while rules and escalation reduce the risk of unsafe or unsupported responses. [web:218][web:220][web:223]

## Alternatives

| Option | When it fits | Limitation |
|---|---|---|
| Rules only | Very narrow flows with limited variation. | Too rigid and hard to scale. |
| Pure LLM | Fast prototype with no strong accuracy requirement. | Risk of hallucination and weak control. |
| Prompting + retrieval | Most enterprise chatbot use cases. | Needs good source content and evaluation. |
| Fine-tuning | When you need consistent style or behavior. | Not ideal if the main need is factual knowledge. |

## Build strategy
Follow this order:
1. prompt the model first.
2. add retrieval if factual grounding is needed.
3. add guardrails and escalation.
4. fine-tune only if the chatbot needs more consistent behavior than prompting can provide.

## Decision criteria
The chatbot approach is the right choice if:
- the domain is bounded.
- the knowledge base is available.
- correctness matters.
- fallback or human escalation is possible.

## Recommendation
Proceed with a chatbot only when the business problem is narrow enough to control and the system can safely say “I don’t know” when needed.
