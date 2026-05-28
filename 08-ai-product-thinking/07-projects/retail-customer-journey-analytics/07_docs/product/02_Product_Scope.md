# 02_Product_Scope.md

## 🎯 MVP Definition (Phase 1: Cloud Pipeline)

### In Scope
| Feature | Description | Priority |
|---------|-------------|----------|
| **Data Ingestion** | CSV → Amazon S3 (raw layer) | P0 |
| **Data Transformation** | EC2 Python/SQL scripts → curated tables | P0 |
| **Data Loading** | Transformed data → Amazon Redshift | P0 |
| **SQL Analytics Layer** | 5 analytics queries (trends, delivery, payment) | P0 |
| **Metabase Dashboard** | 3 KPI dashboards (orders, freight, payment) | P0 |
| **Data Dictionary** | Column definitions, business logic | P1 |

### Out of Scope (Phase 1)
- ❌ Real-time streaming (Kinesis)
- ❌ ML models (churn prediction, demand forecasting)
- ❌ A/B testing framework
- ❌ Customer-facing app (Streamlit)
- ❌ Airflow/Dagster orchestration

## 🚀 Phase 2: Customer Journey Funnel (Q3 2026)

### In Scope
| Feature | Description | Priority |
|---------|-------------|----------|
| **Funnel SQL Views** | Acquisition, Activation, Retention, LTV queries | P0 |
| **Cohort Analysis** | 90-day retention cohorts by month | P0 |
| **Streamlit App** | Login + funnel visualization + DB persistence | P0 |
| **Funnel Dashboard** | Stage-to-stage conversion rates | P0 |
| **Churn Alerts** | Email/SNS alerts for at-risk customers | P1 |

### Out of Scope (Phase 2)
- ❌ Personalization recommendations
- ❌ Real-time funnel tracking
- ❌ Multi-touch attribution modeling

## 🔮 Phase 3: Enterprise Scale (Q1 2027)

### In Scope
- ✅ Airflow orchestration
- ✅ dbt transformation layer
- ✅ Great Expectations data quality
- ✅ BigQuery migration (GCP users)
- ✅ CI/CD với GitHub Actions
- ✅ Monitoring & alerting (CloudWatch)

## 📐 Feature Prioritization Framework

**RICE Scoring** (Reach, Impact, Confidence, Effort):

| Feature | Reach | Impact | Confidence | Effort | RICE Score | Priority |
|---------|-------|--------|------------|--------|------------|----------|
| Cloud Pipeline (S3→Redshift) | 5000 | 4 | 90% | 80 | 225 | P0 |
| Funnel SQL Views | 2000 | 3 | 80% | 40 | 120 | P0 |
| Streamlit App | 1000 | 3 | 70% | 60 | 35 | P1 |
| ML Churn Model | 2000 | 4 | 50% | 120 | 33 | P2 |
| Real-time Streaming | 5000 | 4 | 40% | 200 | 40 | P2 |

## 🚫 Boundaries & Constraints

### Technical Constraints
- **Data volume:** 100K orders (MVP) → scalable to 5M+
- **Latency:** Batch processing (daily), not real-time (Phase 1)
- **Cloud provider:** AWS (Phase 1), GCP optional (Phase 3)
- **Budget:** $500/month (EC2, Redshift, S3) for MVP

### Business Constraints
- **Timeline:** MVP in 6 weeks (Phase 1)
- **Team:** 1 PM, 1 data engineer, 1 analyst (contract)
- **Compliance:** GDPR/LGPD for customer data (Brazil)

## 📋 Acceptance Criteria (MVP)

| Criteria | Pass Condition |
|----------|----------------|
| Data Pipeline | CSV → S3 → Redshift completes in < 30 mins |
| SQL Queries | 5 analytics queries return results in < 5 secs |
| Dashboard | Metabase loads in < 3 secs, 3 KPIs visible |
| Data Quality | 0 nulls in critical columns (order_id, customer_id) |
| Documentation | README + How_to_Run.md + data_dictionary.md complete |

## 🔗 Related Documents
- [01_Business_Context.md](01_Business_Context.md)
- [03_Stakeholders.md](03_Stakeholders.md)
- [11_Rollout_Strategy.md](11_Rollout_Strategy.md)
