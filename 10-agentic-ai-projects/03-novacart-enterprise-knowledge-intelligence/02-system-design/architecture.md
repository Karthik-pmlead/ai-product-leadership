# Architecture

## Overview
NovaCart uses a Retrieval-Augmented Generation (RAG) architecture to answer natural-language questions using indexed enterprise documents.

## Components
- **n8n:** Workflow orchestration.
- **Google Drive:** Document source.
- **OpenAI Embeddings:** Convert document chunks and queries into vectors.
- **Pinecone:** Store and retrieve vector embeddings.
- **Cohere Reranking:** Improve retrieval relevance.
- **GPT-4o-mini:** Generate responses from retrieved context.

## Data Flow
Google Drive → Document Ingestion → Embeddings → Pinecone → Query Retrieval → Reranking → LLM Response

## Design Principle
Prioritize relevant source evidence and explicit abstention over generating an answer when sufficient information is unavailable.
