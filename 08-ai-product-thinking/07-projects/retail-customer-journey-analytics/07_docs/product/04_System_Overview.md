# 04_System_Overview.md

## 🌐 High-Level System Capabilities

| Capability | Description | User Benefit |
|------------|-------------|--------------|
| **Data Ingestion** | Upload CSV → Amazon S3 (raw layer) | No manual data copying, automated pipeline |
| **Data Transformation** | Python/SQL scripts clean & aggregate data | Analytics-ready tables in < 30 mins |
| **Analytics Warehouse** | Amazon Redshift stores curated data | Fast queries (< 5 secs) on 100K+ orders |
| **BI Dashboards** | Metabase shows KPIs (orders, freight, payment) | Self-service insights for non-technical users |
| **Customer Journey Funnel** | Track Acquisition → Activation → Retention → LTV | Identify drop-off points, optimize conversion |
| **Streamlit App** | Interactive app with login + funnel viz | Product managers explore funnels without SQL |

## 👣 User Flows

### Flow 1: Data Analyst → Metabase Dashboard
1. Analyst logs into Metabase
2. Opens "Retail KPI Dashboard"
3. Views: Monthly orders, top states by freight, payment method distribution
4. Filters by state/date range
5. Exports chart → shares with marketing team

### Flow 2: Product Manager → Streamlit Funnel App
1. PM logs into Streamlit app (email/password)
2. Selects "Acquisition Funnel" tab
3. Views: New customers → First order → Review submission → Repeat purchase
4. Clicks on drop-off stage → sees cohort breakdown
5. Exports insight → adds to sprint review deck

### Flow 3: Data Engineer → Pipeline Monitoring
1. Engineer logs into AWS Console
2. Checks CloudWatch logs for EC2 ETL job
3. Sees: Job completed in 22 mins, 0 errors
4. Checks Redshift table row counts → matches expected
5. Sets up alert: If job fails → SNS notification


## 🎯 Key Users & Jobs-to-be-Done

| User | Job-to-be-Done | Outcome |
|------|----------------|---------|
| **Data Analyst** | "I need to quickly answer business questions about orders" | 10x faster insights vs. manual SQL |
| **Product Manager** | "I need to see where customers drop off in the funnel" | 15% conversion uplift by fixing drop-offs |
| **Marketing Manager** | "I need customer segments for email campaigns" | 20% higher email open rates |
| **Data Engineer** | "I need a reliable pipeline that doesn't break" | 99% uptime, 0 manual intervention |
| **Executive** | "I need to see retention trends for quarterly review" | Data-driven strategy decisions |

## 📊 System Boundaries

### Inside Scope (This System)
- ✅ CSV → S3 → EC2 → Redshift pipeline
- ✅ SQL transformation layer (staging → analytics → funnel)
- ✅ Metabase dashboards (3 KPIs)
- ✅ Streamlit app (login + funnel viz)
- ✅ Data dictionary + documentation

### Outside Scope (External Systems)
- ❌ Customer-facing e-commerce website (Target Brazil)
- ❌ CRM system (Salesforce)
- ❌ Email marketing platform (HubSpot)
- ❌ Payment gateway (Stripe/PayPal)
- ❌ Logistics system (shipping carriers)

**Note:** Future phases may integrate with external systems via APIs.

## 🔗 Data Flow Summary
```
[CSV Files]
↓ (upload)
[Amazon S3 - Raw]
↓ (EC2 ETL script)
[Amazon S3 - Curated]
↓ (COPY command)
[Amazon Redshift - Analytics Tables]
↓ (SQL queries)
[Metabase Dashboard] AND [Streamlit App]

```

## 🛡️ Security & Privacy Overview

- **Data encryption:** At rest (S3 SSE), in transit (HTTPS)
- **Access control:** IAM roles (minimize permissions), Redshift user roles
- **PII handling:** Customer names/emails anonymized in dataset
- **Compliance:** LGPD (Brazil), GDPR (EU) ready
- **Audit trail:** CloudWatch logs for all pipeline runs

## 🔗 Related Documents
- [05_Data_Strategy.md](05_Data_Strategy.md)
- [10_System_Architecture.md](10_System_Architecture.md)
- [13_Responsible_AI_Security.md](13_Responsible_AI_Security.md)
