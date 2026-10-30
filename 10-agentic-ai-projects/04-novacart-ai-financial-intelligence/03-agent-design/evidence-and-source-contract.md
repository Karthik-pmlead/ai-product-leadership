# Evidence and Source Contract

## Objective
Define the evidence standards the Monthly Financial Report Agent must follow when generating financial insights and recommendations.

## Source Requirements

The agent uses two knowledge sources:

| Source | Namespace | Purpose |
|---|---|---|
| Internal Vector Store | `internal` | Financial and product performance |
| External Vector Store | `external` | Market and industry intelligence |

## Evidence Rules

1. Query both internal and external knowledge sources.
2. Base factual findings on retrieved information.
3. Do not invent financial figures, market statistics, or business trends.
4. Identify unavailable information explicitly.
5. Do not present assumptions or estimates as verified facts.
6. Include source information to support report findings.
7. Distinguish internal performance evidence from external market context.

## Insight and Recommendation Rules

- Explain observed performance trends using available evidence.
- Identify potential drivers only when supported by relevant information.
- Distinguish correlation from proven causation.
- Connect recommendations to identified risks, opportunities, or performance gaps.
- Avoid recommendations based on unsupported assumptions.

## Source Traceability

Each reported finding should be traceable to its underlying retrieved information.

Where available, include:
- Source document name
- Source category (internal or external)
- Relevant supporting information

## Quality Standard

A report is considered evidence-grounded when:
- Both knowledge sources have been queried.
- Financial figures are supported by retrieved information.
- Market observations are supported by external sources.
- Key findings include source information.
- Missing information is clearly identified.
- Recommendations do not exceed what the evidence supports.

**Core principle: No unsupported claims.**
