# Retrieval and Generation

## Objective
Answer user questions using relevant retrieved knowledge rather than unsupported model assumptions.

## Workflow
1. Accept a natural-language question through the n8n chat interface.
2. Retrieve relevant content from Pinecone using query embeddings.
3. Rerank retrieved results using Cohere.
4. Provide the retrieved context to GPT-4o-mini.
5. Return a grounded answer or an abstention message when relevant information is unavailable.

## Guardrails
- Use retrieved information as the basis for answers.
- Abstain when the retrieved evidence is missing or irrelevant.
- Evaluate factual accuracy, retrieval relevance, and abstention behavior.

## Current Limitations
Explicit source citations and structured business-metric analysis are not established in the current workflow. They remain potential enhancements.
