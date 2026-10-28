# Assumptions and Constraints

## Assumptions
- Relevant internal documents are available in Google Drive.
- Document content is sufficiently accurate and current.
- Users ask questions within the indexed knowledge scope.
- OpenAI, Pinecone, and Cohere services are configured and accessible.

## Constraints
- Answer quality depends on source quality and retrieval relevance.
- Missing or outdated documents can lead to incomplete answers.
- The current workflow relies on unstructured document retrieval.
- Citation-backed answers, anomaly analysis, and email reporting are future enhancements.
- Exported n8n workflows require environment configuration and testing before activation.

## Risks
- Unsupported answers despite retrieval.
- Poor retrieval due to incomplete or outdated content.
- Exposure of credentials or sensitive data if configuration is published improperly.
