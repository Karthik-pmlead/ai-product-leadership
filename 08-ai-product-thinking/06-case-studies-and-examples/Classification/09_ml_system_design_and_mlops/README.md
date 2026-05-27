# ML System Design and MLOps

## Runtime design
- intake.
- classification.
- routing rules.
- confidence thresholding.
- review queue.
- workflow integration.

## MLOps needs
- version taxonomy.
- version training data.
- version model and rules.
- monitor routing quality.
- refresh labels and exceptions over time.

## Operational controls
- log inputs and outputs.
- store review corrections.
- track routing history.
- support rollback.
- monitor queue health.

## Monitoring
Track accuracy, latency, review rate, and category drift.

## Refresh strategy
Retrain or refine when routing behavior changes or the business taxonomy shifts.

## Incident response
If routing quality drops, route more items to review, pause automation for risky classes, and investigate the issue.
