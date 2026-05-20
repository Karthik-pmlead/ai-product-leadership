# 04_prd_canvas/ai-prd-canvas.md

# AI PRD Canvas

## Purpose
Capture the core product definition for aspect sentiment analysis in one place so the team can align on the problem, users, outputs, scope, and success criteria before solution design begins.

## Product summary
Aspect sentiment analysis converts unstructured customer feedback into structured insights about what customers feel toward specific business aspects such as product quality, delivery, support, pricing, and usability. This supports better customer experience decisions and faster prioritization. Aspect-based sentiment analysis is especially useful when businesses want detailed insights from feedback rather than only overall sentiment. [web:56][web:66][web:99]

## Product vision
Create a reliable insight layer that helps teams understand which parts of the customer experience are working, which are failing, and where to act first.

## Problem
Customer feedback is too unstructured and high-volume for teams to analyze manually at scale. As a result, important aspect-level signals get lost in summaries, spreadsheets, and ad hoc reviews.

## Target users

| User | Need | Output they want |
|---|---|---|
| Product managers | Understand what customers feel about specific product aspects. | Aspect-level sentiment trends and top issues. |
| CX / VoC teams | Track recurring themes across feedback sources. | Dashboards and reports. |
| Support leaders | Identify common customer complaints faster. | Ticket and comment summaries by aspect. |
| Operations leaders | Spot service or process issues. | Trend alerts and issue hotspots. |
| Executives | See customer experience health at a glance. | Simple business summaries and trend views. |

## User jobs to be done

| User | Job to be done |
|---|---|
| Product manager | Prioritize fixes based on the customer pain points that matter most. |
| CX analyst | Summarize feedback into themes that can be shared with leadership. |
| Support manager | Find which issues are recurring and should be escalated. |
| Operations lead | Detect service failures and operational bottlenecks early. |

## Scope

| In scope | Out of scope |
|---|---|
| Aspect detection from text | Full conversational support automation |
| Sentiment classification by aspect | Emotion detection beyond sentiment in v1 |
| Trend analysis by aspect | Autonomous decision-making |
| Feedback ingestion from selected channels | Full omnichannel enterprise rollout |
| Human review for ambiguous cases | Fully unsupervised production release |

## Core aspects

| Aspect | Example subtopics |
|---|---|
| Product quality | Defects, durability, reliability |
| Delivery | Speed, delay, packaging, arrival |
| Support | Response time, helpfulness, escalation |
| Pricing | Cost, fairness, value |
| Usability | Ease of use, friction, confusion |

## Example input and output

| Input | Expected output |
|---|---|
| "The product quality is great, but delivery was slow and support was unhelpful." | Product quality = positive, Delivery = negative, Support = negative |

## Success metrics

| Metric | Meaning |
|---|---|
| Aspect coverage | Share of comments mapped to at least one aspect. |
| Sentiment quality | Confidence that the labels reflect the actual customer meaning. |
| Actionability | Whether teams use the insights in reviews and planning. |
| Time to insight | How quickly teams can identify issues from new feedback. |
| Adoption | Whether the output becomes part of regular business workflows. |

## Assumptions
- Feedback contains enough information to identify useful aspects.
- The business can define a manageable taxonomy for v1.
- Human review will be available for uncertain or high-risk outputs.
- Teams will use the insights if they are easy to trust and interpret.

## Constraints
- Feedback may be noisy, 
