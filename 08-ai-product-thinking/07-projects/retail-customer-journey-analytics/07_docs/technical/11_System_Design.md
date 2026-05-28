# 11_System_Design.md

## 🎯 Design Goals

| Goal | Requirement | Validation |
|------|-------------|------------|
| **Scalability** | Handle 1M+ rows without performance degradation | Query < 5 secs at 1M rows |
| **Reliability** | 99% uptime, 0 data loss | CloudWatch alarms, retry logic |
| **Security** | GDPR/LGPD compliance, PII protection | IAM least privilege, encryption |
| **Maintainability** | Reusable code, clear documentation | Code review, 100% doc coverage |
| **Cost Efficiency** | < $500/month for MVP | AWS Cost Explorer monthly review |

## 🏛️ Architectural Patterns

### Pattern 1: Lambda Architecture (Batch + Speed Layer)
```
Batch Layer (Primary):
CSV → S3 → EC2 → Redshift → Metabase/Streamlit

Speed Layer (Future):
Kinesis → Lambda → Redshift Streaming → Real-time dashboard
```

**Why Lambda?**
- Batch: Accurate, complete data (daily)
- Speed: Near real-time insights (future phase)

### Pattern 2: Layered Data Lake
- Raw Layer (immutable) → Staging Layer (cleaned) → Curated Layer (aggregates)


**Why layered?**
- Immutable raw: Audit trail, easy reprocessing
- Cleaned staging: Reusable across teams
- Curated aggregates: Fast query performance

### Pattern 3: API-First Design (Future)

- Streamlit App → Redshift (direct) [Current]
- Streamlit App → FastAPI → Redshift [Future]

**Why API-first?**
- Decouples app from database
- Enables mobile app integration
- Supports A/B testing framework

## 🗄️ Data Model Design

### Star Schema (Analytics Warehouse)
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


### Table Definitions

#### `dim_customers`
```sql
CREATE TABLE dim_customers (
  customer_id VARCHAR(50) PRIMARY KEY,
  customer_unique_id VARCHAR(50),
  customer_zip_code_prefix INTEGER,
  customer_city VARCHAR(100),
  customer_state VARCHAR(50),
  first_order_date DATE,
  total_orders INTEGER,
  total_spend DECIMAL(10,2)
);
```

#### `fact_order_items`
```sql
CREATE TABLE fact_order_items (
  order_item_id INTEGER,
  order_id VARCHAR(50) REFERENCES dim_orders(order_id),
  product_id VARCHAR(50) REFERENCES dim_products(product_id),
  customer_id VARCHAR(50) REFERENCES dim_customers(customer_id),
  date_key INTEGER REFERENCES dim_time(date_key),
  price DECIMAL(10,2),
  freight_value DECIMAL(10,2),
  total_value DECIMAL(10,2)
)
DISTKEY(order_id)
SORTKEY(date_key);
```

## 🔌 API Design (Future Phase)

### REST API Endpoints

```yaml
/openapi.yaml

paths:
  /api/v1/funnel:
    get:
      summary: Get funnel conversion rates
      parameters:
        - name: start_date
          in: query
          schema:
            type: string
            format: date
        - name: end_date
          in: query
          schema:
            type: string
            format: date
      responses:
        200:
          description: Funnel data
          content:
            application/json:
              schema:
                type: object
                properties:
                  stages:
                    type: array
                    items:
                      type: object
                      properties:
                        stage_name: string
                        count: integer
                        conversion_rate: number
```

### Sample Response
```json
{
  "stages": [
    {"stage_name": "Acquisition", "count": 10000, "conversion_rate": 1.0},
    {"stage_name": "Activation", "count": 4500, "conversion_rate": 0.45},
    {"stage_name": "Retention", "count": 3200, "conversion_rate": 0.32},
    {"stage_name": "Growth", "count": 2100, "conversion_rate": 0.21},
    {"stage_name": "Referral", "count": 1800, "conversion_rate": 0.18}
  ]
}
```

## 🧩 Component Interaction Diagram
```
┌────────────┐ ┌────────────┐ ┌────────────┐
│ User │────▶│ Streamlit │────▶│ FastAPI │
│ (Browser) │ │ App │ │ (Future) │
└────────────┘ └────────────┘ └─────┬──────┘
│
▼
┌────────────┐
│ Redshift │
│ (Database) │
└────────────┘
```


## ⚙️ Configuration Management

### Environment Variables (`.env`)
```bash
# AWS
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_REGION=us-east-1

# S3
S3_RAW_BUCKET=retail-cj-raw-prod
S3_CURATED_BUCKET=retail-cj-curated-prod

# Redshift
REDSHIFT_HOST=cluster.xxx.us-east-1.redshift.amazonaws.com
REDSHIFT_PORT=5439
REDSHIFT_DB=analytics
REDSHIFT_USER=analyst
REDSHIFT_PASSWORD=xxx

# Streamlit
STREAMLIT_SECRET_KEY=xxx
```

### Config File (`config.py`)
```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    S3_RAW_BUCKET = os.getenv("S3_RAW_BUCKET")
    S3_CURATED_BUCKET = os.getenv("S3_CURATED_BUCKET")
    REDSHIFT_HOST = os.getenv("REDSHIFT_HOST")
    REDSHIFT_PORT = int(os.getenv("REDSHIFT_PORT", 5439))
    REDSHIFT_DB = os.getenv("REDSHIFT_DB", "analytics")
```

## 🧪 Testing Strategy

### Unit Tests
```python
# tests/unit/test_sql_transformations.py
def test_delivery_time_calculation():
    df = pd.DataFrame({
        'order_purchase_timestamp': ['2023-01-01'],
        'order_delivered_customer_date': ['2023-01-05']
    })
    df['delivery_time'] = compute_delivery_time(df)
    assert df['delivery_time'].iloc == 4
```

### Integration Tests
```python
# tests/integration/test_s3_to_redshift.py
def test_pipeline_end_to_end():
    upload_to_s3('test.csv')
    run_etl()
    row_count = query_redshift("SELECT COUNT(*) FROM stg_orders")
    assert row_count > 0
```

### Data Quality Tests
```python
# tests/data_quality/test_great_expectations.py
expect_column_values_to_not_be_null("stg_orders", "order_id")
expect_column_values_to_be_unique("stg_orders", "order_id")
```

## 🔗 Related Documents
- [10_System_Architecture.md](10_System_Architecture.md)
- [14_Data_Model.md](14_Data_Model.md)
- [08_Risk_Failure_Success_Criteria.md](08_Risk_Failure_Success_Criteria.md)
