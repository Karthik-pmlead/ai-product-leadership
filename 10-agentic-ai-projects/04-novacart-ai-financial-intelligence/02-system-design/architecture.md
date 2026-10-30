# System Architecture

## Overview
The NovaCart AI Financial Intelligence workflow uses a multi-source Retrieval-Augmented Generation (RAG) architecture to generate and deliver monthly financial reports.

The solution consists of three major stages:

1. Internal data ingestion
2. External market intelligence ingestion
3. AI-powered report generation and delivery

## Architecture Flow

```text
       INTERNAL DOCUMENTS             EXTERNAL DOCUMENTS
          PDF / DOCX                  Market Intelligence
               |                             |
               v                             v
      Internal Ingestion             External Ingestion
          Workflow                       Workflow
               |                             |
               v                             v
       OpenAI Embeddings              OpenAI Embeddings
               |                             |
               v                             v
          Pinecone                       Pinecone
       internal namespace             external namespace
               |                             |
               +-------------+---------------+
                             |
                             v
                    Monthly Schedule
                         Trigger
                             |
                             v
                         AI Agent
                             |
                   +---------+---------+
                   |                   |
                   v                   v
             Internal Retrieval   External Retrieval
                   |                   |
                   +---------+---------+
                             |
                             v
                    Insight Synthesis
                             |
                             v
                    HTML Report Output
                             |
                             v
                       Gmail Delivery
```

## Technology Stack

| Layer | Technology |
|---|---|
| Workflow orchestration | n8n |
| AI Agent | n8n AI Agent |
| LLM integration | OpenRouter Chat Model |
| Embeddings | OpenAI Embeddings |
| Vector database | Pinecone |
| Retrieval | Pinecone Vector Store |
| Report generation | HTML |
| Email delivery | Gmail |
| Scheduling | n8n Schedule Trigger |

## Key Design Decisions

- Independent ingestion workflows for internal and external information.
- Separate Pinecone namespaces for knowledge isolation.
- Shared Pinecone index for vector storage.
- Multi-source retrieval during report generation.
- Automated monthly execution and email delivery.
