# Sales Operations Classification / Triage

This folder contains the product and solution blueprint for the sales operations classification / triage use case.

## Purpose

The goal of this use case is to classify and route incoming sales-related items such as leads, emails, requests, forms, and CRM updates into the right category, priority, or team.

## Why this matters

Sales operations teams spend significant time manually sorting and routing incoming work. Classification and triage reduce delay, improve consistency, and help high-value requests reach the right owner faster. [web:264][web:269][web:272]

## Folder contents

| File | Purpose |
|---|---|
| `01_problem_and_context.md` | Merges problem statement, user context, assumptions, and constraints. |
| `02_business_case.md` | Explains the value and feasibility of sales triage. |
| `03_ai_decisioning.md` | Explains why classification / triage is the right AI approach. |
| `04_prd_canvas.md` | Defines the product scope, users, and success metrics. |
| `05_solution_design.md` | Describes classification, routing, and fallback design. |
| `06_data_and_risk.md` | Covers data sources, privacy, and triage risks. |
| `07_eval_and_quality.md` | Defines how triage quality will be tested and monitored. |
| `08_implementation_and_roadmap.md` | Lays out the delivery plan and milestones. |
| `09_ml_system_design_and_mlops.md` | Covers serving, monitoring, and retraining. |
| `10_governance_and_ethics.md` | Covers approvals, auditability, and responsible AI. |

## How to use this folder

Read the files in order from `01_problem_and_context.md` through `10_governance_and_ethics.md`. Start with the sales routing problem, then confirm the business case, then design the classification system and quality checks.

## Suggested first scope

A strong first version should:
- support one stream first, such as inbound leads or support-like sales requests.
- use a fixed taxonomy.
- include confidence scores and human review.
- route uncertain cases to a person or queue.

## Output of this folder

By the end of this folder, the team should have a clear sales triage product definition and a practical implementation path.
