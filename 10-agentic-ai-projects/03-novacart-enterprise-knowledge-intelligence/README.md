# NovaCart Enterprise Knowledge Intelligence Platform

**AI Product Management | RAG | Agentic Workflows | Enterprise Knowledge Retrieval**

## 1. Overview

NovaCart is a fictional consumer electronics and subscription business whose leadership needs reliable answers from internal product documentation and operational knowledge.

This project explores how a Retrieval-Augmented Generation (RAG) system can help business users retrieve relevant internal information, answer natural-language questions, and reduce dependence on manual document searches.

The solution is implemented using **n8n, OpenAI, Pinecone, and Cohere reranking**.

## 2. Problem Statement

Business teams often spend time searching across internal knowledge sources to answer routine questions. General-purpose LLMs can also generate plausible but unsupported answers when reliable source material is unavailable.

The product objective is to make enterprise knowledge retrieval more efficient while prioritizing **grounded answers, relevance, and explicit abstention when information is unavailable**.

### Example user questions

- What was the revenue from NovaPhone X1 in Q4?
- How many NovaHome SmartHub Pro units were sold last year?
- What is the churn rate for NovaCart Essentials Subscription?
- What are the specifications of NovaFit Active Watch?

These are illustrative questions; answering them accurately depends on the availability and quality of indexed source documents.

## 3. Product Goals

- Enable natural-language queries over indexed enterprise knowledge.
- Ground answers in retrieved content rather than unsupported model assumptions.
- Improve retrieval relevance through reranking.
- Abstain when relevant information cannot be found.
- Establish a foundation for evaluating answer quality, reliability, and business value.

## 4. Solution Architecture

```text
Internal Documents
        |
        v
n8n Data Ingestion Workflow
        |
        v
Document Loading and Chunking
        |
        v
OpenAI Embeddings
        |
        v
Pinecone Vector Index
        |
        v
User Question
        |
        v
n8n Knowledge Agent
        |
        v
Vector Retrieval + Cohere Reranking
        |
        v
GPT-4o-mini Answer Generation
        |
        v
Grounded Answer or Abstention
```

## 5. Implementation

| Component | Implementation |
|---|---|
| Workflow orchestration | n8n |
| Language model | OpenAI GPT-4o-mini |
| Embeddings | OpenAI `text-embedding-3-large`, configured for 1,024 dimensions |
| Vector database | Pinecone |
| Retrieval enhancement | Cohere reranking |
| Conversation context | n8n memory component |
| Ingestion | Google Drive document search and download |
| Document chunking | Recursive character splitter, 500-character chunks with 50-character overlap |

The exported workflows are currently configured as inactive. Credentials, source access, and environment configuration must be validated before execution.

## 6. Trust and Answer Quality

The knowledge agent is configured to:

- Retrieve information from the vector store for non-greeting queries.
- Use retrieved content as the basis for its answer.
- Return a predefined abstention message when results are missing or irrelevant.
- Avoid presenting unsupported information as established fact.

**Current limitation:** The workflow prompt establishes grounding and abstention behavior, but this alone does not prove factual accuracy. Citation formatting, source-level traceability, and systematic evaluation require further validation.

## 7. Product Success Metrics

The following are proposed evaluation metrics, not measured results.

| Dimension | Metric |
|---|---|
| Answer quality | Answer correctness against a verified test set |
| Grounding | Percentage of factual claims supported by retrieved sources |
| Retrieval | Recall@K and relevance of retrieved chunks |
| Abstention | Accuracy of abstention when evidence is insufficient |
| Efficiency | Median response latency |
| Adoption | Repeat usage by intended business users |

A baseline evaluation dataset should cover factual questions, missing information, ambiguous queries, time-period mismatches, and irrelevant retrieval results.

## 8. Repository Structure

```text
novacart-enterprise-knowledge-intelligence/
├── README.md
├── 01-product-definition/
│   ├── problem-statement.md
│   ├── product-requirements.md
│   ├── success-metrics.md
│   └── assumptions-and-constraints.md
├── 02-system-design/
│   ├── architecture.md
│   ├── ingestion-pipeline.md
│   ├── retrieval-and-generation.md
│   └── security-and-governance.md
├── 03-agent-design/
│   ├── agent-behavior.md
│   ├── system-prompt.md
│   └── answer-and-citation-contract.md
├── 04-implementation/
│   ├── n8n/
│   │   ├── rag-data-ingestion.json
│   │   └── rag-knowledge-agent.json
│   └── configuration.md
├── 05-evaluation-and-testing/
│   ├── test-strategy.md
│   ├── evaluation-dataset.csv
│   └── error-analysis.md
├── 06-reliability-and-governance/
│   ├── observability.md
│   ├── failure-handling.md
│   └── security-and-data-handling.md
└── 07-demo/
    ├── demo-script.md
    ├── demo-evidence.md
    └── screenshots/
```

## 9. Current Scope and Next Steps

**Implemented in the exported workflows**
- Google Drive document retrieval and Pinecone ingestion path.
- Configured embedding generation and document chunking.
- Conversational knowledge agent with vector retrieval.
- Cohere reranking and a defined abstention response.

**Next steps**
1. Validate and activate both workflows in a configured environment.
2. Test document ingestion, retrieval relevance, and answer correctness.
3. Add explicit source citations and traceability to answers.
4. Build a repeatable evaluation dataset and document failure cases.
5. Extend the experience to structured business metrics and anomaly explanations.
6. Add email-based reporting if required by the leadership use case.

## 10. Security and Responsible Publishing

Before making this repository public:

- Remove credential IDs, private resource identifiers, webhook identifiers, and environment-specific configuration.
- Never commit API keys, tokens, private documents, or production data.
- Use synthetic or approved sample documents for demonstrations.
- Store credentials in n8n's credential manager or another approved secret-management system.
- Document access controls and data-retention assumptions.

## 11. Product Leadership Takeaway

This project demonstrates product thinking around enterprise AI beyond simply connecting an LLM to a vector database: defining a user problem, designing a retrieval workflow, setting grounding and abstention expectations, identifying measurable quality metrics, and making implementation gaps explicit.

**Portfolio focus:** Enterprise AI Product Management · RAG Systems · Agentic Workflow Design · AI Quality and Governance · Product Evaluation
