# Constraints

## Data constraints
- Feedback may be short, noisy, slang-heavy, or multilingual.
- Some comments may mention multiple aspects in one sentence.
- Historical labels may be inconsistent or incomplete.

## Model constraints
- Sentiment must be mapped to a business-defined aspect taxonomy.
- Accuracy may vary by channel, domain, and language.
- The system should handle ambiguity without overclaiming certainty.

## Product constraints
- Users need outputs that are easy to understand and explain.
- Insights must be usable in dashboards, reports, or workflows.
- Latency should be reasonable for batch analysis and near-real-time use cases.

## Business constraints
- The first release should deliver value with limited implementation complexity.
- The system should support clear ROI tracking.
- The solution should fit existing customer experience and analytics workflows.

## Governance constraints
- Sensitive customer data must be protected.
- Review and approval may be needed for customer-facing use.
- The system should avoid misleading sentiment summaries when confidence is low.

## Success boundaries
- Initial scope should be limited to a manageable set of aspects and one or two main channels.
- The first version should prioritize usefulness and reliability over full coverage.
