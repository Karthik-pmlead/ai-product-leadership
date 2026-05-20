# 06_data_and_risk/data-quality.md

# Data Quality

## Purpose
Define the quality checks needed before modeling.

## Checks

| Check | Why it matters |
|---|---|
| Completeness | Missing text or metadata can reduce usefulness. |
| Noise level | Short or messy text may be hard to interpret. |
| Label quality | Inconsistent labels hurt model training and validation. |
| Taxonomy consistency | Aspect names must map cleanly to business categories. |
| Language mix | Multilingual data may require special handling. |

## Quality policy
- Use a small, clean pilot dataset first.
- Review samples manually before modeling.
- Standardize labels and aspect names.
- Track quality issues by source channel.

## Output
A dataset that is consistent enough for pilot-scale analysis.
