# 03_ai_decisioning/ai-decision-matrix.md

# AI Decision Matrix

## Purpose
Decide whether AI should be used for aspect sentiment analysis, and if so, what approach is best for the business.

## Decision summary
Aspect sentiment analysis should use AI because the task requires understanding unstructured language, identifying multiple aspects in one comment, and assigning sentiment at the aspect level. The best first version is a hybrid approach with business rules, a classifier or LLM, and human review for ambiguous cases. [web:86][web:89][web:52]

## Decision criteria

| Criterion | Why it matters | What “good” looks like |
|---|---|---|
| Business value | The use case should improve a real workflow. | Better prioritization, faster insight, better CX reporting. |
| Data readiness | The model needs usable feedback data. | Enough historical comments and manageable taxonomy. |
| Technical complexity | The approach should be buildable. | Clear extraction of aspect and sentiment. |
| Explainability | Business users need to trust the result. | Outputs are easy to inspect and explain. |
| Operational fit | Teams should be able to use the output. | Dashboard, report, or workflow integration. |
| Risk | Incorrect output should not create harm. | Human review for low-confidence cases. |
| Maintenance | The system should remain sustainable. | Taxonomy and models can be updated over time. |

## Options matrix

| Option | Use when | Strengths | Weaknesses | Decision |
|---|---|---|---|---|
| Manual tagging | Very early discovery stage | Easy to start | Slow, inconsistent, expensive | No |
| Rules only | Aspects are stable and language is predictable | Simple and fast | Poor with ambiguity and varied phrasing | No |
| Classical ML classifier | You have historical labeled examples | Efficient and controllable | Needs training data and labeling | Yes |
| LLM prompting | You need flexible text understanding | Handles variation well | Needs guardrails and eval | Yes |
| Hybrid system | You want business control and flexibility | Best balance for v1 | Slightly more design effort | Yes |

## Recommended decision
Use a hybrid system:
- business taxonomy for aspects.
- rules for obvious cases and normalization.
- ML or LLM for aspect and sentiment detection.
- human review for uncertain or high-value feedback.

## Why this is the right choice
Aspect-based sentiment analysis is a fine-grained problem where different features of the same product can have different sentiment in the same comment. That makes structured decisioning more important than in simple positive/negative classification. [web:89][web:52]

## Build vs buy

| Choice | Best for | Recommendation |
|---|---|---|
| Buy | Quick dashboarding with limited customization | Consider if speed matters most |
| Build | Custom taxonomy and workflow | Best if business wants control |
| Hybrid | Fast start with room to adapt | Best overall for the pilot |

## RAG vs fine-tuning vs prompting

| Approach | Fit for this use case | Notes |
|---|---|---|
| Prompting | Good for first prototype | Fastest to test but needs strong eval. |
| RAG | Not the core solution | Useful only if feedback needs supporting knowledge context. |
| Fine-tuning | Possible later | Useful if you need consistent classification behavior at scale. |

## Final recommendation
Start with prompting or a lightweight classifier plus rules. Move to fine-tuning only after the taxonomy stabilizes and the pilot shows value. Do not use RAG as the core method unless the business needs to ground analysis in reference documents or policy text. [web:84][web:90][web:91]
