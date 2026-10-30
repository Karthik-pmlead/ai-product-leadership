# External Data Ingestion

## Objective
Ingest external market intelligence to provide context for NovaCart's internal financial and product performance.

## Workflow

1. Retrieve external market intelligence documents.
2. Extract and process document content.
3. Split content into chunks of 200 characters with 20-character overlap.
4. Generate embeddings using OpenAI Embeddings.
5. Store vectors in Pinecone under the `external` namespace.

## Configuration

| Parameter | Configuration |
|---|---|
| Data source | External market intelligence documents |
| Processing | Independent ingestion workflow |
| Chunk size | 200 characters |
| Chunk overlap | 20 characters |
| Embedding model | OpenAI Embeddings |
| Embedding dimensions | 1,024 |
| Vector database | Pinecone |
| Index | `novacart-updated` |
| Namespace | `external` |

## Expected Outcome

External market intelligence is available for semantic retrieval and comparison with internal business performance.

## Design Consideration

External information is maintained separately from internal data to preserve clear knowledge boundaries during retrieval and analysis.
