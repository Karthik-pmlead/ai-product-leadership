# Solution Design

## Core flow
1. Receive incoming sales item.
2. Normalize text and metadata.
3. Predict category, priority, or owner.
4. Apply routing rules.
5. Flag low-confidence items.
6. Send to queue, owner, or review path.

## Design principles
- Keep labels business-readable.
- Make confidence visible.
- Use rules for hard constraints.
- Preserve traceability from input to route.
- Use human review for uncertain items.

## Key components
- intake layer.
- classifier.
- routing rules.
- confidence thresholding.
- review queue.
- output integration.

## Fallback logic
- low confidence: route to review.
- missing context: use generic queue.
- conflicting signals: escalate.
- unsupported item type: send to manual handling.

## Human review
Human review is needed when the item is high value, ambiguous, or outside the known routing taxonomy.

## Why this matters
Sales triage works best when classification and routing are treated as one workflow rather than separate model and process pieces. [web:265][web:270][web:264]
