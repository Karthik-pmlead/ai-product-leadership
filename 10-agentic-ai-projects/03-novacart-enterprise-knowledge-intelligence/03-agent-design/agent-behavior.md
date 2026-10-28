# Agent Behavior

## Objective
Answer NovaCart business questions using relevant information retrieved from the enterprise knowledge base.

## Behavior
- Accept natural-language questions through the chat interface.
- Retrieve knowledge for non-greeting queries.
- Use retrieved content to formulate answers.
- Abstain when retrieved information is missing or irrelevant.
- Keep responses concise and relevant.

## Guardrails
- Do not invent facts or unsupported metrics.
- Do not answer beyond the available evidence.
- Use the configured abstention message when sufficient evidence is unavailable.

## Current Scope
The agent supports conversational knowledge retrieval. Automated anomaly analysis and email reporting are future enhancements.
