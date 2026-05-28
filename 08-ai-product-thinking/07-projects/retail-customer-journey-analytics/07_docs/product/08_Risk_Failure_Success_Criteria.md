# 08_Risk_Failure_Success_Criteria.md

## 🎯 Success Criteria (Business Outcomes)

### Primary Success Metrics (6 months)
| Metric | Baseline | Target | Measurement Method |
|--------|----------|--------|--------------------|
| **CJCR (Funnel Completion)** | 22% | 28% | `analytics_funnel` query |
| **90-day Retention** | 35% | 42% | Cohort analysis |
| **Time-to-insight** | 2 days | 2 hours | Query-to-dashboard time |
| **Pipeline runtime** | Manual (4 hrs) | 30 mins | CloudWatch logs |
| **Active users** | 0 | 50+ | Metabase + Streamlit login |

### Secondary Success Metrics
| Metric | Target | Owner |
|--------|--------|-------|
| Data quality issues/month | < 2 | Data Engineer |
| Dashboard load time | < 3 secs | Data Engineer |
| User satisfaction (NPS) | ≥ 40 | Product Manager |
| Marketing campaigns using funnel | 5+ | Marketing Lead |

## 🚨 Risk Matrix

### High-Priority Risks

| Risk | Probability | Impact | Mitigation | Owner | Status |
|------|-------------|--------|------------|-------|--------|
| **Pipeline fails silently** | Medium | High | CloudWatch alarms + SNS alerts | Data Eng | ☐ |
| **Data quality issues (nulls)** | High | High | Great Expectations suite, fail on error | Data Eng | ☐ |
| **Redshift query too slow** | Medium | Medium | Cluster scaling, query optimization | Data Eng | ☐ |
| **Low user adoption** | Medium | High | Training sessions, executive sponsorship | PM | ☐ |
| **Security breach (PII leak)** | Low | Critical | IAM least privilege, encryption, audit | Security | ☐ |

### Medium-Priority Risks

| Risk | Probability | Impact | Mitigation | Owner | Status |
|------|-------------|--------|------------|-------|--------|
| **AWS cost overrun** | Medium | Medium | Budget alerts, monthly review | PM | ☐ |
| **Team bandwidth (1 engineer)** | High | Medium | Prioritize MVP, defer ML | PM | ☐ |
| **Metabase dashboard confusion** | Medium | Low | User testing, simplified UI | Analyst | ☐ |
| **Funnel definition disagreements** | Medium | Medium | Document definitions, PM approval | PM | ☐ |

### Low-Priority Risks

| Risk | Probability | Impact | Mitigation | Owner | Status |
|------|-------------|--------|------------|-------|--------|
| **CSV file format changes** | Low | Low | Schema validation step | Data Eng | ☐ |
| **Streamlit app bugs** | Low | Medium | Unit tests, beta testing | PM | ☐ |

## 💥 Failure Modes & Recovery

### Failure Mode 1: Pipeline Does Not Complete
**Symptoms:**  
- CloudWatch shows "Job failed" status
- Redshift table row count < expected

**Root Causes:**  
- S3 upload incomplete
- EC2 script error (Python exception)
- Redshift COPY command failure

**Recovery Steps:**  
1. Check CloudWatch logs for error message
2. Re-run EC2 script manually: `python transform_ec2.py`
3. If S3 issue: Re-upload CSV, verify checksum
4. If Redshift issue: Truncate table, re-run COPY
5. Notify team via Slack #retail-analytics

**Prevention:**  
- Add error handling in Python script
- Set up CloudWatch alarm: If job fails → SNS notification
- Weekly dry-run test

---

### Failure Mode 2: Data Quality Degradation
**Symptoms:**  
- Null values in critical columns (order_id, customer_id)
- Duplicate order_id entries
- Price values < 0

**Root Causes:**  
- Source CSV corrupted
- Transformation bug (JOIN incorrectly)
- Silent data truncation

**Recovery Steps:**  
1. Run Great Expectations suite to identify failed checks
2. Restore raw CSV from S3 backup
3. Re-run transformation with fixed script
4. Verify row counts match source
5. Update data quality check to catch this in future

**Prevention:**  
- Great Expectations suite on all critical columns
- Unit tests for transformation logic
- Peer review on SQL changes

---

### Failure Mode 3: Low User Adoption
**Symptoms:**  
- < 10 active users after Phase 3
- < 5 dashboard views/week
- No marketing campaigns using funnel

**Root Causes:**  
- Poor training (users don't understand)
- Dashboard too complex
- No executive sponsorship

**Recovery Steps:**  
1. Survey users: "What's blocking you from using this?"
2. Conduct 1-on-1 training sessions
3. Simplify dashboard (remove tags, focus on 3 KPIs)
4. Get executive to mandate usage in team meetings

**Prevention:**  
- Early user testing during Phase 1
- Executive sponsorship from Day 1
- Training sessions baked into rollout plan

---

### Failure Mode 4: Security Breach
**Symptoms:**  
- Unauthorized IAM access detected
- PII data accessed by non-authorized user
- CloudTrail shows suspicious activity

**Recovery Steps:**  
1. Revoke compromised IAM keys immediately
2. Audit CloudTrail logs for all actions
3. Notify Security Officer + Legal
4. Rotate all AWS credentials
5. Conduct post-mortem, update IAM policies

**Prevention:**  
- IAM least privilege (minimize permissions)
- S3 bucket encryption (SSE)
- Regular security audits (quarterly)
- PII anonymization in dataset

## 📊 Risk Monitoring Dashboard

| Risk | Monitoring Tool | Alert Threshold | Owner |
|------|-----------------|-----------------|-------|
| Pipeline failure | CloudWatch | 1 failure in 24 hrs | Data Eng |
| Data quality | Great Expectations | 1 failed check | Data Eng |
| Query performance | Redshift logs | Avg > 5 secs | Data Eng |
| User adoption | Metabase analytics | < 10 users/week | PM |
| AWS cost | AWS Budgets | > $500/month | PM |
| Security breach | CloudTrail | Unauthorized access | Security |

## 🎯 Post-Mortem Template

```markdown
# Post-Mortem: [Incident Title]

## Timeline
- [UTC time] Incident started
- [UTC time] Detection
- [UTC time] Resolution

## Impact
- Users affected: X
- Duration: Y hours
- Data affected: Z rows

## Root Cause
[5 Whys analysis]

## Action Items
| Item | Owner | Due Date | Status |
|------|-------|----------|--------|
| Fix pipeline error | Data Eng | DD/MM | ☐ |
| Add alert for this | Data Eng | DD/MM | ☐ |
| Update documentation | PM | DD/MM | ☐ |
```

## 🔗 Related Documents
- [06_Metrics_Framework.md](06_Metrics_Framework.md)
- [17_Monitoring_Alerts.md](17_Monitoring_Alerts.md)
- [13_Responsible_AI_Security.md](13_Responsible_AI_Security.md)
