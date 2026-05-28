# 09_Roadmap.md

## 🗓️ 12-Month Product Roadmap

### Q2 2026 (May–July): MVP – Cloud Pipeline Foundation

| Week | Initiative | Deliverable | Success Metric |
|------|------------|-------------|----------------|
| 1–2 | AWS infra setup | S3 + EC2 + Redshift running | Pipeline completes |
| 3–4 | SQL transformations | 5 analytics queries | Queries < 5 secs |
| 5–6 | Metabase dashboards | 3 KPI dashboards | Load time < 3 secs |
| 7–8 | Data quality suite | Great Expectations config | 0 critical bugs |
| 9–10 | Documentation | README + How_to_Run + data_dict | 100% coverage |

**OKRs:**  
- Pipeline runtime < 30 mins ✅  
- Time-to-insight < 2 hours ✅  
- 0 P0 data bugs ✅  

---

### Q3 2026 (Aug–Oct): Customer Journey Funnel

| Week | Initiative | Deliverable | Success Metric |
|------|------------|-------------|----------------|
| 11–12 | Funnel SQL views | Acquisition → Retention queries | CJCR calculated |
| 13–14 | Cohort analysis | 90-day retention cohorts | Retention 42% |
| 15–16 | Streamlit app | Login + funnel viz + DB | 20 active users |
| 17–18 | Marketing pilot | 5 campaigns using funnel | Campaign lift ≥ 5% |
| 19–20 | Airflow automation | Daily DAG, 0 manual work | 99% uptime |

**OKRs:**  
- CJCR increases to 28% ✅  
- 90-day retention to 42% ✅  
- 50+ active users ✅  

---

### Q4 2026 (Nov–Jan): Scale & Optimize

| Week | Initiative | Deliverable | Success Metric |
|------|------------|-------------|----------------|
| 21–24 | CI/CD pipeline | GitHub Actions auto-test | 100% test coverage |
| 25–28 | 1M row scalability | Redshift cluster scaling | Query < 5 secs at 1M |
| 29–32 | Real-time prototype | Kinesis + Lambda stream | Sub-minute updates |
| 33–36 | Churn prediction ML | Simplified model (logistic) | AUC ≥ 0.75 |
| 37–40 | Company-wide rollout | 100+ active users | NPS ≥ 40 |

**OKRs:**  
- Handle 1M+ rows ✅  
- Sub-minute funnel updates (prototype) ✅  
- 100+ active users ✅  

---

### Q1 2027 (Feb–Apr): Enterprise Features

| Week | Initiative | Deliverable | Success Metric |
|------|------------|-------------|----------------|
| 41–44 | dbt transformation | Modular SQL models | Reusability ≥ 80% |
| 45–48 | BigQuery migration | GCP dual-stack | 0 downtime |
| 49–52 | Personalization engine | Recommendation API | CTR ≥ 8% |
| 53–56 | Multi-touch attribution | Funnel with touchpoints | ROI visibility |
| 57–60 | Production hardening | SLOs, incident response | 99.9% uptime |

**OKRs:**  
- Recommendation CTR ≥ 8% ✅  
- 99.9% uptime ✅  
- Dual-cloud support (AWS + GCP) ✅  

---

## 🎯 Epic Breakdown

### Epic 1: Cloud Data Pipeline (Q2 2026)
- ✅ S3 ingestion
- ✅ EC2 transformation
- ✅ Redshift loading
- ✅ Metabase dashboards

### Epic 2: Customer Journey Analytics (Q3 2026)
- ✅ Funnel SQL views
- ✅ Cohort analysis
- ✅ Streamlit app
- ✅ Marketing integration

### Epic 3: Automation & Scale (Q4 2026)
- ✅ Airflow orchestration
- ✅ CI/CD pipeline
- ✅ 1M row scalability
- ✅ Real-time prototype

### Epic 4: AI/ML & Enterprise (Q1 2027)
- 🚧 Churn prediction ML
- 🚧 Personalization engine
- 🚧 BigQuery migration
- 🚧 dbt transformation layer

## 📊 Resource Allocation

| Quarter | PM | Data Eng | Analyst | DevOps | Total Hours/Week |
|---------|----|----------|---------|--------|------------------|
| Q2 2026 | 20 hrs | 30 hrs | 20 hrs | 5 hrs | 75 hrs |
| Q3 2026 | 20 hrs | 25 hrs | 15 hrs | 5 hrs | 65 hrs |
| Q4 2026 | 15 hrs | 20 hrs | 10 hrs | 10 hrs | 55 hrs |
| Q1 2027 | 15 hrs | 25 hrs | 15 hrs | 10 hrs | 65 hrs |

## 🔮 Future Opportunities (Backlog)

| Initiative | Impact | Effort | Priority |
|------------|--------|--------|----------|
| Multi-touch attribution | High | High | P2 |
| Real-time personalization | High | High | P2 |
| Supplier analytics (sellers) | Medium | Low | P3 |
| Foreign market expansion (Mexico) | High | Medium | P3 |
| Voice analytics (Alexa integration) | Low | High | P4 |

## 🔗 Related Documents
- [01_Business_Context.md](01_Business_Context.md)
- [02_Product_Scope.md](02_Product_Scope.md)
- [07_Rollout_Strategy.md](07_Rollout_Strategy.md)
