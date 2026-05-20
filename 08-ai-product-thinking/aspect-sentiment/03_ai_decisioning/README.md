# 03_ai_decisioning

This folder defines whether AI should be used and what kind of AI approach is appropriate for the aspect sentiment use case.

## Purpose

The purpose of this folder is to decide whether aspect sentiment should be solved with AI, rules, human review, or a hybrid approach. It also explains the reasoning behind build vs buy and prompting vs fine-tuning choices.

## Why this matters

Not every problem needs the same AI approach. This folder helps the team choose the simplest solution that can still deliver business value. [web:30][web:130]

## Folder contents

| File | Purpose |
|---|---|
| [ai-decision-matrix](ai-decision-matrix.md) | Main decision matrix for the use case. |
| [fobw-framework](fobw-framework.md) | Framework for assessing whether AI is the right fit. |
| [build-vs-buy](build-vs-buy.md) | Compares buying a solution vs building one. |
| [fine-tune-vs-rag-vs-prompt](fine-tune-vs-rag-vs-prompt.md) | Compares model strategy options. |
| [use-case-suitability](use-case-suitability.md) | Scores how strong this use case is as a candidate. |

## Example use case

For aspect sentiment, this folder should usually lead to a hybrid approach: use business-defined aspects, lightweight ML or prompting, and human review for uncertain cases. [web:56][web:101][web:107]

## Output of this folder

By the end of this folder, the team should know:
- whether AI is the right choice,
- which approach is best,
- and how the solution should be framed before design begins.
