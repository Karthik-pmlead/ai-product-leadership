# 05_solution_design/sol-arch.md

# Solution Architecture

## Purpose
Define the end-to-end architecture for aspect sentiment analysis.

## Architecture overview

| Layer | Component | Description |
|---|---|---|
| Input | Feedback sources | Surveys, reviews, support tickets, comments. |
| Ingestion | Data connector | Pull text and metadata from approved sources. |
| Preprocessing | Text normalization | Clean text, detect language, remove noise. |
| Aspect layer | Aspect detector | Identify which business aspect is mentioned. |
| Sentiment layer | Sentiment classifier | Assign polarity to each detected aspect. |
| Post-processing | Business mapping | Map model outputs to business taxonomy. |
| Review | Human review queue | Handle low-confidence or ambiguous cases. |
| Output | Analytics layer | Dashboard, report, or export. |

## Design principles
- Keep the first version narrow.
- Use a small aspect taxonomy.
- Separate aspect detection from sentiment labeling.
- Make confidence and review state visible.
- Preserve traceability from input to output.

## Flow
1. Ingest customer feedback.
2. Normalize and prepare text.
3. Detect aspects.
4. Classify sentiment for each aspect.
5. Apply thresholds and fallback rules.
6. Send results to business users.

## Notes
Aspect-based sentiment analysis is often treated as two core tasks: aspect extraction and sentiment classification. This architecture reflects that split. [web:112][web:56]
