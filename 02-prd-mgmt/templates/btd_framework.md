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

**Application Process:**

    Identify Intersection Points - Map where business objectives, tech capabilities, and data assets overlap

    Assess Balance - Ensure appropriate balance across all three domains (imbalance leads to implementation challenges)

    Iterate & Refine - Use continuously throughout product lifecycle
    
### Why BTD Matters for AI Products

Traditional software products focus primarily on business and technology. AI products add **data as a third critical dimension** because:

- **Data drives AI performance** - Model quality depends on data quality
- **Data is a strategic asset** - Proprietary data creates competitive advantage
- **Data requires governance** - Privacy, compliance, and ethics are critical
- **Data pipelines are complex** - Need to build, monitor, and maintain constantly
- **Data has lifecycle** - Drift, degradation, and retraining requirements

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

### Example: Planning an AI Chatbot

**Phase-Based Approach:**
1. Strategy: Build business case for chatbot
2. Discovery: Create AI PRD canvas
3. Planning: Design evaluation plan, model card
4. Launch: Use launch checklist

**BTD Quality Check:**
**Business:**
✓ Business case shows ROI (cost savings from reduced support)
✓ Success metrics defined (deflection rate, CSAT)
✓ User needs validated (customers want 24/7 support)

**Technology:**
✓ LLM selected via decision matrix
✓ Solution design includes API, vector DB, caching
✓ MLOps checklist covers deployment, monitoring

**Data:**
✓ Eval plan includes chat transcripts, test conversations
✓ Model card documents training data (support tickets)
✓ Privacy: PII masked, GDPR compliant

---

## BTD Framework Checklist

Use this checklist at each project phase to ensure balanced BTD coverage:

### Strategy Phase BTD Checklist

**Business:**
- [ ] Problem clearly defined and quantified
- [ ] Target users/personas identified
- [ ] Business value articulated (revenue, cost, risk)
- [ ] ROI estimation completed
- [ ] Strategic alignment confirmed

**Technology:**
- [ ] Technical feasibility assessed
- [ ] High-level architecture sketched
- [ ] Integration requirements identified
- [ ] Scalability considerations noted

**Data:**
- [ ] Data availability confirmed
- [ ] Data quality assessed
- [ ] Data requirements documented
- [ ] Privacy/compliance requirements identified

### Discovery Phase BTD Checklist

**Business:**
- [ ] AI PRD canvas completed
- [ ] Success metrics defined
- [ ] User stories written
- [ ] Business objectives aligned

**Technology:**
- [ ] Model selection via decision matrix
- [ ] Solution design documented
- [ ] Tech stack chosen
- [ ] Technical risks identified

**Data:**
- [ ] Data sources identified
- [ ] Data pipeline designed
- [ ] Data quality plan created
- [ ] Data governance planned

### Planning Phase BTD Checklist

**Business:**
- [ ] Business case updated with latest info
- [ ] Budget approved
- [ ] Stakeholders aligned
- [ ] Go-to-market strategy defined

**Technology:**
- [ ] MLOps checklist completed
- [ ] CI/CD pipeline ready
- [ ] Monitoring configured
- [ ] Security review done

**Data:**
- [ ] Evaluation plan created
- [ ] Model card drafted
- [ ] Dataset prepared
- [ ] Data validation rules defined

### Launch Phase BTD Checklist

**Business:**
- [ ] Success metrics baseline established
- [ ] Stakeholders notified
- [ ] Customer communication ready
- [ ] Support team trained

**Technology:**
- [ ] Launch checklist completed
- [ ] Rollback plan ready
- [ ] Performance tested
- [ ] Monitoring active

**Data:**
- [ ] Data pipeline operational
- [ ] Data quality monitoring active
- [ ] Privacy controls in place
- [ ] Data retention configured

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
