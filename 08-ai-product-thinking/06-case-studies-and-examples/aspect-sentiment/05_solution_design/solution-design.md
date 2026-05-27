# 05_solution_design/solution-design.md

# Solution Design

## Purpose
Define how aspect sentiment analysis will work from a technical and product perspective.

## Design goal
Convert customer feedback into aspect-level sentiment outputs that are accurate, explainable, and usable in business workflows.

## Proposed architecture

| Layer | Description |
|---|---|
| Input | Customer feedback from surveys, reviews, tickets, or comments. |
| Preprocessing | Clean text, normalize formatting, detect language if needed. |
| Aspect detection | Identify which business aspect is mentioned. |
| Sentiment classification | Assign sentiment to each identified aspect. |
| Post-processing | Map outputs to business taxonomy and confidence levels. |
| Delivery | Send results to dashboard, report, or workflow. |

## Recommended approach
Use a hybrid system with:
- aspect taxonomy.
- rules for obvious cases.
- ML or LLM-based classification for flexible language understanding.
- human review for ambiguous outputs.

## Model choice guidance

| Need | Recommended option | Why |
|---|---|---|
| Fast pilot | Prompting or lightweight classifier | Quick to test and validate. |
| Better consistency | Fine-tuned classifier later | Useful once labels and taxonomy stabilize. |
| Multiple aspects per comment | Structured extraction model | Better for fine-grained ABSA tasks. |
| Explainable outputs | Hybrid system with review | Business users need trust and traceability. |

## Fallback logic

| Condition | Fallback |
|---|---|
| Low confidence | Route to human review. |
| No aspect found | Mark as uncategorized. |
| Multiple conflicting sentiments | Split by aspect and keep both with confidence. |
| Unsupported language | Flag for later handling or manual review. |

## Design principles
- Keep the first version narrow.
- Make outputs easy to interpret.
- Preserve confidence and traceability.
- Design for repeated review and improvement.

## Deliverable
A solution that can support pilot-scale analysis before expansion.
