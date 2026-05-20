# Evaluation and Quality

## What to measure
- field-level accuracy.
- exact match rate.
- document-level correctness.
- confidence calibration.
- review rate.
- processing latency.

## Test cases
- clean digital documents.
- scanned documents.
- low-quality images.
- multi-page documents.
- tables and line items.
- missing or partial fields.

## Acceptance criteria
- critical fields must meet the accuracy threshold.
- low-confidence fields must be flagged.
- structured output must be valid.
- human review must be possible.
- latency must be acceptable.

## Evaluation approach
Use field-level metrics, document-level checks, and human review. Structured extraction usually needs more than one metric because some fields matter more than others and document formats can vary widely. [web:261][web:254][web:258]

## Monitoring
Track extraction errors, confidence drift, document quality, and review queue size over time.

## Red-flag signals
- field accuracy drops.
- scan quality worsens.
- too many documents are routed to review.
- schema mismatches increase.
