# Test Strategy

## Objective
Validate answer correctness, retrieval relevance, and safe abstention before production use.

## Test Scenarios
1. **Factual queries:** Answer using relevant indexed documents.
2. **Missing information:** Abstain when evidence is unavailable.
3. **Irrelevant retrieval:** Avoid answering from unrelated content.
4. **Metric and timeframe mismatch:** Abstain when evidence does not support the requested metric or period.
5. **Ambiguous queries:** Assess whether available evidence supports a reliable answer.
6. **Grounding:** Verify that generated claims are supported by retrieved content.

## Evaluation Method
- Create a curated question set with verified expected answers.
- Compare agent responses against source documents.
- Record failures and classify their root causes.
- Re-test after changes to ingestion, retrieval, or prompts.

## Success Criteria
Establish baselines for answer correctness, retrieval relevance, abstention accuracy, and response latency before setting targets.
