# Product Requirements

## Objective
Automate the generation and delivery of NovaCart's Monthly Financial Standing Report using multi-source retrieval and AI-powered analysis.

## Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | Ingest internal PDF and DOCX documents. |
| FR-02 | Ingest external market intelligence documents through a separate workflow. |
| FR-03 | Store internal and external information in separate Pinecone namespaces. |
| FR-04 | Retrieve relevant information from both knowledge sources. |
| FR-05 | Generate a structured report combining financial performance and market context. |
| FR-06 | Include executive summary, KPIs, performance analysis, market context, risks, opportunities, and recommendations. |
| FR-07 | Include source information supporting report findings. |
| FR-08 | Generate the report in HTML format. |
| FR-09 | Trigger report generation monthly and deliver it through Gmail. |

## Non-Functional Requirements

- **Accuracy:** Avoid unsupported financial figures and conclusions.
- **Traceability:** Include source information for review.
- **Consistency:** Follow a standardized report structure.
- **Maintainability:** Keep ingestion and report-generation workflows modular.
- **Security:** Protect source documents and workflow credentials.
