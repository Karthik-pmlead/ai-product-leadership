# Test Strategy

## Objective
Validate the accuracy, completeness, reliability, and delivery of the NovaCart Monthly Financial Standing Report workflow.

## Testing Scope

| Area | Validation |
|---|---|
| Internal ingestion | PDF and DOCX content is extracted and stored successfully. |
| External ingestion | Market intelligence content is ingested into the external namespace. |
| Chunking and embeddings | Documents use the configured 200-character chunks and 20-character overlap. |
| Namespace separation | Internal and external information is stored in the correct Pinecone namespaces. |
| Retrieval | The agent retrieves relevant information from both sources. |
| Analysis | Findings are supported by retrieved evidence. |
| Report generation | All required report sections are generated in HTML. |
| Email delivery | The generated report is delivered through Gmail. |
| Scheduling | The workflow executes through the monthly schedule trigger. |

## Test Scenarios

1. **Ingestion validation:** Verify successful processing of supported PDF and DOCX documents.
2. **Retrieval validation:** Confirm relevant information is retrieved from both namespaces.
3. **Source validation:** Check whether report findings can be traced to retrieved documents.
4. **Accuracy validation:** Verify financial figures against source documents.
5. **Missing-data validation:** Confirm unavailable information is explicitly identified.
6. **Report validation:** Check completeness, formatting, and readability.
7. **End-to-end validation:** Verify scheduled execution through report delivery.

## Acceptance Criteria

- Both knowledge sources are accessible to the agent.
- Retrieved information is relevant to the reporting period.
- Financial figures are consistent with source documents.
- Unsupported claims are avoided.
- Required report sections are present.
- HTML output is readable.
- Gmail delivery completes successfully.
