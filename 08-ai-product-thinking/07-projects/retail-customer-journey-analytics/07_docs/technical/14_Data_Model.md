# 14_Data_Model.md

## 🎯 Overview

This document defines the **data model** for the Retail Customer Journey Analytics Pipeline, including:
- **Star schema** for analytics warehouse
- **Table definitions** (columns, types, keys)
- **Relationships** (foreign keys)
- **Business logic** for derived columns
- **Funnel data model** (customer journey stages)

**Database:** Amazon Redshift (PostgreSQL-compatible)  
**Schema:** `analytics` (production), `staging` (temporary)  
**Volume:** 100K orders (MVP) → scalable to 1B+ rows

---

## 🏗️ Star Schema Diagram
```
 ┌──────────────────┐
│ dim_customers │
│ (customer_id PK)│
└────────┬─────────┘
│
┌──────────────┼──────────────┐
│ │ │
┌─────────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
│ dim_products │ │dim_orders │ │ dim_time │
│ (product_id PK)│ │(order_id PK)│ │ (date PK) │
└────────────────┘ └─────┬──────┘ └────────────┘
│
┌────────▼─────────┐
│ fact_order_items│
│ (order_item_id) │
│ → order_id FK │
│ → product_id FK │
│ → customer_id FK│
│ → date_fk │
└──────────────────┘
```


---

## 📊 Dimension Tables

### `dim_customers`

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `customer_id` | VARCHAR(50) | Unique customer identifier | **PK**, NOT NULL |
| `customer_unique_id` | VARCHAR(50) | Anonymized customer ID | UNIQUE |
| `customer_zip_code_prefix` | INTEGER | First 5 digits of zip code | |
| `customer_city` | VARCHAR(100) | Customer city (lowercase) | |
| `customer_state` | VARCHAR(50) | State acronym (e.g., SP) | |
| `first_order_date` | DATE | Date of first order | |
| `total_orders` | INTEGER | Total orders placed | ≥ 0 |
| `total_spend` | DECIMAL(10,2) | Total amount spent (BRL) | ≥ 0 |
| `customer_since Days` | INTEGER | Days since first order | ≥ 0 |
| `churn_risk_score` | DECIMAL(3,2) | ML-predicted churn risk (0–1) | 0.0–1.0 (future) |

**Business Logic:**
- `first_order_date` = MIN(order_purchase_timestamp) per customer
- `total_orders` = COUNT(order_id) per customer
- `total_spend` = SUM(price + freight_value) per customer

**Snapshot Query:**
```sql
CREATE TABLE dim_customers AS
SELECT 
  c.customer_id,
  c.customer_unique_id,
  c.customer_zip_code_prefix,
  LOWER(c.customer_city) AS customer_city,
  UPPER(c.customer_state) AS customer_state,
  MIN(o.order_purchase_timestamp)::DATE AS first_order_date,
  COUNT(o.order_id) AS total_orders,
  SUM(oi.price + oi.freight_value) AS total_spend,
  CURRENT_DATE - MIN(o.order_purchase_timestamp)::DATE AS customer_since_days
FROM stg_customers c
JOIN stg_orders o ON c.customer_id = o.customer_id
JOIN stg_order_items oi ON o.order_id = oi.order_id
GROUP BY 1, 2, 3, 4, 5;
```

---

### `dim_products`

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `product_id` | VARCHAR(50) | Unique product identifier | **PK**, NOT NULL |
| `product_category_name` | VARCHAR(100) | Product category (Portuguese) | |
| `product_category_english` | VARCHAR(100) | Translated category (future) | |
| `product_name_length` | INTEGER | Length of product name | ≥ 0 |
| `product_description_length` | INTEGER | Description length (chars) | ≥ 0 |
| `product_photos_qty` | INTEGER | Number of photos | 0–10 |
| `product_weight_g` | INTEGER | Weight in grams | > 0 |
| `product_length_cm` | INTEGER | Length in cm | > 0 |
| `product_width_cm` | INTEGER | Width in cm | > 0 |
| `product_height_cm` | INTEGER | Height in cm | > 0 |
| `avg_price` | DECIMAL(10,2) | Average selling price (BRL) | ≥ 0 |
| `total_units_sold` | INTEGER | Total units sold | ≥ 0 |

**Business Logic:**
- `avg_price` = AVG(price) from fact_order_items
- `total_units_sold` = SUM(order_item_id) per product

---

