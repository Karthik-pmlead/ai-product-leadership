# 04_prd_canvas/ai-prd-canvas.md

# AI PRD Canvas

## Product name
Aspect Sentiment Intelligence

## Problem
Customer feedback is unstructured and spread across multiple channels, making it hard to see what customers feel about specific aspects of the product or service.

## Target users

| User | Need |
|---|---|
| Product managers | Understand which aspects drive positive or negative sentiment. |
| CX teams | Track customer themes over time. |
| Support leaders | Find recurring customer pain points. |
| Operations leaders | Identify process or service issues. |

## Desired outcome
Convert raw customer feedback into aspect-level sentiment insight that teams can use for prioritization and action.

## Scope

| In scope | Out of scope |
|---|---|
| Aspect identification | Full customer journey orchestration |
| Sentiment classification by aspect | Automated resolution of customer complaints |
| Feedback summaries by theme | Emotion detection beyond basic sentiment in v1 |
| Trend reporting | Real-time decision automation |

## Core aspects

| Aspect | Example |
|---|---|
| Product quality | Durability, defects, reliability |
| Delivery | Speed, delay, packaging arrival |
| Support | Response quality, helpfulness, escalation |
| Pricing | Value, affordability, fairness |
| Usability | Ease of use, friction, confusion |

## Example input and output

| Input | Output |
|---|---|
| "The product quality is great, but delivery was slow and support was unhelpful." | Product quality = positive, Delivery = negative, Support = negative |

## User experience

| Step | Experience |
|---|---|
| 1 | User uploads or streams customer feedback. |
| 2 | System detects the aspect mentioned in each comment. |
| 3 | System assigns sentiment to each aspect. |
| 4 | User views trends, summaries, and issue hotspots. |

## Success metrics

| Metric | What it means |
|---|---|
| Aspect coverage | How many comments can be mapped to an aspect. |
| Sentiment quality | How reliable the sentiment labels are. |
| Trend usefulness | Whether users can spot patterns and act on them. |
| Adoption | Whether teams actually use the output in reviews. |

## Assumptions
The feedback contains enough signal to identify meaningful aspects, and the business has a manageable taxonomy of core aspects for the first version. Human review will be available for ambiguous or high-risk cases.

## Constraints
Feedback may be noisy, multilingual, or short. The first version should stay focused on a few channels and a few aspects so the system remains easy to validate and explain.

## Next step
Define solution design, evaluation criteria, and implementation roadmap for the first pilot.
