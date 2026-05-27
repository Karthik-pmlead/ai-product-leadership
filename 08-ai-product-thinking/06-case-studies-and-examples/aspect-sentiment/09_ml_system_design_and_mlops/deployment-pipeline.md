# 09_ml_system_design_and_mlops/deployment-pipeline.md

# Deployment Pipeline

## Purpose
Define how changes move into production.

## Pipeline
1. code or prompt change.
2. test on sample feedback.
3. validate against acceptance cases.
4. approve release.
5. deploy to pilot environment.
6. monitor results.
7. rollback if needed.

## Principle
Use the simplest safe release process that fits the pilot.