### `dim_orders`

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `order_id` | VARCHAR(50) | Unique order identifier | **PK**, NOT NULL |
| `customer_id` | VARCHAR(50) | FK → dim_customers | FK, NOT NULL |
| `order_status` | VARCHAR(20) | Order status | IN ('delivered', 'shipped', ...) |
| `order_purchase_timestamp` | TIMESTAMP | Purchase date (UTC) | NOT NULL |
| `order_approved_at` | TIMESTAMP | Payment approval (UTC) | |
| `order_delivered_carrier_date` | DATE | Carrier pickup date | |
| `order_delivered_customer_date` | DATE | Delivery date to customer | |
| `order_estimated_delivery_date` | DATE | Estimated delivery (UTC) | |
| `delivery_time_days` | INTEGER | Actual delivery time | = delivered - purchase |
| `estimated_vs_actual_gap` | INTEGER | Estimated - actual (days) | negative = early |
| `total_price` | DECIMAL(10,2) | Order total (price + freight) | ≥ 0 |
| `payment_type` | VARCHAR(20) | Primary payment method | credit_card, debit, etc. |
| `payment_installments` | INTEGER | Number of installments | ≥ 1 |
| `state` | VARCHAR(50) | Customer state | FK → dim_customers.state |

**Business Logic:**
```sql
delivery_time_days = order_delivered_customer_date - order_purchase_timestamp
estimated_vs_actual_gap = order_estimated_delivery_date - order_delivered_customer_date
```

---

### `dim_time`

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `date_key` | INTEGER | Date in YYYYMMDD format | **PK**, NOT NULL |
| `date` | DATE | Actual date | NOT NULL |
| `day_of_week` | INTEGER | 1=Mon, 7=Sun | 1–7 |
| `day_name` | VARCHAR(10) | Monday, Tuesday, ... | |
| `month` | INTEGER | 1–12 | 1–12 |
| `month_name` | VARCHAR(10) | January, February, ... | |
| `quarter` | INTEGER | 1–4 | 1–4 |
| `year` | INTEGER | 2016, 2017, 2018 | |
| `is_weekend` | BOOLEAN | Saturday/Sunday | TRUE/FALSE |
| `is_holiday` | BOOLEAN | Brazilian holiday (future) | TRUE/FALSE |

**Populate Query:**
```sql
CREATE TABLE dim_time AS
SELECT 
  EXTRACT(YEAR FROM d)::INT * 10000 + EXTRACT(MONTH FROM d)::INT * 100 + EXTRACT(DAY FROM d)::INT AS date_key,
  d AS date,
  EXTRACT(DOW FROM d) + 1 AS day_of_week,
  TO_CHAR(d, 'Day') AS day_name,
  EXTRACT(MONTH FROM d) AS month,
  TO_CHAR(d, 'Month') AS month_name,
  EXTRACT(QUARTER FROM d) AS quarter,
  EXTRACT(YEAR FROM d) AS year,
  CASE WHEN EXTRACT(DOW FROM d) IN (0, 6) THEN TRUE ELSE FALSE END AS is_weekend
FROM generate_series('2016-01-01'::DATE, '2020-12-31'::DATE, '1 day'::INTERVAL) AS d;
```

---

## 📈 Fact Tables

### `fact_order_items`

| Column | Type | Description | Constraints |
|--------|------|-------------|-------------|
| `order_item_id` | INTEGER | Line item ID within order | **PK**, NOT NULL |
| `order_id` | VARCHAR(50) | FK → dim_orders | FK, NOT NULL |
| `product_id` | VARCHAR(50) | FK → dim_products | FK, NOT NULL |
| `customer_id` | VARCHAR(50) | FK → dim_customers | FK, NOT NULL |
| `date_key` | INTEGER | FK → dim_time | FK, NOT NULL |
| `price` | DECIMAL(10,2) | Product price (BRL) | > 0 |
| `freight_value` | DECIMAL(10,2) | Shipping fee (BRL) | ≥ 0 |
| `total_value` | DECIMAL(10,2) | price + freight | > 0 |
| `payment_value` | DECIMAL(10,2) | Payment amount (BRL) | > 0 |
| `is_first_order_item` | BOOLEAN | First item in customer's first order | TRUE/FALSE |

**Distribution & Sort Keys:**
```sql
DISTKEY(order_id)
SORTKEY(date_key)
```

**Business Logic:**
```sql
total_value = price + freight_value
is_first_order_item = (order_id = FIRST_ORDER(customer_id))
```

---

## 🎯 Customer Journey Funnel Data Model

### `analytics_funnel`

