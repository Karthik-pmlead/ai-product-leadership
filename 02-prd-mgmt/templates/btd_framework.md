# Business-Technology-Data (BTD) Framework for AI Products

**Overview:** The BTD Framework ensures balanced consideration of three critical domains when building AI products. This guide maps our phase-based templates to the BTD framework.

---

## What is the BTD Framework?

The BTD Framework (from ThinkAIPM) treats **data as a third critical domain** alongside business and technology for AI products.

| Domain | Focus | Key Questions |
|--------|-------|---------------|
| **Business** | Maximize value, optimize ROI | What problem? Who benefits? What's the ROI? |
| **Technology** | Tech stack & development | What models? What infrastructure? Scalable? |
| **Data** | Data for develop/launch/operate | What data needed? Quality sufficient? Privacy? |

**Why Data Matters for AI:** Data drives AI performance, is a strategic asset, requires governance, and has lifecycle (drift, retraining).

---

## Template Mapping to BTD Framework

Our templates are organized by **project phases**. Here's how they map to BTD domains:

| BTD Domain | Strategy Phase | Discovery Phase | Planning Phase | Launch Phase | Enablement Phase |
|------------|----------------|-----------------|----------------|--------------|------------------|
| **Business** | [business_case_template.md](./business_case_template.md) | [ai_prd_canvas_template.md](./ai_prd_canvas_template.md) | [ai_decision_matrix_template.md](./ai_decision_matrix_template.md) | [launch_checklist_template.md](./launch_checklist_template.md) | - |
| **Technology** | - | [solution_design_template.md](./solution_design_template.md) | [mlops_checklist_template.md](./mlops_checklist_template.md) | [launch_checklist_template.md](./launch_checklist_template.md) | - |
| **Data** | - | [fobw_framework.md](./fobw_framework.md) | [eval_plan_template.md](./eval_plan_template.md) | [model_card_template.md](./model_card_template.md) | - |

---

## Using Both Frameworks Together

### Recommended Workflow

**1. Execute Using Phases:**
Strategy → Discovery → Planning → Launch → Enablement


**2. Quality Check Using BTD:**
At each phase, ask:

    Business: Value, ROI, user needs addressed?

    Technology: Feasibility, scalability covered?

    Data: Quality, governance, pipelines planned?


**3. Fill Gaps:**
- **Business gap** → Use business_case_template.md, ai_prd_canvas_template.md
- **Technology gap** → Use solution_design_template.md, ai_decision_matrix_template.md
- **Data gap** → Use eval_plan_template.md, model_card_template.md

---

## When to Use BTD Framework

| Use BTD | Don't Use BTD |
|---------|---------------|
| Starting a new AI project | Day-to-day execution |
| Project stuck or failing | - |
| Post-mortem review | - |

---

## Key Takeaway

**Use both frameworks:**
- **Phases** = What to do and when (execution)
- **BTD** = What to cover (quality check)

This ensures no gaps in business, technology, or data coverage.

---

*Based on ThinkAIPM's AI Product Management framework. [thinkaipm.com/frameworks](https://thinkaipm.com/frameworks)*
