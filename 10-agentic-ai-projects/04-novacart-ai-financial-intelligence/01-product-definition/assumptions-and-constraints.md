# Assumptions and Constraints

## Assumptions

- Internal financial and product performance information is available in PDF and DOCX formats.
- External market intelligence documents are available for ingestion.
- Source documents contain sufficient information to support monthly reporting.
- Pinecone is used as the vector database for both knowledge sources.
- The AI Agent has access to separate internal and external retrieval tools.
- Gmail is available for automated report delivery.
- Monthly report generation is driven by a scheduled n8n workflow.

## Constraints

- Analysis is limited to information retrieved from the configured knowledge sources.
- Internal and external information must remain logically separated.
- Missing or unavailable information must not be presented as fact.
- Financial figures and conclusions must be grounded in source evidence.
- Report generation depends on successful ingestion, retrieval, and AI workflow execution.
- Email delivery depends on valid Gmail connectivity and configuration.

## Implementation Configuration

| Parameter | Configuration |
|---|---|
| Vector database | Pinecone |
| Index | `novacart-updated` |
| Internal namespace | `internal` |
| External namespace | `external` |
| Chunk size | 200 characters |
| Chunk overlap | 20 characters |
| Embedding dimensions | 1,024 |
| Document formats | PDF, DOCX |
| Report format | HTML |
| Delivery | Gmail |
| Schedule | Monthly |
