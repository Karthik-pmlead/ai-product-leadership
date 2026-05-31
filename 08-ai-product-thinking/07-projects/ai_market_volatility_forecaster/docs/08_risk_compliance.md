# 8. Risk Assessment & Compliance

## 8.1 Technical Risks

### Risk 1: Model Drift During Regime Shifts

| Attribute | Description |
|-----------|-------------|
| **Description** | LSTM trained on 2023–2024 data fails during 2025 rate hikes (regime change) |
| **Probability** | 60% (high, given 2020 pandemic, 2022 rate hikes) |
| **Impact** | Accuracy drops from 58% → 45%, traders lose money |
| **Mitigation** | **Adaptive retraining**: Retrain weekly on last 90 days; **Regime detection**: Auto-switch model weights when vol >30% |
| **Contingency** | Fallback to EWMA (simple, robust) if LSTM accuracy <50% for 3 consecutive days |

**Monitoring**: Track accuracy daily; alert if <55% for 3 days.

---

### Risk 2: Overfitting to Historical Data

| Attribute | Description |
|-----------|-------------|
| **Description** | LSTM memorizes 2020–2024 patterns, fails on unseen data |
| **Probability** | 40% |
| **Impact** | Backtest accuracy 65%, live accuracy 45% |
| **Mitigation** | **Walk-forward validation** (no overlapping train/test); **20% dropout**; **Early stopping** (patience=10); **Out-of-sample testing** on 2025 data |
| **Contingency** | Reduce model complexity (hidden_size=32 instead of 64) |

**Monitoring**: Compare backtest vs. live accuracy; alert if gap >10%.

---

### Risk 3: Data Quality Issues

| Attribute | Description |
|-----------|-------------|
| **Description** | yfinance returns NaN, duplicated rows, or wrong prices |
| **Probability** | 30% |
| **Impact** | Forecast errors, crashes |
| **Mitigation** | **Data validation**: Check for NaN, duplicates, price gaps >20%; **Fallback**: Use Refinitiv API if yfinance fails |
| **Contingency** | Cache last known good data, use EWMA until data restored |

**Monitoring**: Data quality dashboard; alert if >1% NaN/duplicates.

---

### Risk 4: API Latency Spike During Market Hours

| Attribute | Description |
|-----------|-------------|
| **Description** | API latency jumps from 100ms → 2s during high volume (market open) |
| **Probability** | 25% |
| **Impact** | Traders can't use real-time forecast |
| **Mitigation** | **GPU auto-scaling** (Kubernetes); **Caching**: Pre-compute forecasts nightly; **CDN**: Cache static assets |
| **Contingency** | Serve cached forecast (1-hour old) if real-time >500ms |

**Monitoring**: Latency p95; alert if >200ms for 5 minutes.

---

## 8.2 Business Risks

### Risk 5: Competitor Copies Our Model

| Attribute | Description |
|-----------|-------------|
| **Description** | Bloomberg releases AI vol forecast with same accuracy |
| **Probability** | 40% (Bloomberg has more data, compute) |
| **Impact** | Our $50K MRR → $0 in 6 months |
| **Mitigation** | **Patent pending** for regime detection algorithm; **First-mover advantage**: Build enterprise relationships before Bloomberg ships; **Multi-modal edge**: LOB + sentiment + macro (hard to replicate) |
| **Contingency** | Pivot to niche (small hedge funds) where Bloomberg doesn't compete |

**Monitoring**: Track Bloomberg product releases; quarterly competitive analysis.

---

### Risk 6: Enterprise Sales Takes Longer Than Expected

| Attribute | Description |
|-----------|-------------|
| **Description** | JPM/Multi-year sales cycle, MVP sits unused for 12 months |
| **Probability** | 50% |
| **Impact** | $0 revenue by Month 12, startup fails |
| **Mitigation** | **Start with sell-side brokers** (shorter sales cycle); **Offer freemium** (free for 100 forecasts/day); **Build referral network** (portfolio managers refer to traders) |
| **Contingency** | Bootstrapped revenue: Charge $500/month for pro tier while waiting for enterprise |

**Monitoring**: Track sales pipeline length; alert if >6 months per deal.

---

### Risk 7: Regulatory Changes Make Model Non-Compliant

| Attribute | Description |
|-----------|-------------|
| **Description** | SEC new rule requires explainable AI, our LSTM is black box |
| **Probability** | 20% |
| **Impact** | Must rebuild with SHAP/LIME, 6-month delay |
| **Mitigation** | **Build explainability now**: SHAP values in Phase 2; **Engage regulators early**: Present model to SEC/FCA for feedback; **Third-party validation**: Hire auditor to certify model |
| **Contingency** | Switch to interpretable model (linear + tree ensemble) if required |

