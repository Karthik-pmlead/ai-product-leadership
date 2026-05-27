# MLOps Checklist

**Project:** [Project Name]  
**Model:** [Model Name/Version]  
**Owner:** [Name]  
**Date:** [Date]  
**Status:** [Draft / In Progress / Complete]

---

## 1. Data Management

### 1.1 Data Quality
- [ ] Data quality issues identified
- [ ] Missing values handled
- [ ] Outliers addressed
- [ ] Data validation rules defined
- [ ] Data quality metrics tracked

### 1.2 Data Versioning
- [ ] Dataset versioned (DVC, Git LFS)
- [ ] Version metadata documented
- [ ] Version tracking automated
- [ ] Rollback capability tested

### 1.3 Data Lineage
- [ ] Data sources documented
- [ ] Data transformations tracked
- [ ] Pipeline dependencies mapped
- [ ] Data provenance recorded

### 1.4 Data Privacy & Security
- [ ] PII identified and masked
- [ ] Data encryption enabled (at rest)
- [ ] Data encryption enabled (in transit)
- [ ] Access controls configured
- [ ] Compliance requirements met (GDPR, HIPAA)

---

## 2. Model Development

### 2.1 Code Quality
- [ ] Code follows style guide
- [ ] Code reviewed (peer review)
- [ ] Unit tests written (≥80% coverage)
- [ ] Integration tests written
- [ ] CI pipeline configured

### 2.2 Experiment Tracking
- [ ] Experiments logged (MLflow, Weights & Biases)
- [ ] Hyperparameters tracked
- [ ] Metrics logged
- [ ] Artifacts versioned
- [ ] Reproducibility ensured

### 2.3 Model Training
- [ ] Training pipeline reproducible
- [ ] Random seeds fixed
- [ ] Training data versioned
- [ ] Training environment containerized
- [ ] Training logs captured

### 2.4 Model Validation
- [ ] Validation metrics meet thresholds
- [ ] Cross-validation performed
- [ ] Overfitting checked
- [ ] Bias testing completed
- [ ] Fairness evaluation done

---

## 3. Model Registry

### 3.1 Model Registration
- [ ] Model registered in model registry
- [ ] Model metadata documented
- [ ] Model versioning enabled
- [ ] Model lineage tracked
- [ ] Model artifacts stored

### 3.2 Model Metadata
- [ ] Training data version documented
- [ ] Hyperparameters recorded
- [ ] Performance metrics logged
- [ ] Author information recorded
- [ ] Creation date recorded

### 3.3 Model Approval Workflow
- [ ] Approval workflow defined
- [ ] Approvers identified
- [ ] Approval criteria documented
- [ ] Approval automation configured

---

## 4. Deployment

### 4.1 Deployment Plan
- [ ] Deployment strategy chosen (blue-green, canary)
- [ ] Rollback plan documented
- [ ] Deployment runbook created
- [ ] Deployment automation scripted
- [ ] Deployment tested in staging

### 4.2 Environment Setup
- [ ] Production environment provisioned
- [ ] Environment configuration managed (Infrastructure as Code)
- [ ] Dependencies pinned
- [ ] Environment variables configured
- [ ] Secrets managed securely

### 4.3 Model Serving
- [ ] Model serving infrastructure configured
- [ ] API endpoint created
- [ ] Authentication configured
- [ ] Rate limiting configured
- [ ] Load balancing configured

### 4.4 Deployment Verification
- [ ] Health checks implemented
- [ ] Smoke tests passed
- [ ] Integration tests passed
- [ ] Performance tests passed
- [ ] Security scan completed

---

## 5. Monitoring & Observability

### 5.1 Infrastructure Monitoring
- [ ] CPU usage monitored
- [ ] Memory usage monitored
- [ ] Disk usage monitored
- [ ] Network latency monitored
- [ ] Uptime monitored

### 5.2 Application Monitoring
- [ ] Request latency tracked
- [ ] Error rate tracked
- [ ] Throughput tracked
- [ ] Request volume tracked
- [ ] Latency percentiles (P50, P95, P99) tracked

### 5.3 Model Monitoring
- [ ] Prediction distribution tracked
- [ ] Model accuracy monitored (if ground truth available)
- [ ] Confidence scores tracked
- [ ] Input data distribution tracked
- [ ] Output data distribution tracked

### 5.4 Data Drift Detection
- [ ] Feature drift detection configured
- [ ] Target drift detection configured
- [ ] Drift threshold defined
- [ ] Drift alerts configured
- [ ] Drift remediation plan documented

### 5.5 Alerting
- [ ] Alert thresholds defined
- [ ] Alert channels configured (Slack, email, PagerDuty)
- [ ] Alert escalation defined
- [ ] Alert deduplication configured
- [ ] Alert runbooks created