| Column | Type | Description | Business Logic |
|--------|------|-------------|----------------|
| `customer_id` | VARCHAR(50) | FK → dim_customers | PK for funnel |
| `cohort_date` | DATE | First order month | DATE_TRUNC('month', first_order_date) |
| `stage_acquisition` | BOOLEAN | Account created | customer_id exists |
| `stage_activation` | BOOLEAN | First order delivered | order_status = 'delivered' |
| `stage_retention` | BOOLEAN | Second order ≤ 90 days | COUNT(orders) ≥ 2 AND days_between ≤ 90 |
| `stage_growth` | BOOLEAN | ≥ 3 orders/quarter | COUNT(orders) ≥ 3 in 90 days |
| `stage_referral` | BOOLEAN | Review score ≥ 4 | MAX(review_score) ≥ 4 |
| `stages_completed` | INTEGER | Count of TRUE stages | SUM(CASE WHEN stage_X THEN 1 ELSE 0 END) |
| `conversion_stage_1_2` | BOOLEAN | Acq → Activ conversion | stage_acquisition AND stage_activation |
| `conversion_stage_2_3` | BOOLEAN | Activ → Reten conversion | stage_activation AND stage_retention |
| `ltv_brl` | DECIMAL(10,2) | Customer LTV | SUM(total_value) |
| `days_to_first_order` | INTEGER | Account → first order | first_order_date - account_date |
| `churned` | BOOLEAN | No order in 90 days | MAX(order_date) + 90 < CURRENT_DATE |

**Funnel Conversion Calculation:**
```sql
SELECT 
  COUNT(DISTINCT CASE WHEN stage_acquisition THEN customer_id END) AS acquisition_count,
  COUNT(DISTINCT CASE WHEN stage_activation THEN customer_id END) AS activation_count,
  COUNT(DISTINCT CASE WHEN stage_retention THEN customer_id END) AS retention_count,
  COUNT(DISTINCT CASE WHEN stage_growth THEN customer_id END) AS growth_count,
  COUNT(DISTINCT CASE WHEN stage_referral THEN customer_id END) AS referral_count,
  
  activation_count * 1.0 / acquisition_count AS acq_to_activ_rate,
  retention_count * 1.0 / activation_count AS activ_to_retention_rate,
  growth_count * 1.0 / retention_count AS retention_to_growth_rate,
  referral_count * 1.0 / growth_count AS growth_to_referral_rate,
  
  referral_count * 1.0 / acquisition_count AS overall_cjcr  -- North-Star Metric
FROM analytics_funnel
WHERE cohort_date >= '2026-01-01';
```

---

## 🔗 Relationships (ERD)
```
dim_customers (1) ----< (N) dim_orders
dim_customers (1) ----< (N) fact_order_items
dim_products (1) ----< (N) fact_order_items
dim_orders (1) ----< (N) fact_order_items
dim_time (1) ----< (N) fact_order_items
dim_time (1) ----< (N) dim_orders
```

**Foreign Key Constraints:**
```sql
ALTER TABLE dim_orders ADD CONSTRAINT fk_orders_customer 
  FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id);

ALTER TABLE fact_order_items ADD CONSTRAINT fk_items_order 
  FOREIGN KEY (order_id) REFERENCES dim_orders(order_id);

ALTER TABLE fact_order_items ADD CONSTRAINT fk_items_product 
  FOREIGN KEY (product_id) REFERENCES dim_products(product_id);

ALTER TABLE fact_order_items ADD CONSTRAINT fk_items_customer 
  FOREIGN KEY (customer_id) REFERENCES dim_customers(customer_id);

ALTER TABLE fact_order_items ADD CONSTRAINT fk_items_date 
  FOREIGN KEY (date_key) REFERENCES dim_time(date_key);
```

---

## 📊 Data Quality Rules

| Table | Column | Rule | Action on Failure |
|-------|--------|------|-------------------|
| `dim_customers` | customer_id | NOT NULL, UNIQUE | Fail pipeline |
| `dim_orders` | order_id | NOT NULL, UNIQUE | Fail pipeline |
| `fact_order_items` | order_id | FK exists in dim_orders | Fail pipeline |
| `fact_order_items` | price | > 0 | Warn, log anomaly |
| `analytics_funnel` | stages_completed | 0–5 | Fail if > 5 |
| All tables | critical columns | 0 NULLs | Fail pipeline |

**Great Expectations Check:**
```yaml
expectations:
  - expect_column_values_to_not_be_null:
      column: order_id
      table: fact_order_items
  - expect_column_values_to_be_unique:
      column: order_id
      table: dim_orders
  - expect_column_values_to_be_in_set:
      column: order_status
      table: dim_orders
      value_set: ['delivered', 'shipped', 'canceled', 'approved']
```

---

## 🔗 Related Documents
- [10_System_Architecture.md](10_System_Architecture.md)
- [11_System_Design.md](11_System_Design.md)
- [05_Data_Strategy.md](05_Data_Strategy.md)
