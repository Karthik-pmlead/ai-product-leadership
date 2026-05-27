# ML System Design and MLOps

## Runtime design
- document ingestion.
- OCR or image understanding.
- field extraction.
- validation.
- review queue.
- export.

## MLOps needs
- version document sets.
- version schemas.
- version models and prompts if used.
- monitor accuracy and drift.
- refresh when layouts or document types change.

## Operational controls
- log input document references.
- store extracted fields and confidence.
- preserve human corrections.
- track schema versions.
- support rollback.

## Monitoring
Track field accuracy, OCR failures, document quality, review rate, and latency.

## Refresh strategy
Document extraction systems often need updates when layouts change, so schema and content refresh can matter as much as model updates.

## Incident response
If extraction quality drops, route more documents to review, pause automation on risky document types, and investigate the source of the failure.
