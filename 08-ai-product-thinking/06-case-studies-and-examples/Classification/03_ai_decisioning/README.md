# AI Decisioning

## Decision
Use classification / triage when the goal is to assign incoming sales items to the right category, priority, or team.

## Why this fits
This use case is a strong AI fit because the input is repetitive, the output classes are defined in advance, and the workflow benefits from consistency and speed.

## Recommended approach
Use a hybrid triage pipeline:
- text classification for category or intent.
- rules for obvious routing constraints.
- confidence thresholds for review.
- human escalation for uncertain or high-value items.

## Why this approach
A hybrid approach works well because sales items often have short text, incomplete context, and business-specific routing rules that should not rely on the model alone. [web:265][web:269][web:270]

## Alternatives

| Option | When it fits | Limitation |
|---|---|---|
| Rules only | Very stable and simple routing. | Hard to scale and brittle on messy text. |
| Pure classifier | Clean taxonomy and enough examples. | May miss business exceptions. |
| Classifier + rules | Most sales triage use cases. | Needs review logic and monitoring. |
| Human-only triage | Very low volume. | Too slow and inconsistent at scale. |

## Build strategy
Start with classification plus rules, then add human review and workflow integration before trying to make the model more complex.

## Decision criteria
The triage approach is the right choice if:
- categories are known in advance.
- routing needs to be fast.
- mistakes are measurable.
- human fallback is possible.

## Recommendation
Proceed with classification / triage only when the routing labels are clear enough to automate safely.
