# 03_ai_decisioning/ai-decision-matrix.md

# AI Decisioning

## Decision question

Should we use AI for aspect sentiment analysis, and if so, what is the right approach?

## Decision summary

Yes, AI is appropriate because the task involves unstructured text, repeated patterns, and a need to classify multiple aspects within the same comment. Sentiment analysis is widely used for customer feedback interpretation, support prioritization, and product insight generation. [web:60][web:55][web:66]

## Decision matrix

| Option | Fit | Pros | Cons | Recommended? |
|---|---|---|---|---|
| Manual tagging | Low | Simple to start, easy to explain | Slow, expensive, inconsistent | No |
| Rules only | Medium | Fast for fixed keywords and known patterns | Weak on ambiguity and language variety | No |
| Traditional ML classifier | High | Good for structured labeling and repeatable outputs | Needs training data and maintenance | Yes |
| LLM-based extraction | High | Flexible, handles varied language well | Needs guardrails and evaluation | Yes |
| Hybrid approach | Very high | Combines taxonomy, rules, ML/LLM, and human review | Slightly more design effort | Yes |

## Recommended approach

Use a hybrid approach:
- a business-defined aspect taxonomy.
- rules for obvious mappings and normalization.
- a classifier or LLM for aspect detection and sentiment.
- human review for ambiguous or high-impact cases.

This works well because aspect-based sentiment analysis often requires both structured business definitions and flexible language understanding. [web:59][web:60]

## FOBW lens

| FOBW question | Answer |
|---|---|
| What is the business objective? | Understand what customers like and dislike about specific aspects of the experience. |
| What outcome matters? | Better prioritization, faster insight, and improved customer experience. |
| What should we build? | A system that detects aspects and sentiment from customer feedback. |
| What will make it work? | Clear taxonomy, good evaluation, and human oversight for low-confidence cases. |

## Build vs buy

| Choice | When it makes sense |
|---|---|
| Buy | When the business wants quick time-to-value and standard dashboard-style insight. |
| Build | When the taxonomy, workflow, or integration is specific to the company. |
| Hybrid | When you want speed now and flexibility later. |

## Final decision

For the first version, use a hybrid AI solution with human review. This gives the business a practical balance of speed, quality, and control. It also creates a foundation for later automation if the pilot proves valuable. [web:60][web:61][web:65]
