# fine-tune-vs-rag-vs-prompt.md

# Fine-tune vs RAG vs Prompting

## Purpose
Choose the most suitable AI approach for aspect sentiment analysis.

## Options

| Approach | Best for | Fit here | Recommendation |
|---|---|---|---|
| Prompting | Fast prototyping and flexible extraction | High | Yes for v1 |
| RAG | Grounding answers in reference content | Low to medium | Only if policy or knowledge context is required |
| Fine-tuning | Stable task behavior at scale | Medium to high | Later, after taxonomy stabilizes |

## Guidance
- Use prompting first when you want speed and flexibility.
- Use fine-tuning when you have enough labeled examples and need consistent classification behavior.
- Use RAG only if the analysis must incorporate supporting documents, definitions, or policy material.

## Recommendation
For the first version, use prompting or a lightweight classifier before considering fine-tuning. Keep RAG out of the core path unless the business needs grounded explanations from internal documents.
