# 09_ml_system_design_and_mlops/ml-system-design.md

# ML System Design and MLOps

## Purpose
Define how the aspect sentiment solution will run in production.

## System goals
- reliable processing.
- stable deployment.
- monitoring and alerts.
- retraining or refresh workflow.
- traceable outputs.

## Production flow

| Stage | Description |
|---|---|
| Ingest | Pull feedback from approved sources. |
| Transform | Clean, normalize, and prepare text. |
| Infer | Detect aspects and sentiment. |
| Store | Save outputs and metadata. |
| Monitor | Track quality, volume, and drift. |
| Review | Route low-confidence cases. |
| Refresh | Update taxonomy or models over time. |

## MLOps components

| Component | Purpose |
|---|---|
| Versioning | Track model, prompt, taxonomy, and dataset versions. |
| CI/CD | Release changes safely. |
| Monitoring | Detect quality issues and drift. |
| Logging | Preserve inputs, outputs, and confidence. |
| Retraining workflow | Improve performance as data grows. |
| Rollback plan | Recover from bad releases quickly. |

## Architecture notes
- Keep the inference path simple.
- Separate business taxonomy from model logic.
- Log both aspect and sentiment outputs.
- Keep human review in the loop for uncertain outputs.

## Operational concerns
- latency if used interactively.
- cost of model calls.
- batch vs near-real-time processing.
- scaling to more channels later.

## Deliverable
A production-ready operating design for the pilot and future expansion.
