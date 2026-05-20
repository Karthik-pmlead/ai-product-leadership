# AI Product Thinking Repo

A repository for designing, evaluating, and shipping successful AI products for business.

## Purpose

This repo helps teams move from business problem to AI product decision, design, build, launch, and operation. It is organized to separate product thinking, model choice, and production operations so the work stays clear and reusable. GitHub recommends a README to explain what a repository does and how people should use it. [web:30][web:38]

## How to use this repo

| Step | Folder | What it covers |
|---|---|---|
| 1 | `01_problem_and_context` | Business problem, user pain points, constraints, assumptions, and success criteria. |
| 2 | `02_business_case` | ROI, feasibility, cost/benefit, prioritization, and stakeholder alignment. |
| 3 | `03_ai_decisioning` | AI vs rules vs workflow vs humans, FOBW, AI decision matrix, and build/buy/fine-tune decisions. |
| 4 | `04_prd_canvas` | AI PRD canvas, scope, users, outcomes, and product framing. |
| 5 | `05_solution_design` | Solution architecture, model choice, reasoning, interfaces, and fallback paths. |
| 6 | `06_data_and_risk` | Data sources, quality, privacy, security, bias, and risk controls. |
| 7 | `07_eval_and_quality` | Offline/online eval, test sets, acceptance criteria, red teaming, and monitoring metrics. |
| 8 | `08_implementation_and_roadmap` | Delivery phases, milestones, dependencies, rollout, and launch plan. |
| 9 | `09_ml_system_design_and_mlops` | Training/inference architecture, deployment, monitoring, versioning, retraining, and incident response. |
| 10 | `10_governance_and_ethics` | Policy, approvals, fairness, explainability, auditability, and compliance. |
| 11 | `11_prompting_and_examples` | Prompt patterns, prompt library, examples, guardrails, and review checklists. |
| 12 | `12_playbooks` | Reusable playbooks, operating guides, and launch checklists. |
| 13 | `99_templates` | Reusable templates for PRDs, business cases, eval plans, model cards, and MLOps. |

## Repository tree

```text
ai-product-thinking/
├── README.md
├── 00_overview/
│   ├── repo-principles.md
│   ├── naming-conventions.md
│   └── contribution-guide.md
├── 01_problem_and_context/
│   ├── problem-statement.md
│   ├── user-research.md
│   ├── assumptions.md
│   └── constraints.md
├── 02_business_case/
│   ├── roi-model.md
│   ├── feasibility.md
│   ├── prioritization.md
│   └── stakeholder-summary.md
├── 03_ai_decisioning/
│   ├── fobw-framework.md
│   ├── ai-decision-matrix.md
│   ├── build-vs-buy.md
│   ├── fine-tune-vs-rag-vs-prompt.md
│   └── use-case-suitability.md
├── 04_prd_canvas/
│   ├── ai-prd-canvas.md
│   ├── prd-one-pager.md
│   ├── scope-and-nongoals.md
│   └── success-metrics.md
├── 05_solution_design/
│   ├── solution-architecture.md
│   ├── model-selection-rationale.md
│   ├── input-output-contracts.md
│   ├── fallback-and-escalation.md
│   └── human-in-the-loop.md
├── 06_data_and_risk/
│   ├── data-inventory.md
│   ├── data-quality.md
│   ├── privacy-and-security.md
│   ├── bias-and-fairness.md
│   └── risk-register.md
├── 07_eval_and_quality/
│   ├── eval-plan.md
│   ├── test-cases.md
│   ├── acceptance-criteria.md
│   ├── red-team-cases.md
│   └── monitoring-metrics.md
├── 08_implementation_and_roadmap/
│   ├── roadmap.md
│   ├── milestones.md
│   ├── dependencies.md
│   ├── launch-plan.md
│   └── adoption-plan.md
├── 09_ml_system_design_and_mlops/
│   ├── ml-system-design.md
│   ├── serving-patterns.md
│   ├── deployment-pipeline.md
│   ├── monitoring-and-alerting.md
│   ├── retraining-workflow.md
│   └── incident-response.md
├── 10_governance_and_ethics/
│   ├── ai-policy.md
│   ├── approvals.md
│   ├── auditability.md
│   ├── compliance-checklist.md
│   └── responsible-ai-review.md
├── 11_prompting_and_examples/
│   ├── prompt-library.md
│   ├── prompt-patterns.md
│   ├── examples.md
│   ├── guardrails.md
│   └── prompt-review-checklist.md
├── 12_playbooks/
│   ├── product-launch-playbook.md
│   ├── evaluation-playbook.md
│   ├── review-rituals.md
│   └── operating-sop.md
└── 99_templates/
    ├── ai-prd-canvas-template.md
    ├── ai-decision-matrix-template.md
    ├── business-case-template.md
    ├── solution-design-template.md
    ├── eval-plan-template.md
    ├── model-card-template.md
    ├── mlops-checklist-template.md
    └── launch-checklist-template.md
```

## Where things belong

| Topic | Put it here | Why |
|---|---|---|
| Business use-case selection | `03_ai_decisioning` | This is where you decide whether AI is appropriate. |
| FOBW framework | `03_ai_decisioning` | It is a decision framework. |
| AI PRD canvas | `04_prd_canvas` | It is the product framing layer. |
| Model choice like FaceNet vs ResNet | `05_solution_design` | This is where architecture and model selection live. |
| Why a model was chosen | `03_ai_decisioning` + `05_solution_design` | Decision rationale goes in one folder; implementation choice goes in the other. |
| ML system design | `09_ml_system_design_and_mlops` | This is the production architecture layer. |
| MLOps | `09_ml_system_design_and_mlops` | This covers deployment, monitoring, retraining, and operations. |
| Eval strategy | `07_eval_and_quality` | This is where quality gates and test design belong. |
| Ethics and governance | `10_governance_and_ethics` | This is the responsible AI layer. |

## Recommended rule

| Question | Folder |
|---|---|
| Should we use AI? | `03_ai_decisioning` |
| Which model/architecture should we use? | `05_solution_design` |
| How do we ship and operate it? | `09_ml_system_design_and_mlops` |

## Core templates

| Template | File idea |
|---|---|
| AI PRD canvas | `99_templates/ai_prd_canvas_template.md` |
| AI decision matrix | `99_templates/ai_decision_matrix_template.md` |
| FOBW framework | `99_templates/fobw_framework.md` |
| Business case | `99_templates/business_case_template.md` |
| Solution design doc | `99_templates/solution_design_template.md` |
| Eval plan | `99_templates/eval_plan_template.md` |
| MLOps checklist | `99_templates/mlops_checklist_template.md` |
| Launch checklist | `99_templates/launch_checklist_template.md` |
| Model card | `99_templates/model_card_template.md` |

## Design principles

| Principle | Meaning |
|---|---|
| Separate decision from design | Decide what to build before choosing how to build it. |
| Separate design from operations | Model choice is not the same as deployment and monitoring. |
| Keep templates reusable | Use the same structure across multiple AI products. |
| Optimize for business impact | Every folder should support building successful AI products. |
