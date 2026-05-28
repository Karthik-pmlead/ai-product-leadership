# 06_Metrics_Framework.md

## 🎯 North-Star Metric

**Customer Journey Completion Rate (CJCR)**  
= (Customers who complete all 5 journey stages) / (Total new customers)

**Target:** 28% (from baseline 22%) within 6 months

### Journey Stages Definition
| Stage | Definition | Success Criteria |
|-------|------------|------------------|
| **1. Acquisition** | New customer creates account + first browse | Customer record exists in `customers` |
| **2. Activation** | First order placed + payment成功 | `orders.order_status = 'delivered'` |
| **3. Retention** | Second order within 90 days | Repeat customer in cohort analysis |
| **4. Growth** | Order frequency increases (≥3 orders/quarter) | LTV > R$ 400 |
| **5. Referral** | Review submitted (score ≥ 4) + seller rating ≥ 4.5 | `reviews.review_score ≥ 4` |

## 📊 OKRs (Objectives & Key Results)

### Q3 2026 OKRs

| Objective | Key Result | Baseline | Target | Owner |
|-----------|------------|----------|--------|-------|
| **Improve funnel conversion** | CJCR increases from 22% → 28% | 22% | 28% | PM |
| **Reduce churn** | 90-day retention increases from 35% → 42% | 35% | 42% | PM + Marketing |
| **Speed up insights** | Time-to-insight drops from 2 days → 2 hours | 2 days | 2 hrs | Data Eng |
| **Improve data quality** | Data quality issues drop from 15 → 2/month | 15 | 2 | Data Eng |

### Q4 2026 OKRs

| Objective | Key Result | Baseline | Target | Owner |
|-----------|------------|----------|--------|-------|
| **Scale pipeline** | Handle 1M+ orders without performance degradation | 100K | 1M | Data Eng |
| **Launch real-time** | Funnel updates within 5 minutes of event | 24 hrs | 5 mins | Data Eng |
| **Personalization** | Recommendation click-through rate > 8% | N/A | 8% | Product |

## 📈 Funnel KPIs

### Primary Funnel Metrics
| Metric | Formula | Target | Frequency |
|--------|---------|--------|-----------|
| **Acquisition Rate** | New customers / Total visitors | 15% | Daily |
| **Activation Rate** | First orders / New customers | 45% | Weekly |
| **Retention Rate (90-day)** | Repeat customers / Cohort | 42% | Monthly |
| **Growth Rate** | Customers with ≥3 orders / Active customers | 25% | Monthly |
| **Referral Rate** | Reviews with score ≥4 / Orders | 35% | Weekly |
| **Funnel Conversion (Acq→Ref)** | Stages completed / Total stages | 28% | Monthly |

### Secondary Metrics
| Metric | Formula | Target |
|--------|---------|--------|
| **Average Order Value (AOV)** | Total revenue / Total orders | R$ 135 |
| **Customer Lifetime Value (LTV)** | Avg orders × AOV × Avg lifespan | R$ 540 |
| **Churn Rate** | Customers with 0 orders (90 days) / Cohort | < 58% |
| **Time to First Order** | Days from account → first purchase | < 14 days |

## 🔍 Diagnostic Metrics (Root Cause Analysis)

| Problem | Diagnostic Metric | Threshold | Action |
|---------|-------------------|-----------|--------|
| **Acquisition drop** | Bounce rate on landing page | > 60% | Optimize UI/UX |
| **Activation drop** | Cart abandonment rate | > 70% | Simplify checkout |
| **Retention drop** | Days since last order | > 60 days | Retargeting email |
| **Growth drop** | Order frequency decline | > 20% MoM | Loyalty program |
| **Referral drop** | Review submission rate | < 25% | Incentivize reviews |

## 📊 Dashboard KPIs (Metabase)

### KPI 1: Monthly Order Trends
- **Metric:** Orders per month (2016–2018)
- **Visualization:** Line chart
- **Insight:** Seasonality peaks (Nov–Dec)

### KPI 2: Delivery Performance by State
- **Metric:** Avg delivery time (days), estimated vs actual gap
- **Visualization:** Bar chart + heatmap
- **Insight:** Top 5 fast states, top 5 slow states

### KPI 3: Payment Method Distribution
- **Metric:** % orders by payment_type (credit, debit, voucher, boleto)
- **Visualization:** Pie chart + MoM trend
- **Insight:** Credit card dominance (60%)

### KPI 4: Funnel Conversion
- **Metric:** Stage counts + conversion rates
- **Visualization:** Funnel chart
- **Insight:** Activation → Retention drop-off (largest gap)

## 🧪 Experimentation Framework

### A/B Testing Setup
