# Error Analysis

## Objective
Identify failure patterns and prioritize improvements to answer reliability.

## Error Categories

| Error | Potential Cause | Follow-up |
|---|---|---|
| Incorrect answer | Unsupported generation | Review retrieved evidence and prompt |
| Missing answer | Document absent or retrieval failure | Check ingestion and index coverage |
| Irrelevant answer | Poor retrieval relevance | Review chunking and reranking |
| Wrong timeframe | Evidence does not match requested period | Strengthen metric and timeframe validation |
| Unsupported claim | Insufficient grounding | Add source validation and citation support |
| Incorrect abstention | Weak relevance judgment | Test and refine abstention behavior |

## Review Process
1. Capture the question, retrieved evidence, and generated response.
2. Compare the response with verified source information.
3. Classify the failure and identify its root cause.
4. Prioritize fixes by impact and recurrence.
5. Re-run affected test cases.
