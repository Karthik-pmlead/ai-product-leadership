# Observability

## Objective
Monitor the NovaCart AI Financial Intelligence workflow to ensure reliable ingestion, retrieval, report generation, and email delivery.

## Monitoring Areas

| Component | What to Monitor |
|---|---|
| Internal ingestion | Document processing and vector storage status |
| External ingestion | Market intelligence ingestion status |
| Embeddings | Embedding generation failures |
| Pinecone | Namespace availability and retrieval results |
| AI Agent | Execution status and report generation |
| Report output | HTML generation and report completeness |
| Gmail | Email delivery status |
| Scheduler | Monthly workflow execution |

## Key Operational Indicators

- Successful and failed workflow executions.
- Number of documents processed.
- Retrieval results from internal and external namespaces.
- Report generation success rate.
- Monthly email delivery status.
- Workflow execution duration.

## Recommended Enhancements

- Centralized workflow execution monitoring.
- Alerts for ingestion and report-generation failures.
- Retrieval quality tracking.
- Historical execution logs.
- Monthly operational performance summary.

*Note: These indicators define a monitoring approach. Centralized monitoring and automated alerts are proposed enhancements, not confirmed implemented capabilities.*
