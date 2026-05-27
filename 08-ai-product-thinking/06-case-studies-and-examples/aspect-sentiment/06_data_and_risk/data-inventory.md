# 06_data_and_risk/data-inventory.md

# Data Inventory

## Purpose
List the data sources needed for aspect sentiment analysis.

## Data sources

| Source | Use | Notes |
|---|---|---|
| Surveys | Customer feedback input | Often structured with free-text comments. |
| Reviews | Public or internal customer opinion | Useful for product and service themes. |
| Support tickets | Complaint and issue detection | Good for recurring operational pain points. |
| Chat transcripts | Real-time or near-real-time feedback | Often noisy but high value. |
| NPS / CSAT comments | Direct customer sentiment | Good for trend analysis. |

## Fields to capture
- feedback_id
- feedback_text
- source_channel
- timestamp
- product_area
- language
- customer_segment if allowed
- review_status

## Inventory note
Keep only approved and necessary data fields for the pilot.
