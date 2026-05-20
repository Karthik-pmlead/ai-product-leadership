# Data and Risk

## Data sources
- invoices.
- contracts.
- forms.
- receipts.
- claims.
- emails.
- reports.

## Data needs
- sample documents.
- ground-truth field labels.
- target schema definitions.
- document metadata.
- review outcomes.

## Key risks
- OCR errors.
- poor scan quality.
- layout variation.
- missing or inconsistent fields.
- privacy leakage.
- overconfidence in extracted values.

## Mitigations
- use high-quality sample documents.
- define the schema clearly.
- validate outputs with rules.
- keep human review for low confidence.
- protect sensitive fields.
- monitor field-level errors.

## Risk posture
The first release should focus on one document type with a stable field schema.
