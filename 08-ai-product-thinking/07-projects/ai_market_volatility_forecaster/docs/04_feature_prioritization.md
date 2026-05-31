# 4. Feature Prioritization (MoSCoW Method)

## 4.1 MoSCoW Categories

| Category | Definition | Examples |
|----------|------------|----------|
| **MUST have** | Non-negotiable, MVP blocking | LSTM volatility forecast, 6-horizon output, Flask API |
| **SHOULD have** | Important but not vital for MVP | Regime detection, multi-asset dashboard, compliance report |
| **COULD have** | Nice to have, defer if time | Options arbitrage scanner, what-if simulator, React frontend |
| **WON'T have** | Out of scope for now | HFT execution (<1ms), kdb+ database, Transformer ensemble |

---

## 4.2 Feature List with MoSCoW Classification

### MUST HAVE (MVP)

| Feature | Description | Acceptance Criteria | Effort | Story Points |
|---------|-------------|---------------------|--------|--------------|
| **LSTM Volatility Forecast** | Train LSTM on 1-year price data, forecast 1/5/30-day vol | 58%+ directional accuracy, <100ms latency | High | 13 |
| **6-Horizon Output** | 1min, 5min, 1hr, 1day, 5day, 30day forecasts | All 6 horizons displayed in dashboard | Medium | 8 |
| **Flask REST API** | `/api/predict`, `/api/data`, `/api/health` endpoints | Response time <200ms, 99.9% uptime | Medium | 8 |
| **Streamlit Dashboard** | Stock selector, forecast chart, vol chart, metrics | Load time <3s, interactive charts | Low | 5 |
| **95% Confidence Intervals** | Upper/lower bands for forecast | Correctly calculated (±2σ) | Low | 3 |
| **yfinance Data Integration** | Fetch 1-year OHLCV data | Handles MultiIndex columns, no errors | Low | 3 |

**Total MUST have**: 40 points

---

### SHOULD HAVE (Phase 2)

| Feature | Description | Acceptance Criteria | Effort | Story Points |
|---------|-------------|---------------------|--------|--------------|
| **Regime Detection** | Auto-identify high/low vol regimes, switch model weights | 85% regime classification accuracy | High | 13 |
| **Multi-Asset Dashboard** | Grid view for 50+ stocks | Sort by vol change, color-coded | Medium | 8 |
| **Options Arbitrage Scanner** | Alert when IV vs. RV > 5% | Fetch IV from Bloomberg API | High | 13 |
| **VaR with Forecasted Vol** | Calculate VaR using forecasted (not historical) vol | 1-day and 10-day VaR | Medium | 8 |
| **Compliance Report Auto-gen** | MiFID II / SEC PDF/Excel report | Schedule daily/weekly/monthly | Medium | 8 |
| **EWMA Volatility Backup** | Simple EWMA if LSTM unavailable | <5s diff from LSTM | Low | 5 |

**Total SHOULD have**: 55 points

---

### COULD HAVE (Phase 3)

| Feature | Description | Acceptance Criteria | Effort | Story Points |
|---------|-------------|---------------------|--------|--------------|
| **What-If Simulator** | Monte Carlo with AI-generated paths | Scenarios: VIX +20%, rates +100bps | High | 21 |
| **React Frontend** | Replace Streamlit with production React | Same features, better performance | High | 21 |
| **Portfolio Vol Forecast** | Portfolio-level volatility (not individual) | Contribution by stock | Medium | 13 |
| **Hedge Simulation** | P&L if hedge 50% with VIX calls | Net P&L = loss avoided - cost | High | 21 |
| **Multi-leg Reversal Detection** | Detect options OTM contract manipulation | 90% recall | High | 21 |
| **SNS Alert Integration** | Send alerts to Slack/Teams/SMS | Configurable thresholds | Low | 5 |

**Total COULD have**: 102 points

---

### WON'T HAVE (Phase 4+)

| Feature | Reason for Deferral |
|---------|---------------------|
| **HFT Execution (<1ms)** | Requires FPGA, not PC-grade inference |
| **kdb+ Database** | $50K/year license, MVP uses yfinance |
| **Transformer Ensemble (Stockformer)** | Phase 3 goal, LSTM sufficient for MVP |
| **FIX Protocol Integration** | Phase 3, requires exchange certification |
| **GPU Auto-scaling (Kubernetes)** | Phase 3, MVP uses single GPU |
| **GDPR Compliance Module** | Phase 3, MVP is demo-only |

---

## 4.3 Prioritization Rationale

### Why MUST-have These Features?

| Feature | Why Non-Negotiable? |
|---------|---------------------|
| **LSTM Forecast** | Core value prop: 58% accuracy vs. 48% random. Without this, no differentiation. |
| **6-Horizon Output** | Traders need 1min (HFT) AND 30day (portfolio). Single-horizon = GARCH replacement. |
| **Flask API** | Production-ready architecture. Without API, can't integrate with trading systems. |
| **Streamlit Dashboard** | Demo-ready in 2 hours. React would add 10x dev time for MVP. |
| **95% CI** | Critical for trader trust. Without uncertainty, forecast is meaningless. |
| **yfinance** | Free, no API key. Bloomberg API requires $25K/year for MVP. |

### Why SHOULD-BE These?

| Feature | Why Important but Not MVP? |
|---------|-----------------------------|
| **Regime Detection** | Improves accuracy 10%, but LSTM works 80% without it. Phase 2 optimization. |
| **Multi-Asset Dashboard** | Market makers need 50 stocks, but MVP is single-stock proof-of-concept. |
| **Options Arbitrage** | High value ($10M savings), but requires Bloomberg API license ($25K). |
| **VaR** | Risk managers need it, but can calculate manually for MVP demo. |
| **Compliance Report** | Regulators need it, but MVP is internal demo, not production. |

### Why COULD-BE These?

| Feature | Why Defer? |
|---------|------------|
| **What-If Simulator** | Nice for PMs, but traders care about forecast, not simulation. |
| **React Frontend** | Streamlit is 10x faster to build. React in Phase 3 for production. |
| **Portfolio Vol** | PMs need it, but MVP focuses on single-stock accuracy proof. |
| **Hedge Simulation** | Complex (21 points), low priority vs. core forecast. |
| **Multi-leg Detection** | Exchange-specific, MVP targets banks first. |
| **SNS Alerts** | Easy to add later, not core to forecast accuracy. |

---

## 4.4 MVP Scope (Phase 1)

**In Scope (Must-have only)**:
- LSTM volatility forecast (1/5/30-day)
- 6-horizon display (1min–30day placeholders)
- Flask API (`/api/predict`, `/api/data`, `/api/health`)
- Streamlit dashboard (stock selector, forecast chart, vol chart)
- 95% confidence intervals
- yfinance data integration

**Out of Scope (Phase 2+)**:
- Regime detection
- Multi-asset dashboard
- Options arbitrage scanner
- VaR calculation
- Compliance reports
- React frontend

**MVP Timeline**: 3 months (40 story points, 2 engineers)
**MVP Budget**: $150K (team + compute + data)
