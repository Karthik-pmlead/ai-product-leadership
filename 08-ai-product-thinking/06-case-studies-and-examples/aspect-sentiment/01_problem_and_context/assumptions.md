# Assumptions

## Product assumptions
- Customer feedback contains enough signal to identify meaningful aspects.
- The same aspect can appear in many forms, such as "delivery", "shipping", or "arrival time".
- A limited set of core aspects will cover most of the business need.

## Data assumptions
- Historical feedback is available in sufficient volume for initial development.
- Some feedback examples already contain labels, tags, or issue categories.
- Feedback sources can be centralized into one analysis pipeline.

## AI assumptions
- Aspect-level sentiment can be modeled with acceptable accuracy for business use.
- A hybrid approach may work best, combining taxonomy rules with ML or LLM-based classification.
- Not every comment needs perfect interpretation; business value can still come from trend-level accuracy.

## Operating assumptions
- Users will trust the output if examples and explanations are shown.
- Teams will act on insights if they are tied to business metrics.
- Human review will be needed for ambiguous or high-stakes cases.

## Scope assumptions
- The first version will focus on a narrow set of aspects such as quality, price, delivery, usability, and support.
- The initial goal is insight generation, not fully automated decision-making.
