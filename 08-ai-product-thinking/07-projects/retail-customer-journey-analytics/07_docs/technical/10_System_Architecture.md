# 10_System_Architecture.md

## 🏗️ High-Level Architecture Diagram
```
┌─────────────────────────────────────────────────────────────────┐
│ RETAIL CUSTOMER JOURNEY ANALYTICS │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ CSV Files │─────▶│ Amazon S3 │─────▶│ Amazon EC2 │
│ (Olist) │ │ (Raw) │ │ (ETL Script)│
└──────────────┘ └──────────────┘ └──────────────┘
│
▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ Streamlit │◀─────│ Amazon │◀─────│ Amazon S3 │
│ App (Funnel) │ │ Redshift │ │ (Curated) │
└──────────────┘ │ (Warehouse) │ └──────────────┘
└──────────────┘
│
▼
┌──────────────┐
│ Metabase │
│ (Dashboard) │
└──────────────┘
```


## 🔧 Component Details

### 1. Data Source (CSV Files)
- **Type:** Static dataset (Olist Brazilian E-commerce)
- **Volume:** 100K orders, 8 CSV files (~50 MB)
- **Format:** Comma-separated, UTF-8
- **Update Frequency:** One-time (MVP), daily batch (future)

### 2. Amazon S3 (Raw Layer)
- **Purpose:** Immutable raw data storage
- **Bucket Name:** `retail-cj-raw-[env]`
- **Encryption:** SSE-S3 (AWS managed)
- **Lifecycle:** Move to Glacier after 2 years
- **Access:** IAM role (EC2 write-only, analyst read-only)

### 3. Amazon EC2 (ETL Compute)
- **Instance Type:** t3.medium (2 vCPU, 4 GB RAM)
- **OS:** Amazon Linux 2
- **Scripts:** 
  - `ingest_to_s3.py` (CSV → S3)
  - `transform_ec2.py` (clean & aggregate)
  - `load_redshift.py` (COPY to warehouse)
- **Dependencies:** boto3, psycopg2, pandas
- **Runtime:** ~22 minutes per batch

### 4. Amazon S3 (Curated Layer)
- **Purpose:** Transformed, analytics-ready data
- **Bucket Name:** `retail-cj-curated-[env]`
- **Format:** Parquet (columnar, compressed)
- **Partitioning:** By date (year/month/day)
- **Access:** Redshift COPY permission

### 5. Amazon Redshift (Analytics Warehouse)
- **Cluster Type:** dc2.large (2 nodes, 16 GB RAM)
- **Schema:** 
  - `stg_*` (staging tables)
  - `analytics_*` (aggregates)
  - `analytics_funnel` (journey metrics)
- **Distribution:** KEY(order_id)
- **Sort Key:** order_purchase_timestamp
- **Query Performance:** < 5 secs for 100K rows

### 6. Metabase (BI Dashboard)
- **Deployment:** EC2 instance (metabase/metabase Docker)
- **Connection:** Redshift JDBC
- **Dashboards:**
  - Retail KPI Dashboard (orders, freight, payment)
  - Funnel Conversion Dashboard (stage-to-stage)
- **Refresh:** Daily batch (8 AM IST)
- **Users:** 50+ (internal)

### 7. Streamlit App (Customer Journey)
- **Deployment:** AWS Elastic Beanstalk (Python 3.9)
- **File:** `ecommerceApp.py`
- **Pages:**
  - Login (authentication)
  - Acquisition Funnel
  - Retention Cohorts
  - Dashboards
- **Database:** Redshift (via psycopg2)
- **Sessions:** PostgreSQL (user auth)

## 🔄 Data Flow (Step-by-Step)

### Step 1: Ingestion (CSV → S3 Raw)
```python
# ingest_to_s3.py
import boto3

s3 = boto3.client('s3')
for csv_file in ['customers.csv', 'orders.csv', ...]:
    s3.upload_file(csv_file, 'retail-cj-raw', f'raw/{csv_file}')
```

### Step 2: Transformation (EC2)
```python
# transform_ec2.py
import pandas as pd

df = pd.read_csv('s3://retail-cj-raw/raw/orders.csv')
df['order_date'] = pd.to_datetime(df['order_purchase_timestamp'])
df['delivery_time'] = (df['order_delivered_customer_date'] - 
                       df['order_purchase_timestamp']).dt.days
df.to_parquet('s3://retail-cj-curated/stg_orders.parquet')
```

### Step 3: Loading (S3 → Redshift)
```sql
-- load_redshift.sql
COPY stg_orders FROM 's3://retail-cj-curated/stg_orders.parquet'
IAM_ROLE 'arn:aws:iam::123456789:role/RedshiftS3Role'
FORMAT AS PARQUET;
```

### Step 4: Analytics (Redshift → Metabase)
```sql
-- analytics_order_trends.sql
SELECT 
  DATE_TRUNC('month', order_purchase_timestamp) AS month,
  COUNT(*) AS orders,
  SUM(price) AS revenue
FROM stg_orders
GROUP BY 1
ORDER BY 1;
```

### Step 5: Funnel (Redshift → Streamlit)
```python
# ecommerceApp.py (funnel page)
import streamlit as st
import psycopg2

conn = psycopg2.connect(host='redshift-cluster.xxx.us-east-1.redshift.amazonaws.com')
cur = conn.cursor()
cur.execute("SELECT stage, count FROM analytics_funnel")
funnel_data = cur.fetchall()
st.bar_chart(funnel_data)
```

## 🔒 Security Architecture

### Network Security
- **VPC:** Private subnet for Redshift, EC2
- **Security Groups:** 
  - EC2 → S3 (open)
  - Redshift → EC2 (port 5439)
  - Metabase → Redshift (port 5439)
- **No public access** to Redshift

### Data Encryption
- **At rest:** S3 SSE, Redshift AES-256
- **In transit:** HTTPS (TLS 1.2+), Redshift SSL
- **Keys:** AWS KMS (managed)

### Access Control
- **IAM Roles:** Least privilege
  - EC2: S3 read/write, CloudWatch logs
  - Redshift: S3 COPY, schema access
- **Database Users:** 
  - analyst: Read-only on analytics_*
  - engineer: Read/write on stg_*
  - admin: Full access

## 📊 Scalability Plan

| Component | Current | Scale Target | Scaling Strategy |
|-----------|---------|--------------|------------------|
| S3 | 50 MB | 500 GB | Infinite (no scaling needed) |
| EC2 | t3.medium | t3.xlarge | Vertical (upgrade instance) |
| Redshift | dc2.large (2) | dc2.xlarge (4) | Horizontal (add nodes) |
| Metabase | 1 EC2 | 2 EC2 + ALB | Horizontal (auto-scaling) |
| Streamlit | 1 EB | 3 EB + ALB | Horizontal (auto-scaling) |

## 🔗 Related Documents
- [04_System_Overview.md](04_System_Overview.md)
- [11_System_Design.md](11_System_Design.md)
- [14_Data_Model.md](14_Data_Model.md)
