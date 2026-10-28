# Ingestion Pipeline

## Objective
Convert internal documents into searchable knowledge for retrieval.

## Workflow
1. Search for documents in the configured Google Drive folder.
2. Download documents for processing.
3. Split content into chunks using a recursive character splitter.
4. Generate embeddings using OpenAI `text-embedding-3-large` configured for 1,024 dimensions.
5. Store embeddings in Pinecone for retrieval.

## Configuration
- Chunk size: 500 characters
- Chunk overlap: 50 characters
- Vector store: Pinecone

## Key Considerations
- Document quality and freshness directly affect answer quality.
- Chunking must preserve enough context for accurate retrieval.
- Ingestion failures and duplicate processing should be tested before production use.
