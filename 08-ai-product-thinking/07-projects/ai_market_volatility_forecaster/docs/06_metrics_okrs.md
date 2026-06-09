# 6. Metrics & OKRs

## 6.1 North Star Metric

**"Accurate Volatility Forecasts Delivered"**  
= (Number of accurate forecasts) × (Number of users)

- **Accurate**: Forecast matches actual vol within 10% error
- **Users**: Traders, market makers, risk managers actively using the platform

**Target**: 10,000 accurate forecasts/month × 50 active users = 500,000 forecast-user pairs/month

---

## 6.2 OKRs (Objectives & Key Results)

### Objective 1: Achieve State-of-the-Art Forecast Accuracy

| Key Result | Baseline | Target | Measurement |
|------------|----------|--------|-------------|
| **Directional accuracy (1hr)** | 48% (random) | **58–62%** | Rolling 30-day backtest [web:33] |
| **Volatility RMSE (5day)** | 1.0× (GARCH) | **0.8× (20% improvement)** | Mean Squared Error [web:21][web:34] |
| **Liquidity crash detection** | 0% | **85% recall, <5% FP** | Precision-Recall curve [web:33] |
| **Options pricing error** | 8–10% | **5–6%** | Black-Scholes vs. realized [web:31] |

**Why these matter**: 
- 58% directional accuracy = **10% edge over random**,足以盈利 for traders
- 20% RMSE improvement = **$10M/year savings** for JPM's derivatives book
- 85% crash detection = **prevent flash crashes**, protect market integrity

---

### Objective 2: Delight Users with Fast, Reliable Forecasts

| Key Result | Baseline | Target | Measurement |
|------------|----------|--------|-------------|
| **Forecast latency** | N/A | **<100ms (1min horizon)** | Time from request to response [web:33] |
| **API uptime** | N/A | **99.9%** | Monthly (downtime <43min) |
| **Dashboard load time** | N/A | **<3 seconds** | From click to rendered |
| **User satisfaction (NPS)** | N/A | **>50** | Survey after 30 days |

**Why these matter**:
- <100ms latency = usable for HFT (1min horizon)
- 99.9% uptime = traders can rely on it during market hours
- <3s load time = no frustration, high adoption

---

### Objective 3: Drive Adoption Across Capital Markets

| Key Result | Baseline | Target | Measurement |
|------------|----------|--------|-------------|
| **Active users** | 0 | **50** (Phase 1), **500** (Phase 2) | Monthly active users (MAU) |
| **Signup-to-active conversion** | N/A | **>30%** | Sign up → use forecast ≥3x/week |
| **Retention (30-day)** | N/A | **>60%** | Users still active after 30 days |
| **Enterprise pilots** | 0 | **3** (LSEG, JPM, MS) | Signed LOIs |

**Why these matter**:
- 50 users = product-market fit proof
- 30% conversion = value proposition clear
- 3 enterprise pilots = revenue pipeline

---

### Objective 4: Ensure Regulatory Compliance

| Key Result | Baseline | Target | Measurement |
|------------|----------|--------|-------------|
| **MiFID II Art. 17 documentation** | 0% | **100% complete** | Audit-ready docs |
| **SEC Rule 15c3-5 logs** | None | **7-year retention** | Audit trail |
| **Model validation sign-off** | None | **2 internal + 1 external** | Quant team + regulator |
| **GDPR compliance** | N/A | **100% anonymized** | Data audit |

**Why these matter**:
- MiFID II / SEC compliance = **can sell to EU/US banks**
- Model validation = **regulators won't fine us**
- GDPR = **avoid €20M fines**

---

## 6.3 KPIs (Key Performance Indicators)

### Daily KPIs (Tracked in Dashboard)

| KPI | Formula | Target | Alert Threshold |
|-----|---------|--------|-----------------|
| **Forecast Accuracy** | `1 - forecast_vol - actual_vol / actual_vol` | >90% | <85% for 3 days |
| **API Success Rate** | `successful_requests / total_requests` | >99.9% | <99% for 1 hour |
| **Latency (p95)** | 95th percentile response time | <100ms | >200ms for 5min |
| **Active Users** | Unique users in last 24h | >10/day | <5/day for 3 days |

---

### Weekly KPIs (Tracked in Reports)

| KPI | Formula | Target | Alert Threshold |
|-----|---------|--------|-----------------|
| **New Signups** | Count per week | >20/week | <10/week for 2 weeks |
| **Feature Usage** | % users using ≥3 features/week | >40% | <20% for 2 weeks |
| **Churn Rate** | `users_lost / users_start` | <5%/week | >10%/week |
| **NPS** | `(promoters - detractors) / total` | >50 | <30 |

---

### Monthly KPIs (Tracked in Business Reviews)

| KPI | Formula | Target | Alert Threshold |
|-----|---------|--------|-----------------|
| **MRR (Monthly Recurring Revenue)** | $ from subscriptions | $50K/month (Phase 2) | <$30K for 2 months |
| **CAC (Customer Acquisition Cost)** | `marketing_spend / new_customers` | <$5K/customer | >$10K |
| **LTV (Customer Lifetime Value)** | `MRR × avg_lifetime_months` | >$100K/customer | <$50K |
| **LTV:CAC Ratio** | `LTV / CAC` | >5:1 | <3:1 |

---

## 6.4 Success Criteria for MVP (Phase 1)

| Criterion | Target | Pass/Fail |
|-----------|--------|-----------|
| **LSTM trained** | 100 epochs, loss <0.01 | ✅ Pass |
| **Directional accuracy** | ≥55% (1hr horizon) | ✅ Pass |
| **API functional** | All 3 endpoints return 200 OK | ✅ Pass |
| **Dashboard loads** | <3 seconds, no errors | ✅ Pass |
| **100 forecast calls** | Successfully completed | ✅ Pass |
| **10 user tests** | 8/10 rate "useful" or "very useful" | ✅ Pass |

**MVP Launch Decision**: All 6 criteria must pass. If any fail, iterate and retest.

---

## 6.5 Backtesting Framework

### Walk-Forward Validation (No Look-Ahead Bias)

```python
def walk_forward_backtest(model, data, train_window=252, test_window=20):
    """
    Train on 1 year, test on 20 days, roll forward.
    """
    accuracies = []
    for i in range(train_window, len(data) - test_window):
        train_data = data[i-train_window:i]
        test_data = data[i:i+test_window]
        
        model.fit(train_data)
        predictions = model.predict(test_data)
        actual = test_data['volatility'].values
        
        accuracy = 1 - np.mean(np.abs(predictions - actual) / actual)
        accuracies.append(accuracy)
    
    return np.mean(accuracies), np.std(accuracies)
```

**Why walk-forward?**: Prevents **look-ahead bias** (using future data to predict past).

### Performance Metrics from Backtest

| Metric | Formula | Target |
|--------|---------|--------|
| **Directional Accuracy** | `correct_directions / total_predictions` | ≥58% |
| **RMSE** | `sqrt(mean((pred - actual)^2))` | ≤0.8× GARCH |
| **Sharpe Ratio** | `mean(returns) / std(returns)` | ≥1.5 |
| **Max Drawdown** | `min(cumulative_return)` | ≥-10% |
| **Win Rate** | `profitable_trades / total_trades` | ≥55% |
