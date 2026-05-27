13_risks_and_failure_modes.md

# Risks & Failure Modes — Face Recognition Attendance System

---

# Purpose

This document identifies:
- operational risks
- AI risks
- security risks
- infrastructure failures
- organizational risks

A strong AI PM should proactively think about:
- what can fail
- why it can fail
- how to detect failures
- how to mitigate them

---

# Major Risk Categories

1. AI/Model Risks
2. Security Risks
3. Infrastructure Risks
4. Operational Risks
5. Privacy & Compliance Risks
6. User Experience Risks
7. Organizational Risks

---

# 1. AI / Model Risks

---

# False Rejections (High FRR)

Valid employees are rejected incorrectly.

---

# Causes

| Cause | Example |
|---|---|
| Poor lighting | Warehouse entry |
| Occlusions | Masks/glasses |
| Camera angle | Side profile |
| Demographic bias | Uneven model performance |
| Aging effects | Appearance changes |

---

# Impact

- employee frustration
- attendance disputes
- reduced trust
- operational delays

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Better training data | Improve robustness |
| Multi-angle enrollment | Better matching |
| Infrared cameras | Lighting robustness |
| Human fallback workflows | Continuity |
| Adaptive thresholds | Reduce failures |

---

# False Acceptances (High FAR)

Unauthorized users are accepted.

---

# Impact

- payroll fraud
- security breaches
- compliance violations

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Stricter thresholds | Better security |
| Liveness detection | Prevent spoofing |
| Multi-factor authentication | Higher assurance |
| Security monitoring | Threat detection |

---

# Model Drift

Performance degrades over time.

---

# Causes

| Cause | Example |
|---|---|
| Environmental changes | New office lighting |
| Population changes | New employee demographics |
| Attack evolution | New spoofing methods |

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Continuous monitoring | Detect degradation |
| Periodic retraining | Improve accuracy |
| Drift dashboards | Operational visibility |

---

# 2. Security Risks

---

# Spoofing Attacks

Examples:
- printed photos
- replay videos
- deepfakes
- masks

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Liveness detection | Detect real humans |
| Depth sensing | Prevent flat-image attacks |
| Challenge-response | Prevent replay attacks |

---

# Biometric Data Breach

Impact:
- irreversible privacy exposure
- legal consequences
- employee trust loss

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Encryption | Protect data |
| RBAC | Limit access |
| Embedding storage | Reduce sensitivity |
| Audit logging | Detect misuse |

---

# Insider Threats

Internal misuse of privileged access.

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Least-privilege access | Reduce exposure |
| Access reviews | Governance |
| Audit trails | Accountability |

---

# 3. Infrastructure Risks

---

# Network Failures

Impact:
- delayed authentication
- attendance disruption

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Offline mode | Business continuity |
| Edge inference | Reduced dependency |
| Failover networks | Reliability |

---

# Camera Failures

Examples:
- hardware malfunction
- obstruction
- physical damage

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Redundant cameras | Availability |
| Device monitoring | Early detection |
| Preventive maintenance | Reliability |

---

# Peak-Hour Scalability Failures

Examples:
- shift changes
- office entry surges

---

# Impact

- high latency
- authentication queues
- employee dissatisfaction

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Autoscaling | Handle traffic |
| Load balancing | Traffic distribution |
| Queue management | Stability |

---

# 4. Operational Risks

---

# Manual Override Abuse

Risk:
- fraudulent attendance correction

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Audit logging | Traceability |
| Approval workflows | Governance |
| Exception monitoring | Abuse detection |

---

# Enrollment Failures

Employees cannot register properly.

---

# Causes

- poor image quality
- incomplete enrollment
- environmental issues

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Guided enrollment UX | Better capture |
| Enrollment validation | Quality control |
| Assisted onboarding | Reduced failure |

---

# 5. Privacy & Compliance Risks

---

# Privacy Violations

Examples:
- over-retention
- surveillance concerns
- unauthorized analytics

---

# Impact

- legal exposure
- employee distrust
- regulatory penalties

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Explicit consent | Transparency |
| Data minimization | Lower risk |
| Retention limits | Compliance |
| Governance reviews | Oversight |

---

# 6. User Experience Risks

---

# Poor Authentication Experience

Examples:
- repeated retries
- slow authentication
- unclear failure reasons

---

# Impact

- low adoption
- reduced trust
- operational frustration

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Fast inference | Better UX |
| Clear feedback | Transparency |
| Retry guidance | Reduced friction |

---

# Employee Resistance

Employees may perceive:
- surveillance
- privacy invasion
- unfairness

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Transparent communication | Build trust |
| Consent workflows | Respect privacy |
| Clear governance | Accountability |

---

# 7. Organizational Risks

---

# Cross-Functional Misalignment

Examples:
- HR vs Security priorities
- IT vs Compliance concerns

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Governance committees | Alignment |
| Shared KPIs | Coordination |
| Clear ownership | Accountability |

---

# Vendor Dependency Risk

Risk:
- lock-in
- pricing changes
- limited flexibility

---

# Mitigations

| Mitigation | Purpose |
|---|---|
| Modular architecture | Flexibility |
| API abstraction | Easier migration |
| Hybrid strategy | Reduced dependency |

---

# Failure Detection Framework

```text
System Monitoring
        ↓
Anomaly Detection
        ↓
Alert Generation
        ↓
Incident Triage
        ↓
Mitigation Workflow
        ↓
Recovery
        ↓
Postmortem


Severity Classification

| Severity | Example               |
| -------- | --------------------- |
| Sev-1    | Authentication outage |
| Sev-2    | High FRR spike        |
| Sev-3    | Regional degradation  |
| Sev-4    | Minor UX issue        |


Risk Prioritization Matrix

| Risk                  | Likelihood | Impact   |
| --------------------- | ---------- | -------- |
| False rejections      | High       | Medium   |
| Spoofing              | Medium     | High     |
| Data breach           | Low        | Critical |
| Employee resistance   | Medium     | High     |
| Infrastructure outage | Medium     | High     |


AI PM Interview Insight

Strong candidates:

anticipate failures
design fallback mechanisms
discuss monitoring
think operationally

not just:

model accuracy.

Final Principle

Biometric systems should be designed assuming:

Failures WILL happen.

The goal is:

graceful degradation
rapid recovery
minimal user disruption
strong governance

