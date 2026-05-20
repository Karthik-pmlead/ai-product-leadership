# 09_ml_system_design_and_mlops/retraining-workflow.md

# Retraining Workflow

## Purpose
Improve the system over time.

## Workflow
1. collect corrected labels.
2. review recurring mistakes.
3. update taxonomy or prompts.
4. retrain or refine model.
5. re-evaluate on test set.
6. release only if improvement is clear.

## Note
Aspect drift should trigger a taxonomy review, not just a model update.