**Monitoring**: Track SEC/FCA rule changes; monthly regulatory scan.

---

## 8.3 Compliance Requirements

### MiFID II Article 17 (Algorithmic Trading)

| Requirement | Our Implementation |
|-------------|-------------------|
| **Risk controls** | Pre-trade volatility check (alert if forecast vol >30%) |
| **Circuit breakers** | Auto-pause trading if forecast accuracy <50% for 3 days |
| **Order monitoring** | Log all trades triggered by forecast (who, when, why) |
| **System resilience** | 99.9% uptime, fallback to EWMA if LSTM fails |
| **Documentation** | Model documentation in `docs/prd/05_technical_specs.md` |

**Audit Frequency**: Annual internal audit + external auditor every 2 years.

---

### SEC Rule 15c3-5 (Market Risk Control)

| Requirement | Our Implementation |
|-------------|-------------------|
| **Pre-trade checks** | Volatility threshold check before order submission |
| **Real-time monitoring** | Dashboard showing forecast vol vs. actual vol |
| **Post-trade analysis** | Daily report: forecast accuracy, trades executed, P&L |
| **Record retention** | 7-year log of all predictions and trades |
| **Chief Risk Officer approval** | Model sign-off by CRO before production |

**Audit Frequency**: Quarterly internal review.

---

### GDPR (EU Data Privacy)

| Requirement | Our Implementation |
|-------------|-------------------|
| **Data minimization** | Only store necessary data (ticker, date, forecast) |
| **Anonymization** | No trader PII (names, emails) stored |
| **Right to erasure** | Delete user data upon request (within 30 days) |
| **Data portability** | Export user data as CSV on request |
| **Consent** | User opts in to data collection (checkbox) |

**Audit Frequency**: Annual data privacy audit.

---

## 8.4 Model Validation Framework

### Internal Validation (Quant Team)

| Step | Description | Owner |
|------|-------------|-------|
| **1. Backtest** | Walk-forward on 2020–2024 data | ML Engineer |
| **2. Stress test** | 2020 pandemic, 2022 rate hikes scenarios | Quant Analyst |
| **3. Comparison** | vs. GARCH, vs. Bloomberg HLVOL | Quant Analyst |
| **4. Sensitivity** | Vary hyperparameters (hidden_size, epochs) | ML Engineer |
| **5. Sign-off** | CRO approval | Chief Risk Officer |

**Pass Criteria**: Accuracy ≥58%, RMSE ≤0.8× GARCH, stress test P&L ≥-10%.

---

### External Validation (Auditor)

| Auditor | Scope | Frequency |
|---------|-------|-----------|
| **Deloitte** | Model risk management | Every 2 years |
| **FCA** (UK) | MiFID II compliance | Annual |
| **SEC** (US) | Rule 15c3-5 compliance | Every 3 years |

**Cost**: $50K–$100K per audit.

---

## 8.5 Incident Response Plan

### Scenario: Model Accuracy Drops to 45% for 3 Days

| Step | Action | Owner | Timeline |
|------|--------|-------|----------|
| **1. Alert** | NPS detects accuracy <55%, sends Slack alert | Monitoring System | Immediate |
| **2. Triage** | Quant team investigates root cause | Quant Analyst | <1 hour |
| **3. Fallback** | Switch to EWMA (simple, robust) | DevOps | <10 minutes |
| **4. Retrain** | Retrain LSTM on last 90 days | ML Engineer | <24 hours |
| **5. Validate** | Backtest new model, confirm accuracy ≥58% | Quant Analyst | <2 hours |
| **6. Switch Back** | Resume LSTM if validated | DevOps | <10 minutes |
| **7. Post-mortem** | Document root cause, prevent recurrence | You (PM) | <1 week |

**Communication**: Notify users within 1 hour of incident, daily updates until resolved.

---

## 8.6 Risk Register Summary

| Risk | Probability | Impact | Mitigation | Status |
|------|-------------|--------|------------|--------|
| Model drift | 60% | High | Adaptive retraining, regime detection | 🟡 Active |
| Overfitting | 40% | High | Walk-forward, dropout, early stopping | 🟡 Active |
| Data quality | 30% | Medium | Validation, fallback to Refinitiv | 🟢 Monitored |
| API latency | 25% | Medium | GPU auto-scaling, caching | 🟢 Monitored |
| Competitor copy | 40% | Critical | Patent, first-mover, multi-modal | 🟡 Active |
| Sales cycle | 50% | High | Freemium, sell-side first | 🟡 Active |
| Regulatory change | 20% | Critical | Explainability now, regulator engagement | 🟢 Monitored |
