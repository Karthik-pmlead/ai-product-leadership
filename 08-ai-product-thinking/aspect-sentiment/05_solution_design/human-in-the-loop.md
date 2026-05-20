# 05_solution_design/human-in-the-loop.md

# Human in the Loop

## Purpose
Define when human review is required and how it should work.

## Review triggers

| Trigger | Action |
|---|---|
| Low confidence | Send to human review. |
| Conflicting aspect sentiment | Flag for manual inspection. |
| Sensitive feedback | Escalate to review. |
| Unclear aspect mapping | Mark as ambiguous. |

## Review workflow
1. System processes feedback.
2. Low-confidence or sensitive items are routed to reviewers.
3. Reviewer confirms, corrects, or re-labels the output.
4. Corrections are logged for future improvement.

## Why this matters
Human review increases trust, reduces error risk, and helps the model improve over time. It is especially important in aspect-based sentiment analysis where one comment can contain multiple sentiments. [web:108][web:113]

## Review principle
Use automation for scale, but keep humans in the loop for ambiguity and high-value decisions.
