# eval-plan.md

# Evaluation Plan

## Purpose
Define how we will know whether aspect sentiment analysis is working well enough for business use.

## Evaluation goals
- Detect the correct aspect.
- Classify sentiment correctly for that aspect.
- Produce outputs that are useful and explainable.
- Ensure the system works across feedback sources.

## Evaluation dimensions

| Dimension | What to measure |
|---|---|
| Aspect detection | Whether the system identifies the right business aspect. |
| Sentiment quality | Whether the polarity is correct for each aspect. |
| Coverage | How many comments the system can process. |
| Confidence calibration | Whether low-confidence outputs are appropriately flagged. |
| Business usefulness | Whether users can act on the results. |

## Test set design
Include:
- positive, negative, and mixed comments.
- comments with multiple aspects.
- short, noisy, and ambiguous comments.
- common business terms and slang.
- examples from each target channel.

## Acceptance criteria

| Area | Example criterion |
|---|---|
| Aspect coverage | Majority of comments mapped to at least one aspect. |
| Quality | Outputs are reliable enough for trend analysis. |
| Reviewability | Low-confidence cases are visible and routable. |
| Usability | Business users can understand the result. |

## Human review
Use human review for:
- ambiguous comments.
- conflicting aspect signals.
- low-confidence predictions.
- high-value or high-risk feedback.

## Monitoring after launch
- drift in aspect distribution.
- drop in confidence or quality.
- changes in feedback volume.
- adoption by business teams.

## Deliverable
A measurable quality gate for pilot approval and ongoing monitoring.
