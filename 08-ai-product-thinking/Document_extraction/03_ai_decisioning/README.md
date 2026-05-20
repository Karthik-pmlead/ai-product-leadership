# AI Decisioning

## Decision
Use document extraction when the goal is to convert unstructured documents into structured business data.

## Why this fits
This use case is a strong AI fit because the input is messy, the outputs are repeatable, and the workflow benefits from automation.

## Recommended approach
Use a hybrid extraction pipeline:
- OCR or text extraction for document reading.
- layout or vision understanding if needed.
- field extraction into a schema.
- validation rules for business constraints.
- human review for low-confidence cases.

## Why this approach
OCR alone is often not enough for enterprise documents because tables, formatting, and non-standard layouts can make extraction harder. A hybrid approach improves reliability by combining visual/text understanding with validation and review. [web:254][web:256][web:257]

## Alternatives

| Option | When it fits | Limitation |
|---|---|---|
| Rules only | Very structured templates. | Breaks when layouts vary. |
| OCR only | Simple documents and text-heavy scans. | Weak on complex structure. |
| OCR + extraction model | Most enterprise document workflows. | Needs quality evaluation and fallback. |
| Full manual processing | Very low volume. | Too slow and expensive. |

## Build strategy
Start with OCR + extraction + validation, then add more advanced layout or vision logic only if the document complexity requires it.

## Decision criteria
The extraction approach is the right choice if:
- documents contain repeated fields.
- output must be structured.
- accuracy is measurable.
- human review is possible for exceptions.

## Recommendation
Proceed with document extraction only when the target document type and output schema are stable enough to automate safely.
