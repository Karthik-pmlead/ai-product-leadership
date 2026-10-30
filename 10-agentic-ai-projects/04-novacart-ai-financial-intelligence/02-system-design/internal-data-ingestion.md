# Internal Data Ingestion

## Objective
Ingest NovaCart's internal financial and product performance documents into Pinecone for retrieval during monthly report generation.

## Workflow

1. Retrieve internal documents from the configured source.
2. Identify document types.
3. Route PDF and DOCX files through the appropriate processing paths.
4. Extract document content.
5. Split content into chunks of 200 characters with 20-character overlap.
6. Generate embeddings using OpenAI Embeddings.
7. Store vectors in Pinecone under the `internal` namespace.

## Configuration

| Parameter | Configuration |
|---|---|
| Document formats | PDF, DOCX |
| Processing | Type-aware routing |
| Chunk size | 200 characters |
| Chunk overlap | 20 characters |
| Embedding model | OpenAI Embeddings |
| Embedding dimensions | 1,024 |
| Vector database | Pinecone |
| Index | `novacart-updated` |
| Namespace | `internal` |

## Expected Outcome

Internal financial and product performance information is available for semantic retrieval by the Monthly Report Agent.