---

## 6. Logging

### 6.1 Application Logging
- [ ] Structured logging enabled
- [ ] Log levels configured
- [ ] Sensitive data excluded from logs
- [ ] Log retention policy defined
- [ ] Log aggregation configured

### 6.2 Model Logging
- [ ] Input data logged (with privacy considerations)
- [ ] Predictions logged
- [ ] Confidence scores logged
- [ ] Model version logged
- [ ] Request IDs tracked

### 6.3 Audit Logging
- [ ] Model deployment logged
- [ ] Model access logged
- [ ] Configuration changes logged
- [ ] User actions logged
- [ ] Audit logs protected from tampering

---

## 7. Automation & CI/CD

### 7.1 CI Pipeline
- [ ] Code committed to version control
- [ ] Automated tests run on commit
- [ ] Code quality checks automated
- [ ] Security scans automated
- [ ] Build artifacts versioned

### 7.2 CD Pipeline
- [ ] Automated deployment pipeline
- [ ] Staging deployment automated
- [ ] Production deployment automated
- [ ] Rollback automated
- [ ] Deployment notifications configured

### 7.3 MLOps Pipeline
- [ ] Automated retraining pipeline
- [ ] Automated model evaluation
- [ ] Automated model promotion
- [ ] Automated monitoring deployment
- [ ] Pipeline orchestration configured (Airflow, Kubeflow)

---

## 8. Governance & Compliance

### 8.1 Model Card
- [ ] Model card created
- [ ] Intended use documented
- [ ] Limitations documented
- [ ] Training data documented
- [ ] Performance metrics documented
- [ ] Ethical considerations documented

### 8.2 Documentation
- [ ] Architecture documented
- [ ] API documentation complete
- [ ] Runbooks created
- [ ] Troubleshooting guide created
- [ ] Onboarding documentation created

### 8.3 Compliance
- [ ] Regulatory requirements identified
- [ ] Compliance evidence collected
- [ ] Audit trail maintained
- [ ] Data retention policy enforced
- [ ] Right to explanation supported

### 8.4 Security
- [ ] Security review completed
- [ ] Vulnerability scan completed
- [ ] Penetration test completed (if required)
- [ ] Access reviews scheduled
- [ ] Incident response plan tested

---

## 9. Testing

### 9.1 Unit Testing
- [ ] Model code tested
- [ ] Data preprocessing tested
- [ ] Post-processing tested
- [ ] Utility functions tested
- [ ] Test coverage ≥80%

### 9.2 Integration Testing
- [ ] Data pipeline tested end-to-end
- [ ] Model serving tested end-to-end
- [ ] API integration tested
- [ ] External dependencies mocked
- [ ] Error handling tested

### 9.3 Model Testing
- [ ] Accuracy tests pass
- [ ] Precision/recall tests pass
- [ ] Latency tests pass
- [ ] Load tests pass
- [ ] Adversarial tests pass

### 9.4 User Acceptance Testing
- [ ] UAT scenarios defined
- [ ] UAT testers identified
- [ ] UAT completed
- [ ] UAT feedback addressed
- [ ] UAT sign-off obtained

---

## 10. Maintenance & Operations

### 10.1 Model Maintenance
- [ ] Retraining schedule defined
- [ ] Retraining automation configured
- [ ] Model version retirement policy defined
- [ ] Model deprecation plan documented
- [ ] Maintenance window scheduled

### 10.2 Incident Management
- [ ] Incident response plan created
- [ ] Incident escalation defined
- [ ] Incident communication plan created
- [ ] Incident post-mortem process defined
- [ ] On-call rotation configured

### 10.3 Cost Management
- [ ] Infrastructure costs tracked
- [ ] Cost optimization identified
- [ ] Budget alerts configured
- [ ] Resource utilization monitored
- [ ] Cost allocation documented

---

## 11. Final Verification

### Pre-Launch Checklist
- [ ] All critical items complete
- [ ] Stakeholders approved
- [ ] Go/No-Go decision made
- [ ] Launch communication sent
- [ ] Support team ready

### Post-Launch Checklist
- [ ] Monitoring active
- [ ] Alerts configured
- [ ] Dashboard accessible
- [ ] Documentation published
- [ ] Lessons learned captured

---

## Sign-off

| Role | Name | Date | Status |
|------|------|------|--------|
| ML Engineer | [Name] | [Date] | [✓] |
| DevOps Engineer | [Name] | [Date] | [✓] |
| Product Owner | [Name] | [Date] | [✓] |
| Security Lead | [Name] | [Date] | [✓] |

---

## Notes

[Additional notes, exceptions, or special considerations]
