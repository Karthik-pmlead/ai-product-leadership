# 05_solution_design/model-sel-rationale.md

# Model Selection Rationale

## Purpose
Explain why a specific model approach is being chosen for aspect sentiment analysis.

## Recommendation
Start with a hybrid approach that combines rules, a lightweight classifier or prompting, and human review. If the pilot proves valuable and the taxonomy stabilizes, consider fine-tuning later.

## Evaluation criteria

| Criterion | Why it matters |
|---|---|
| Accuracy | The output must be good enough for business decisions. |
| Explainability | Users need to understand why a label was assigned. |
| Speed | The pilot should be quick to build and test. |
| Flexibility | The system should handle multiple aspects and language variation. |
| Maintainability | The approach should not be hard to update. |

## Option comparison

| Option | Strengths | Weaknesses | Decision |
|---|---|---|---|
| Rules-based | Simple, transparent, easy to control | Weak for ambiguous language | Use for obvious cases |
| Lightweight classifier | Stable, efficient, repeatable | Needs labeled data | Good first model |
| Prompted LLM | Flexible, fast to prototype | Needs guardrails and eval | Good for pilot experimentation |
| Fine-tuned model | Strong consistency at scale | Needs more data and effort | Later-stage option |

## Why this approach
Aspect sentiment analysis is a fine-grained text problem, so a pure rules-only approach is usually too limited. A hybrid setup gives the business a practical balance of speed, control, and quality. [web:56][web:81][web:107]

## Decision
Use the simplest model that can reliably support the pilot use case, then improve only after the taxonomy and data quality are stable.
