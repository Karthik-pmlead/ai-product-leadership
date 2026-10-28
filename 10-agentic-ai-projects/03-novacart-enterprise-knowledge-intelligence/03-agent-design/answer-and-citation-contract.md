# Answer and Citation Contract

## Answer Requirements
- Answer the user's question directly.
- Use retrieved knowledge as the evidence base.
- Match requested metrics and timeframes to the available evidence.
- Abstain when relevant evidence is insufficient.

## Abstention
Return the configured fallback message when the knowledge base does not contain relevant information:

> I'm sorry, I don't have that information in my knowledge base. Please try asking a different question.

## Citation Requirements
Source citations are **not explicitly implemented in the current workflow**.

Future enhancement:
- Identify the source document supporting each answer.
- Provide traceable references where available.
- Avoid presenting unsupported claims as verified facts.

## Evaluation
Test answer correctness, evidence relevance, timeframe matching, and abstention behavior against a curated question set.
