# AI Product Requirements Document (PRD) Canvas

**Product Name:** [Name]  
**Owner:** [PM Name]  
**Status:** [Draft / In Review / Approved]  
**Last Updated:** [Date]  
**Version:** [1.0]

---

## 1. Problem Statement

### What problem are we solving?
[Clear description of the user problem or opportunity]

- **Who:** [Target users/personas]
- **What:** [The problem they face]
- **Why it matters:** [Impact/importance]
- **Current workarounds:** [How users solve this today]

### Why AI?
[Justification for using AI vs. traditional rules-based approach]

---

## 2. Goals & Success Metrics

### User Goals
- [Goal 1]
- [Goal 2]

### Business Goals
- [Goal 1]
- [Goal 2]

### Success Metrics
| Metric | Target | How Measured |
|--------|--------|--------------|
| [Metric 1] | [Target] | [Method] |
| [Metric 2] | [Target] | [Method] |
| [Accuracy/Quality Metric] | [Target %] | [Evaluation method] |

### Non-Goals
[What this project explicitly will NOT do]

---

## 3. AI Model Requirements

### Model Type
- [ ] LLM (Large Language Model)
- [ ] Classification Model
- [ ] Regression Model
- [ ] Generative Model
- [ ] Recommendation System
- [ ] Other: [Specify]

### Model Specifications
| Attribute | Requirement |
|-----------|-------------|
| Input Type | [Text/Image/Video/Tabular/etc.] |
| Output Type | [Text/Classification/Score/etc.] |
| Expected Latency | [< X ms] |
| Throughput | [X requests/second] |
| Accuracy Target | [X%] |
| Hallucination Tolerance | [Low/Medium/High] |

### Model Source
- [ ] Custom-trained model
- [ ] Third-party API (e.g., GPT-4, Claude)
- [ ] Open-source model (e.g., Llama, Mistral)
- [ ] Fine-tuned existing model

### Training Data Requirements
- **Data Type:** [Describe data needed]
- **Data Volume:** [X examples/samples]
- **Data Quality:** [Requirements for labeling/cleaning]
- **Data Sources:** [Where data comes from]
- **Privacy/Compliance:** [GDPR, HIPAA, etc.]

---

## 4. AI Behavior & Constraints

### Expected AI Actions
[What the AI is expected to do - the decision or action it should take]

### Input Requirements
- **Required Inputs:**
  - [Input 1]: [Description, format, quality]
  - [Input 2]: [Description, format, quality]

### Output Requirements
- **Expected Output:** [Description of output format and content]
- **Output Quality Standards:** [Acceptable quality ranges]

### Edge Cases & Failure Modes
| Scenario | Expected Behavior | Fallback |
|----------|-----------------|----------|
| [Edge case 1] | [How AI should handle] | [Fallback action] |
| [Edge case 2] | [How AI should handle] | [Fallback action] |
| Low confidence | [Threshold: X%] | [Fallback to human/rules] |

### Guardrails & Constraints
- [Constraint 1: e.g., "Must not generate PII"]
- [Constraint 2: e.g., "Must stay within brand guidelines"]
- [Constraint 3: e.g., "Must reject harmful inputs"]

---

## 5. User Experience & Flow

### User Stories
**As a** [user type]  
**I want to** [action]  
**So that** [benefit]

### User Flow
**Flow 1:** [Description]
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Example Prompts/Inputs
| Use Case | Example Input | Expected Output |
|----------|---------------|-----------------|
| [Case 1] | "[Input]" | "[Expected output]" |
| [Case 2] | "[Input]" | "[Expected output]" |

---

## 6. Evaluation Plan

### Evaluation Criteria
| Criterion | Target | Evaluation Method |
|-----------|--------|-------------------|
| Accuracy | [X%] | [Method] |
| Precision | [X%] | [Method] |
| Recall | [X%] | [Method] |
| User Satisfaction | [X/5] | [Survey/Feedback] |
| Latency | [< X ms] | [Monitoring] |

### Evaluation Dataset
- **Size:** [X samples]
- **Composition:** [Description of test data]
- **Source:** [Where test data comes from]

### Ongoing Monitoring
- **Metrics to track:** [List metrics]
- **Alerting thresholds:** [When to alert]
- **Retraining triggers:** [When to retrain model]

---

## 7. Risk Mitigation

### Risks
| Risk | Impact | Likelihood | Mitigation Strategy |
|------|--------|------------|---------------------|
| [Risk 1] | [High/Med/Low] | [High/Med/Low] | [Strategy] |
| [Bias/Fairness issue] | [High/Med/Low] | [High/Med/Low] | [Strategy] |
| [Hallucination] | [High/Med/Low] | [High/Med/Low] | [Strategy] |
| [Data privacy] | [High/Med/Low] | [High/Med/Low] | [Strategy] |

### Cost of Failure
[What happens if the AI is wrong or underperforms - impact on people, operations, cost]

### Value of Success
[How outcomes improve and value created - savings, revenue, risk reduction]

---

## 8. Technical Considerations

### Technical Constraints
- **Stack:** [Languages, frameworks, versions]
- **Existing codebase:** [Key files and patterns]
- **API contracts:** [External services, data formats]
- **Prohibitions:** [What the AI agent must NOT do]

### Integration Requirements
- **APIs Needed:** [List APIs]
- **Data Pipelines:** [Description]
- **Infrastructure:** [Cloud/on-prem, compute requirements]

### Security & Compliance
- [ ] Data encryption (at rest and in transit)
- [ ] Access controls and authentication
- [ ] Compliance: [GDPR, HIPAA, SOC2, etc.]
- [ ] Audit logging requirements

---

## 9. Ethical Considerations

### Ethical Risks
- [Potential bias in training data]
- [Fairness across user groups]
- [Transparency and explainability]
- [User consent and data usage]

### Human-AI Interaction
[How will humans and AI interact? What decisions remain with humans?]

---

## 10. Go-to-Market Strategy

### Roll-out Plan
- [ ] A/B test
- [ ] Canary deployment
- [ ] Full launch

### Phases
**Phase 1:** [Name]  
**Dependencies:** None  
**Scope:** [What this phase covers]  
**Tasks:**
1. [Task 1]
2. [Task 2]  
**Testable output:** [How to verify]

**Phase 2:** [Name]  
**Dependencies:** Phase 1  
**Scope:** [What this phase covers]  
**Tasks:**
1. [Task 1]
2. [Task 2]  
**Testable output:** [How to verify]

### Target Launch Date
[Date]

---

## 11. Requirements Priority

### Must Have (P0)
- [ ] [Requirement 1]
- [ ] [Requirement 2]

### Should Have (P1)
- [ ] [Requirement 3]

### Nice to Have (P2)
- [ ] [Requirement 4]

---

## 12. Appendix

- [Supporting research]
- [Mockups/Wireframes]
- [Data samples]
- [Competitive analysis]
- [Related documents]

---

## Approvals

| Role | Name | Status | Date |
|------|------|--------|------|
| Product Manager | [Name] | [Approved/Pending] | [Date] |
| AI/ML Lead | [Name] | [Approved/Pending] | [Date] |
| Engineering Lead | [Name] | [Approved/Pending] | [Date] |
| Legal/Security | [Name] | [Approved/Pending] | [Date] |

---

*This template is adapted from best practices for AI product management, including guidance from Product School, IdeaPlan, and industry standards for AI/ML product development.*
