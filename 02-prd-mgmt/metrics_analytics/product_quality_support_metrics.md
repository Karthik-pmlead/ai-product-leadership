# Product Quality Metrics

## Overview

Product quality metrics measure how reliable, usable, stable, and supportable a product is. They help teams understand whether the product works as intended and whether users are experiencing friction, defects, or service issues [web:225][web:227][web:228].

## Core metrics

| Metric | What it measures | Why it matters | Notes |
|---|---|---|---|
| Bug Rate | Number of bugs per release, feature, or user base. | Shows product stability. | Useful for release and quality tracking [web:225][web:230]. |
| Defect Density | Defects found per unit of code or product area. | Helps locate weak areas. | Common software quality metric [web:225][web:231]. |
| Crash Rate | Percentage of sessions or users affected by app crashes. | Direct signal of product instability. | Critical for mobile and consumer apps [web:225][web:228]. |
| Uptime | Percentage of time the service is available. | Core reliability measure. | Important for platforms and SaaS [web:227][web:228]. |
| Latency | Time taken for the product to respond. | Impacts user experience. | Also called response time [web:228]. |
| Error Rate | Frequency of failed requests or system errors. | Shows technical reliability. | Important in APIs and apps [web:225][web:228]. |
| Test Coverage | Percentage of code covered by tests. | Indicates test depth. | Not equal to quality, but useful [web:225]. |
| MTTR | Mean time to repair or restore service after a failure. | Measures incident recovery speed. | Strong reliability metric [web:225][web:227]. |
| Lead Time for Changes | Time from code commit to production deployment. | Shows delivery speed and pipeline health. | Common software delivery metric [web:225]. |
| Release Frequency | How often new versions are shipped. | Measures delivery cadence. | Useful with quality safeguards [web:225]. |

## Support and service quality

| Metric | What it measures | Why it matters | Notes |
|---|---|---|---|
| CSAT | Customer satisfaction after a support or product interaction. | Measures satisfaction at key touchpoints. | Best after specific events [web:226]. |
| NPS | Likelihood to recommend the product. | Measures loyalty and advocacy. | Better as a directional metric [web:226]. |
| CES | Customer effort needed to resolve an issue. | Shows ease of getting help. | Lower effort is better [web:226]. |
| First Contact Resolution (FCR) | Issues solved on the first interaction. | Measures support effectiveness. | High FCR usually means better service [web:226][web:232]. |
| SLA Compliance | Percentage of tickets or requests handled within SLA. | Measures service reliability. | Important for customer support teams [web:226]. |
| Average Ticket Resolution Time | Time taken to close a support ticket. | Shows support speed. | Track by issue type and channel. |
| Ticket Backlog | Open unresolved support requests. | Shows operational load. | Large backlog can indicate service problems. |
| Escalation Rate | Tickets escalated to higher support tiers. | Shows complexity or poor first-line resolution. | Useful for process improvement. |
| Customer-Reported Bugs | Bugs reported by users after release. | Measures quality from the customer’s perspective. | Important complement to internal defect counts [web:225]. |

## Example interpretation

| Metric | Good signal | Bad signal |
|---|---|---|
| Bug Rate | Falling over time. | Rising after each release. |
| Uptime | Above target SLA. | Frequent outages. |
| Latency | Fast and consistent. | Slow or spiky response times. |
| CSAT | Improving after support changes. | Declining after product releases. |
| FCR | More issues solved immediately. | Repeated transfers and escalations. |

## How to use these metrics

| Use case | Best metrics |
|---|---|
| Release quality | Bug Rate, Defect Density, Crash Rate, Test Coverage |
| Reliability | Uptime, Error Rate, MTTR, Latency |
| Support quality | CSAT, CES, FCR, SLA Compliance |
| Operational health | Ticket Backlog, Escalation Rate, Resolution Time |
| Customer perspective | CSAT, NPS, Customer-Reported Bugs |

## Practical tips

| Tip | Why it helps |
|---|---|
| Combine technical and customer metrics | A product can be technically healthy but still feel bad to users. |
| Track trends, not only snapshots | Quality problems often emerge over time. |
| Segment by platform | Web, iOS, Android, and API quality can differ. |
| Review by release | Helps link quality changes to product launches. |
| Use thresholds | Define what “good” and “bad” look like in advance. |

## Interview use

In interviews, describe product quality metrics as the signals that tell you whether the product is stable, reliable, and easy to use. Then show how you would connect technical metrics like uptime and crash rate with customer-facing metrics like CSAT and FCR.
