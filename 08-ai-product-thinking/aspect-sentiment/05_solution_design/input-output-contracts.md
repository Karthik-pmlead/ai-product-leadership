# 05_solution_design/input-output-contracts.md

# Input-Output Contracts

## Purpose
Define what the system accepts and what it must produce.

## Input schema

| Field | Type | Description |
|---|---|---|
| feedback_id | string | Unique identifier for the comment or ticket. |
| feedback_text | string | Raw customer feedback text. |
| source_channel | string | Survey, review, ticket, chat, etc. |
| timestamp | datetime | When the feedback was captured. |
| product_area | string | Optional business category. |
| language | string | Optional language code. |

## Output schema

| Field | Type | Description |
|---|---|---|
| feedback_id | string | Same identifier as input. |
| aspect | string | Detected business aspect. |
| sentiment | string | Positive, negative, neutral, or mixed. |
| confidence | number | Confidence score for the result. |
| rationale | string | Short explanation or evidence. |
| review_status | string | Auto, flagged, or human-reviewed. |

## Example input

```json
{
  "feedback_id": "FB-10021",
  "feedback_text": "The product quality is great, but delivery was slow and support was unhelpful.",
  "source_channel": "survey",
  "timestamp": "2026-05-20T12:15:00Z",
  "product_area": "ecommerce",
  "language": "en"
}
```

## Example output

```json
[
  {
    "feedback_id": "FB-10021",
    "aspect": "product quality",
    "sentiment": "positive",
    "confidence": 0.96,
    "rationale": "Customer says quality is great.",
    "review_status": "auto"
  },
  {
    "feedback_id": "FB-10021",
    "aspect": "delivery",
    "sentiment": "negative",
    "confidence": 0.94,
    "rationale": "Customer says delivery was slow.",
    "review_status": "auto"
  },
  {
    "feedback_id": "FB-10021",
    "aspect": "support",
    "sentiment": "negative",
    "confidence": 0.91,
    "rationale": "Customer says support was unhelpful.",
    "review_status": "auto"
  }
]
```

## Contract rules
- One feedback item may produce multiple output records.
- Every output must preserve traceability to the source input.
- Low-confidence outputs must be flagged for review.
- The system should support unknown or uncategorized aspects.

## Validation rules
- Input text cannot be empty.
- Confidence must be between 0 and 1.
- Sentiment values must follow a fixed taxonomy.
- Aspect labels must map to the approved business aspect list.
