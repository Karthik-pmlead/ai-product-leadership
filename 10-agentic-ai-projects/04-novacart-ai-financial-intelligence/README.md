 
# NovaCart AI Financial Intelligence Platform
## Automated Monthly Financial Standing Report Agent

### 1. Overview

NovaCart AI Financial Intelligence is an agentic AI workflow designed to automate the preparation and delivery of monthly financial performance reports.

The solution combines internal product and sales performance data with external market intelligence to generate a consolidated **Monthly Financial Standing Report** for leadership.

Built using n8n, Pinecone, and an AI Agent, the workflow retrieves information from separate internal and external knowledge sources, synthesizes the findings into an executive-friendly HTML report, and delivers it through Gmail on a monthly schedule.

### 2. Business Problem

The Product Finance team needs to assess NovaCart's financial performance in the context of changing market conditions.

Preparing the monthly report requires analysts to:
- Retrieve and review internal financial and product performance information.
- Research external market trends and industry developments.
- Cross-reference internal results with external market conditions.
- Identify performance drivers, risks, and opportunities.
- Consolidate findings into a leadership-ready report.
- Deliver the report within the monthly reporting cycle.

This manual process creates repetitive effort, requires information to be gathered from multiple sources, and makes consistent monthly reporting more difficult.

### 3. Product Objective

Build an automated financial intelligence workflow that:

1. Ingests internal financial and product performance documents.
2. Ingests external market intelligence independently.
3. Maintains clear separation between internal and external knowledge.
4. Retrieves relevant evidence from both sources.
5. Synthesizes performance insights with market context.
6. Generates a structured Monthly Financial Standing Report.
7. Delivers the report automatically through email on a monthly schedule.

### 4. Solution Architecture

The solution is organized into three stages.

#### Stage 1 — Internal Data Ingestion

- Retrieves internal PDF and DOCX documents.
- Processes documents through the ingestion workflow.
- Splits content into chunks of 200 characters with 20-character overlap.
- Generates embeddings using OpenAI embeddings.
- Stores vectors in Pinecone under the `internal` namespace.

#### Stage 2 — External Market Intelligence Ingestion

- Uses an independent ingestion workflow for external market intelligence.
- Processes and embeds market intelligence documents.
- Stores vectors in Pinecone under the `external` namespace.
- Maintains separation from internal financial information.

#### Stage 3 — Agentic Report Generation and Delivery

- Runs through a monthly schedule trigger.
- Invokes an AI Agent with access to two Pinecone retrieval tools.
- Retrieves relevant evidence from both `internal` and `external` namespaces.
- Synthesizes internal performance with external market context.
- Generates an executive-friendly HTML report.
- Sends the report through Gmail.

### 5. Technology Stack

| Component | Technology |
|---|---|
| Workflow orchestration | n8n |
| AI Agent | n8n AI Agent |
| LLM integration | OpenRouter Chat Model |
| Vector database | Pinecone |
| Embeddings | OpenAI Embeddings |
| Retrieval | Pinecone Vector Store |
| Document formats | PDF, DOCX |
| Report generation | HTML |
| Email delivery | Gmail |
| Scheduling | n8n Schedule Trigger |

### 6. Knowledge Architecture

The solution uses separate Pinecone namespaces to maintain distinct knowledge boundaries.

| Knowledge source | Namespace | Purpose |
|---|---|---|
| Internal documents | `internal` | NovaCart financial and product performance |
| External documents | `external` | Industry trends and market intelligence |

Both namespaces use the same Pinecone index, `novacart-updated`.

This separation allows the agent to retrieve information from each source independently and combine the evidence during report generation.

### 7. Monthly Report Structure

The AI Agent generates an HTML report containing the following sections:

1. **Executive Summary** — Overall financial standing and key findings.
2. **KPI Dashboard** — Relevant financial and product performance indicators.
3. **Performance Deep Dive** — Analysis of internal performance.
4. **Market Context** — Relevant external industry and market developments.
5. **Drivers & Correlations** — Potential relationships between business performance and market conditions.
6. **Risks, Opportunities & Recommendations** — Evidence-based observations and suggested actions.
7. **Sources** — Retrieved information supporting the report.

### 8. AI Agent Design Principles

The agent is instructed to:

- Query both internal and external vector stores.
- Use retrieved evidence rather than unsupported prior knowledge.
- Avoid inventing financial figures or market statistics.
- Identify information that is unavailable in the retrieved sources.
- Avoid presenting unsupported estimates as facts.
- Include source information in the generated report.
- Produce concise, structured, leadership-oriented HTML.

**Core quality principle:** Financial conclusions should be grounded in retrieved evidence, with source information available to support review.

### 9. Business Value

The solution is designed to deliver the following operational benefits:

| Dimension | Expected value |
|---|---|
| Reporting efficiency | Reduces manual information gathering and report preparation |
| Consistency | Standardizes the monthly report structure |
| Decision support | Connects internal performance with external market context |
| Traceability | Retains source information for report review |
| Timeliness | Automates monthly report generation and email delivery |
| Scalability | Supports independent ingestion pipelines and reusable retrieval components |

*These are intended business benefits, not quantified outcomes from a measured production deployment.*

### 10. Product and Technical Learnings

**Product management**
- Translate a recurring business reporting problem into an automated product workflow.
- Define source boundaries and reporting requirements.
- Establish evidence-grounded output as a quality requirement.
- Design for leadership consumption and operational delivery.

**Technical product management**
- Design multi-source RAG workflows.
- Separate internal and external knowledge through vector namespaces.
- Coordinate document ingestion, embeddings, retrieval, and synthesis.
- Integrate scheduled agent execution with email delivery.
- Define quality expectations for generated financial intelligence.

### 11. Future Enhancements

Potential next steps include:

- Automated report-quality evaluation.
- Stronger claim-level source citations.
- Retrieval and generation monitoring.
- Failure notifications and workflow retry mechanisms.
- Historical report comparison and trend analysis.
- Human review and approval before leadership distribution.

These are proposed enhancements and are not represented as implemented capabilities.

### 12. Project Scope

This case study demonstrates an agentic AI workflow that connects document ingestion, multi-source retrieval, financial analysis, report generation, and automated delivery.

It focuses on the product and system design decisions required to turn a recurring manual reporting process into a structured, repeatable AI-enabled workflow.

---

**Project:** NovaCart AI Financial Intelligence  
**Use case:** Monthly Financial Standing Report  
**Architecture:** Multi-source RAG with an AI Agent  
**Orchestration:** n8n  
**Delivery:** Scheduled HTML report through Gmail
