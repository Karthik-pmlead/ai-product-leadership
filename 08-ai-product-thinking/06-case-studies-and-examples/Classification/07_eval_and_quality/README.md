# Evaluation and Quality

## What to measure
- classification accuracy.
- routing accuracy.
- top-k accuracy if multiple destinations exist.
- review rate.
- time to route.
- downstream handling speed.

## Test cases
- clear examples.
- ambiguous requests.
- multi-intent items.
- short messages.
- missing metadata.
- business-rule overrides.

## Acceptance criteria
- high-confidence items should route correctly.
- low-confidence items must be flagged.
- the taxonomy must be stable enough for operations.
- routing must improve speed or consistency.

## Evaluation approach
Use labeled examples, business review, and workflow testing. In triage systems, accuracy alone is not enough; the system also needs to route items in a way that helps the business operate better. [web:265][web:270][web:264]

## Monitoring
Track routing accuracy, category drift, review volume, and queue performance over time.

## Red-flag signals
- wrong queue assignment.
- growing review backlog.
- frequent taxonomy exceptions.
- falling confidence.
