# 05_Data_Strategy.md

## 🗃️ Data Sources

| Source | Type | Volume | Frequency | Owner |
|--------|------|--------|-----------|-------|
| **Olist CSV (Kaggle)** | Static dataset | 100K orders, 8 files | One-time (MVP) | Data Team |
| **Amazon S3 (Raw)** | Cloud storage | 50 MB | Incremental uploads | Data Engineer |
| **Amazon Redshift** | Analytics warehouse | 100M rows/day (future) | Daily batch | Data Engineer |
| **Metabase** | BI tool | Embedded queries | Real-time | Data Analyst |
| **Streamlit App** | User interactions | 1K sessions/month | Real-time | Product Team |

## 🔄 Data Ingestion Strategy

### Phase 1: Batch (MVP)
Daily batch job:
```
    CSV files → S3 raw bucket (manual upload or script)

    EC2 trigger: python ingest_to_s3.py

    Verify: Row counts match expected
```
  Airflow DAG:
```
    Sensor: New files in S3

    Task: Transform & load to Redshift

    Task: Run data quality checks

    Task: Notify Slack if failures
```
  ### Phase 3: Real-time (Q1 2027)

  
## 🧹 Data Transformation Layer

### Staging Tables (Raw → Clean)
| Table | Source | Transformation |
|-------|--------|----------------|
| `stg_customers` | customers.csv | Lowercase city/state, valid zip codes |
| `stg_orders` | orders.csv | Parse timestamps (UTC → local), filter invalid status |
| `stg_order_items` | order_items.csv | Join with products, calculate line total |
| `stg_payments` | payments.csv | Normalize payment_type names |
| `stg_reviews` | reviews.csv | Sentiment analysis (future), filter empty reviews |

### Analytics Tables (Staging → Aggregates)
| Table | Purpose | Key Metrics |
|-------|---------|-------------|
| `analytics_order_trends` | Monthly order counts | Orders, revenue, freight by month/state |
| `analytics_delivery_perf` | Delivery performance | Delivery time, estimated vs actual gap |
| `analytics_payment_behavior` | Payment analysis | Payment type share, installment avg |
| `analytics_funnel` | Customer journey | Stage counts, conversion rates, LTV |

### Data Quality Rules

| Rule | Threshold | Action on Failure |
|------|-----------|-------------------|
| **Null check (critical columns)** | 0 nulls in order_id, customer_id | Fail pipeline, alert |
| **Unique constraint** | All order_id unique | Fail pipeline, alert |
| **Range check (price)** | Price > 0, < 10000 BRL | Warn, log anomaly |
| **Referential integrity** | All customer_id exist in customers | Fail pipeline, alert |
| **Freshness** | Pipeline runs daily by 6 AM IST | Warn, retry once |

## 🔒 Data Governance

### Ownership
| Data Domain | Owner | Steward |
|-------------|-------|---------|
| **Customer Data** | Product Owner | Data Analyst |
| **Order Data** | Data Engineer | Data Analyst |
| **Payment Data** | Finance Lead | Data Engineer |
| **Product Data** | Merchandising Lead | Data Analyst |

### Access Control
| Role | Access Level | Tables |
|------|--------------|--------|
| **Data Analyst** | Read-only | analytics_*, stg_* |
| **Data Engineer** | Read/Write | stg_*, raw_* |
| **Product Manager** | Read-only (aggregates) | analytics_funnel, dashboards |
| **Executive** | Read-only (KPIs) | Metabase dashboards only |

### Retention Policy
| Data Type | Retention Period | Archival |
|-----------|------------------|----------|
| **Raw CSV** | 2 years | S3 Glacier |
| **Staging Tables** | 6 months | Delete |
| **Analytics Tables** | 5 years | Redshift snapshot |
| **User session logs** | 1 year | CloudWatch → S3 |

## 📊 Data Quality Framework

### Tools
- **Great Expectations:** Automated data quality suite
- **CloudWatch Alarms:** Pipeline runtime, error rates
- **Metabase Alerts:** KPI threshold breaches

### Metrics
| Metric | Target | Measurement |
|--------|--------|-------------|
| Data completeness | 99.9% | % non-null in critical columns |
| Data accuracy | 99.5% | % rows matching source |
| Pipeline freshness | < 24 hrs | Time since last successful run |
| Query performance | < 5 secs | Avg Redshift query time |

## 🚀 Data Roadmap

| Quarter | Initiative | Impact |
|---------|------------|--------|
| **Q2 2026** | Batch pipeline (MVP) | 10x faster insights |
| **Q3 2026** | Automated Airflow DAG | 99% uptime, 0 manual work |
| **Q4 2026** | Great Expectations suite | 90% reduction in data bugs |
| **Q1 2027** | Real-time streaming | Sub-minute funnel updates |

## 🔗 Related Documents
- [04_System_Overview.md](04_System_Overview.md)
- [14_Data_Model.md](14_Data_Model.md)
- [17_Monitoring_Alerts.md](17_Monitoring_Alerts.md)
