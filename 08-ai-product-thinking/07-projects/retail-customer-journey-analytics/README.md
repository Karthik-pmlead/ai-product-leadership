# 🎯 Target Retail Customer Journey Analytics Pipeline  
### From BigQuery SQL Analysis → Cloud-Native End-to-End Analytics Funnel

![Target](https://img.shields.io/badge/target-red?logo=target)  
![Python](https://img.shields.io/badge/python-3.8+-blue.svg?logo=python&logoColor=white)  
![SQL](https://img.shields.io/badge/SQL-PostgreSQL-blue?logo=postgresql&logoColor=white)  
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?logo=amazon-aws&logoColor=white)  
![Tableau](https://img.shields.io/badge/Tableau-Dashboard-E97627?logo=tableau&logoColor=white)  
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)  
![Metabase](https://img.shields.io/badge/Metabase-BI-509EE3?logo=metabase&logoColor=white)

---

## 📌 Overview

This project transforms a **SQL-based retail analytics case study** into a **full cloud-native Customer Journey Analytics Pipeline**, demonstrating end-to-end data engineering from raw CSV ingestion → cloud storage → transformation → analytics warehouse → visualization → interactive app.

**Primary Evolution:**  
`BigQuery SQL Analysis` → `AWS Cloud Data Pipeline (S3 → EC2 → Redshift → Metabase)` → `Customer Journey Funnel Analytics` → `Streamlit Application`

---

## 🏢 Business Context

**Target** is a globally renowned U.S. retailer known for exceptional guest experience. This case study focuses on **Target’s operations in Brazil**, analyzing **100,000+ orders (2016–2018)** from the **Olist Brazilian E-commerce Dataset**.

**Key Business Questions Addressed:**
- How do order trends evolve over time (monthly seasonality, yearly growth)?
- What are the delivery performance patterns across states?
- Which payment methods dominate, and how do installments affect ordering?
- How does freight cost impact customer behavior by region?
- What are the customer journey stages (Acquisition → Growth → Retention)?

---

## 🗃️ Dataset

**Source:** [Olist Brazilian E-commerce (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  
**Backup:** [Google Drive Folder](https://drive.google.com/drive/folders/1TGEc66YKbD443nslRi1bWgVd238gJCnb?usp=sharing)

**8 CSV Files:**
| File | Records | Purpose |
|------|---------|---------|
| `customers.csv` | ~100K | Customer demographics & location |
| `orders.csv` | ~100K | Order timestamps & status |
| `order_items.csv` | ~150K | Line items, pricing, shipping |
| `payments.csv` | ~120K | Payment methods & installments |
| `reviews.csv` | ~50K | Customer reviews & sentiment |
| `products.csv` | ~3K | Product attributes & categories |
| `sellers.csv` | ~3K | Seller locations |
| `geolocation.csv` | ~80K | Zip code → coordinate mapping |

### Schema Overview
![ER Diagram](https://github.com/user-attachments/assets/b2ee8610-f6fb-440d-9fa3-19a5ee128455)

---

## 🛠️ Technologies Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Data Source** | CSV (Olist) | Raw e-commerce transactions |
| **Storage** | Amazon S3 | Raw & layered data lake |
| **Compute** | Amazon EC2 | Data processing & transformations |
| **Warehouse** | Amazon Redshift | Analytics-optimized columnar DB |
| **Query Engine** | SQL (PostgreSQL-compatible) | Transformation & analysis |
| **Visualization** | Metabase, Tableau | Dashboards & BI |
| **App Layer** | Streamlit | Interactive customer journey app |
| **Orchestration** | Manual (extensible to Airflow) | Pipeline coordination |

---


---

## 🚀 Quick Start

### 1️⃣ SQL Exploratory Analysis (BigQuery/PostgreSQL)
```bash
# Follow detailed steps
docs/07_How_to_Run.md
```

**Key Analyses:**
- Data type validation (`customers` table)
- Order time range (2016–2018)
- Customer distribution by city & state
- Monthly seasonality & order trends
- Delivery time vs. estimated delivery
- Top/low freight states
- Payment method & installment patterns

### 2️⃣ Cloud Pipeline Setup (AWS)
```bash
# Follow infrastructure setup
docs/10b_Retail_Customer_Journey_Analytics_Pipeline.md
```

**Pipeline Steps:**
1. Ingest CSVs → **Amazon S3** (raw layer)
2. Process & transform → **Amazon EC2** (PySpark/SQL)
3. Load curated data → **Amazon Redshift**
4. Visualize → **Metabase dashboards**

![Metabase Dashboard 1](https://github.com/user-attachments/assets/82de50eb-82af-465a-b0de-ece4f0e37a5c)
![Metabase Dashboard 2](https://github.com/user-attachments/assets/f017a9d9-dff4-4b2a-96a6-13d50bbe5005)

### 3️⃣ Customer Journey App (Streamlit)
```bash
cd app
streamlit run ecommerceApp.py
# Opens at http://localhost:8501/
```

**App Features:**
- Login page with authentication
- Customer journey stage tracking
- Interactive funnel visualization
- DB persistence for user interactions

![Login Page](https://github.com/user-attachments/assets/253f0d73-e156-463b-9da9-65767aedadb)

---

## 📊 Customer Journey Analytics Funnel

### Defined Stages & Metrics

| Stage | Key Metrics | SQL View |
|-------|-------------|----------|
| **Acquisition** | New customers, first orders, acquisition cost | `04_customer_journey_funnel.sql` |
| **Activation** | First purchase completion, review submission | |
| **Retention** | Repeat orders, customer lifetime value | |
| **Growth** | Order frequency increase, basket size growth | |
| **Referral** | Review scores, seller ratings | |

**Full journey documentation:** `docs/06_Metrics_Framework.md`

---

## 📚 Product Management Documentation

This repo includes comprehensive **Prd Mgmt docs** for enterprise-grade product delivery:

| Document | Content |
|----------|---------|
| `01_Business_Context.md` | Problem statement, market opportunity, value prop |
| `02_Product_Scope.md` | In-scope/out-of-scope features, MVP definition |
| `03_Stakeholders.md` | Product owner, data eng, analytics, business users |
| `04_System_Overview.md` | High-level system capabilities & user flows |
| `05_Data_Strategy.md` | Data sources, ingestion, governance, quality |
| `06_Metrics_Framework.md` | North-star metric, OKRs, funnel KPIs |
| `07_How_to_Run.md` | Setup & execution instructions |
| `08_Responsible_AI_Security.md` | Privacy, bias, security risks, compliance |
| `09_System_Architecture.md` | Architecture diagrams, data flow, components |
| `10_Tradeoffs.md` | Tech choices, cost vs. performance decisions |
| `11_Rollout_Strategy.md` | Phased launch, user adoption, training |
| `12_Risk_Failure_Success_Criteria.md` | Risk matrix, success metrics, failure modes |
| `13_System_Design.md` | Detailed design, APIs, data models |
| `14_Project_Extension_Plan.md` | Future roadmap, BigQuery → Cloud extension |

---

## 🎯 Key Insights Delivered

### Order Trends
- ✅ Growing trend in orders (2016→2018)
- ✅ Clear monthly seasonality (peak in holidays)
- ✅ Peak ordering time: **Evening (19–23 hrs)**

### Delivery Performance
- ✅ Delivery time = `order_delivered_customer_date - order_purchase_timestamp`
- ✅ Estimated vs. actual delivery gap calculated per state
- ✅ Top 5 states: highest/lowest freight & delivery time

### Payment Behavior
- ✅ Month-over-month payment type distribution
- ✅ Installment patterns & impact on order value

### Regional Analysis
- ✅ Customer distribution across Brazilian states
- ✅ Month-over-month orders per state
- ✅ Order price & freight value by state

---

## 🔮 Future Improvements & Roadmap

### Phase 1: End-to-End Pipeline ✅ (Current)
- [x] CSV → S3 → EC2 → Redshift → Metabase
- [x] SQL transformation layer
- [x] Basic dashboards

### Phase 2: Customer Journey Funnel 🚧
- [ ] Define precise funnel stages in code
- [ ] Build cohort analysis queries
- [ ] Add retention & churn metrics
- [ ] Implement A/B testing framework

### Phase 3: Advanced Features 🔮
- [ ] Airflow/Dagster orchestration
- [ ] dbt for transformation modeling
- [ ] Real-time streaming (Kinesis)
- [ ] ML-powered demand forecasting
- [ ] Personalization recommendations

### Phase 4: Enterprise Scale 🔮
- [ ] BigQuery migration for GCP users
- [ ] Data mesh architecture
- [ ] Privacy-preserving analytics
- [ ] Automated data quality checks (Great Expectations)

---

## 🙏 Acknowledgments

- **Dataset:** Olist Brazilian E-commerce (Kaggle)
- **Case Study:** Target Retail Business Problem
- **Visualization Inspiration:** Tableau, Metabase best practices

---

> 💡 **Note:** This project demonstrates a **progressive evolution** from ad-hoc SQL analysis to production-grade cloud analytics pipeline, embodying modern data engineering best practices for retail customer journey intelligence.
