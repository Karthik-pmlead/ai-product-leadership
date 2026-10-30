# Demo Evidence — NovaCart AI Financial Intelligence

## 1. Demo Overview

**Use Case:** Automated Monthly Financial Standing Report

**Objective:** Demonstrate an agentic AI workflow that combines internal financial performance data with external market intelligence to generate and deliver a structured monthly report.

The demonstration covers the complete workflow:

1. Internal and external document ingestion.
2. Document processing and embedding generation.
3. Pinecone vector storage with namespace separation.
4. Multi-source retrieval through an AI Agent.
5. Financial insight synthesis and report generation.
6. Automated HTML report delivery through Gmail.

## 2. Demo Video

**Video:** [Insert demo video link]

The video should demonstrate:

- Internal document ingestion.
- External market intelligence ingestion.
- Pinecone namespace configuration.
- Monthly schedule trigger.
- AI Agent accessing both vector stores.
- Report generation.
- Gmail delivery.

## 3. Screenshots and Implementation Evidence

Add screenshots under `07-demo/screenshots/`.

| Screenshot | Suggested File Name | Evidence |
|---|---|---|
| Overall system architecture | `01-system-architecture.png` | End-to-end workflow design |
| Internal ingestion workflow | `02-internal-ingestion.png` | PDF/DOCX processing |
| External ingestion workflow | `03-external-ingestion.png` | Market intelligence ingestion |
| Monthly report agent | `05-monthly-report-agent.png` | AI Agent and connected retrieval tools |
| Agent execution | `06-agent-execution.png` | Multi-source retrieval and report generation |
| Generated report | `07-html-report.png` | Structured financial report |
| Gmail delivery | `08-gmail-delivery.png` | Automated report delivery |

## 4. Product Approach and Solution

### Stage 1 — Internal Data Ingestion

**Objective:** Make NovaCart's internal financial and product performance information available for retrieval.

Approach:
- Automated document ingestion.
- Type-aware routing for PDF and DOCX.
- Content extraction and chunking.
- OpenAI embedding generation.
- Pinecone storage in the `internal` namespace.

Configuration:
- Chunk size: 200 characters.
- Overlap: 20 characters.
- Embedding dimensions: 1,024.

### Stage 2 — External Market Intelligence Ingestion

**Objective:** Make external market intelligence available independently of internal business information.

Approach:
- Separate ingestion workflow.
- Document processing and embedding generation.
- Pinecone storage in the `external` namespace.
- Consistent chunking configuration.

### Stage 3 — Report Generation and Delivery

**Objective:** Automate the monthly financial reporting process.

Approach:
- Monthly schedule trigger.
- AI Agent connected to two Pinecone retrieval tools.
- Retrieval from internal and external namespaces.
- Context synthesis and insight generation.
- Structured HTML report generation.
- Automated Gmail delivery.

## 5. Report Output

The Monthly Financial Standing Report contains:

1. Executive Summary
2. KPI Dashboard
3. Performance Deep Dive
4. Market Context
5. Drivers & Correlations
6. Risks, Opportunities & Recommendations
7. Sources

**Sample report:** [Insert link to sample-monthly-report.html]

The report is designed to help leadership understand business performance in the context of relevant market developments.

## 6. Business Outcomes

The solution is designed to address the following business needs:

| Business Area | Intended Outcome |
|---|---|
| Reporting efficiency | Reduce manual data gathering and report preparation. |
| Decision support | Combine internal performance with external market context. |
| Reporting consistency | Standardize monthly financial reporting. |
| Information quality | Reduce errors associated with manual cross-referencing. |
| Timeliness | Automate report generation within the monthly reporting cycle. |
| Operational scalability | Reuse modular ingestion and retrieval workflows. |

**Business impact:** The expected outcome is reduced manual reporting effort, more consistent analysis, and timely access to consolidated financial intelligence.

*Quantitative savings, accuracy improvements, and productivity gains have not yet been measured.*

## 7. Technical Learnings

- Multi-source RAG enables analysis across independently maintained knowledge sources.
- Pinecone namespaces provide logical separation between internal and external information.
- Modular ingestion workflows improve maintainability and support independent processing.
- Chunk size and overlap influence retrieval quality, particularly for structured financial information.
- Retrieval quality directly affects the reliability of generated insights.
- Scheduled workflows connect AI analysis with recurring business operations.
- Automated HTML generation and Gmail integration complete the reporting lifecycle.

## 8. Product Management Learnings

- Start with a recurring business problem rather than an AI feature.
- Translate reporting needs into clear functional requirements.
- Design outputs around leadership decisions and consumption.
- Establish source boundaries and evidence standards.
- Treat accuracy and traceability as core product requirements.
- Consider the complete workflow, including delivery, rather than stopping at AI-generated insights.

## 9. Engineering Management Takeaways

- Separate ingestion, retrieval, synthesis, and delivery into modular components.
- Define clear ownership and responsibilities across workflow stages.
- Maintain consistent embedding and chunking configurations.
- Establish clear boundaries between internal and external information.
- Design for operational reliability and maintainability.
- Evaluate the quality of generated reports, not just successful workflow execution.

## 10. Best Practices Applied

| Practice | Implementation |
|---|---|
| Smart ingestion | Type-aware PDF/DOCX processing |
| Workload separation | Independent internal and external ingestion |
| Scoped retrieval | Separate Pinecone namespaces |
| Grounded generation | Agent instructed to use retrieved evidence |
| Source traceability | Source information included in reports |
| Output standardization | Defined monthly report structure |
| Automation | Monthly trigger and Gmail delivery |
| Credential protection | n8n-managed integration credentials |

## 11. Future Improvements

Potential enhancements include:

- Automated retrieval-quality evaluation.
- Claim-level source citations.
- Financial figure validation against source documents.
- Workflow monitoring and failure notifications.
- Retry mechanisms for transient failures.
- Historical monthly report comparison.
- Human review and approval before leadership distribution.

These enhancements are proposed next steps, not confirmed implemented capabilities.

12. Key Takeaways

**Technical takeaways**

- RAG Architecture: Successfully combined internal metrics and external market intelligence to generate contextual financial insights.

- Vector DB Design: Namespace separation enables clear data boundaries and retrieval scope control.

- Workflow Orchestration: Modular, reusable ingestion patterns simplify data processing and workflow maintenance.

- Automation: Established an end-to-end pipeline from data ingestion to AI-generated report delivery.

**Project Takeaway**

The project demonstrates how an agentic AI workflow can transform a recurring manual financial reporting process into a structured, multi-source intelligence and reporting capability.

The key product decision is to separate internal business performance from external market intelligence during ingestion, then bring both together during evidence-grounded analysis.

**The value is not simply generating a report with AI. It is connecting business information, market context, analysis, and automated delivery into one repeatable workflow.**

