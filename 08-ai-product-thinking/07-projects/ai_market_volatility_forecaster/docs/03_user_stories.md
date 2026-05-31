# 3. User Stories

## 3.1 Persona: Options Trader (Sell-side)

### Story 1: Real-time Volatility Forecast for Delta Hedging
**As an** options trader,  
**I want** 5-minute volatility forecast for AAPL,  
**So that** I can adjust my delta hedge in real-time during earnings.

**Acceptance Criteria**:
- [ ] Forecast updates every 5 minutes with <100ms latency
- [ ] Shows 5min, 1hr, 1day horizons side-by-side
- [ ] Confidence interval (80%/95%) displayed
- [ ] Alert when forecasted vol > 30% (threshold configurable)
- [ ] Export forecast to CSV for audit trail

**Priority**: Must-have  
**Effort**: Medium  
**Story Points**: 5

---

### Story 2: Options Implied Volatility Arbitrage Alert
**As an** options trader,  
**I want** alert when implied vol (IV) deviates >5% from forecasted realized vol (RV),  
**So that** I can trade the mispricing (sell expensive IV, buy cheap IV).

**Acceptance Criteria**:
- [ ] Fetch IV from Bloomberg API (HV/IV surface)
- [ ] Compare IV vs. forecasted RV (1day horizon)
- [ ] Alert when |IV - RV| > 5% (configurable)
- [ ] Show theoretical fair value using Black-Scholes with forecasted vol
- [ ] One-click trade ticket integration

**Priority**: Should-have  
**Effort**: High  
**Story Points**: 13

---

## 3.2 Persona: Market Maker

### Story 3: Liquidity Crash Early Warning
**As a** market maker,  
**I want** 10-second warning when liquidity is about to dry up,  
**So that** I can widen bid-ask spreads before losing money on stale quotes.

**Acceptance Criteria**:
- [ ] Monitor order book depth (Level 2/3 data)
- [ ] Detect imbalance (bid volume << ask volume)
- [ ] Alert 10 seconds before liquidity drop (85% recall, <5% FP)
- [ ] Suggest new spread width based on forecasted vol
- [ ] Auto-pause quoting if(alert triggered)

**Priority**: Must-have  
**Effort**: High  
**Story Points**: 13

---

### Story 4: Multi-Asset Volatility Dashboard
**As a** market maker,  
**I want** dashboard showing volatility forecast for 50+ stocks I make market in,  
**So that** I can prioritize which quotes to adjust first.

**Acceptance Criteria**:
- [ ] Grid view: stocks × horizons (1min, 5min, 1hr, 1day)
- [ ] Color-coded: red = high vol, green = low vol
- [ ] Sort by forecasted vol change (largest increase first)
- [ ] Click to drill into individual stock forecast
- [ ] Refresh every 1 minute

**Priority**: Should-have  
**Effort**: Medium  
**Story Points**: 8

---

## 3.3 Persona: Risk Manager

### Story 5: Real-time VaR with Foreforward Volatility
**As a** risk manager,  
**I want** VaR calculation using forecasted volatility (not historical),  
**So that** I capture tail risk before it happens.

**Acceptance Criteria**:
- [ ] VaR = f(forecasted vol, portfolio weights, correlation matrix)
- [ ] 1-day and 10-day VaR (SEC regulatory requirement)
- [ ] Show VaR with forecasted vol vs. historical vol (difference highlighted)
- [ ] Alert when VaR exceeds threshold (e.g., > $50M)
- [ ] Export to Risk Management System (API)

**Priority**: Must-have  
**Effort**: Medium  
**Story Points**: 8

---

### Story 6: Stress Testing with AI-Generated Scenarios
**As a** risk manager,  
**I want** stress test portfolio with AI-generated volatility scenarios (e.g., "VIX spikes 20%"),  
**So that** I know losses before the market moves.

**Acceptance Criteria**:
- [ ] Monte Carlo simulation with AI-generated paths (not random)
- [ ] Scenarios: "VIX +20%", "Interest rates +100bps", "Stock crash -15%"
- [ ] Show P&L distribution (histogram) for each scenario
- [ ] Compare to historical stress (2008, 2020)
- [ ] Export stress test report (PDF)

**Priority**: Could-have  
**Effort**: High  
**Story Points**: 21

---

## 3.4 Persona: Portfolio Manager

### Story 7: Portfolio Volatility Forecast
**As a** portfolio manager,  
**I want** forecasted volatility for my entire portfolio (not individual stocks),  
**So that** I can decide if I need to hedge.

**Acceptance Criteria**:
- [ ] Portfolio vol = f(individual vols, correlation matrix, weights)
- [ ] 1day, 5day, 30day horizons
- [ ] Show contribution by stock (which stock drives most vol)
- [ ] Alert when portfolio vol > threshold (e.g., > 25%)
- [ ] Suggest hedge ratio (e.g., "Buy $10M VIX calls")

**Priority**: Should-have  
**Effort**: Medium  
**Story Points**: 8

---

### Story 8: What-If Hedging Simulation
**As a** portfolio manager,  
**I want** simulation showing P&L if I hedge 50% of portfolio with VIX calls,  
**So that** I can compare hedge cost vs. risk reduction.

**Acceptance Criteria**:
- [ ] Input: hedge instrument (VIX calls, PUT options), ratio (0–100%)
- [ ] Output: P&L with hedge vs. without hedge (scatter plot)
- [ ] Show hedge cost (premium) vs. loss avoided
- [ ] Net P&L = (loss avoided) - (hedge cost)
- [ ] One-click execute hedge (integration with trading system)

**Priority**: Could-have  
**Effort**: High  
Story Points**: 21

---

## 3.5 Persona: Exchange Regulator (LSEG, Nasdaq, NYSE)

### Story 9: Real-time Market Surveillance Dashboard
**As an** exchange regulator,  
**I want** dashboard showing anomaly detection for all trades (wash trading, spoofing),  
**So that** I can investigate before market integrity is compromised.

**Acceptance Criteria**:
- [ ] Real-time feed: 150K transactions/second [web:20]
- [ ] Anomaly types: wash trading, spoofing, layering, multi-leg reversal
- [ ] 97.5% detection rate, <1% false positive [web:20]
- [ ] Alert with severity (high/medium/low)
- [ ] One-click investigate (drill into trade details)

**Priority**: Must-have  
**Effort**: High  
**Story Points**: 13

---

### Story 10: Regulatory Compliance Report Auto-Generation
**As an** exchange regulator,  
**I want** auto-generated MiFID II / SEC compliance report,  
**So that** I don't waste hours manually compiling data.

**Acceptance Criteria**:
- [ ] Report includes: anomaly count, detection rate, false positive rate, actions taken
- [ ] Format: PDF (regulator submission) + Excel (internal)
- [ ] Schedule: daily, weekly, monthly (configurable)
- [ ] Audit trail: who generated, when, what changes
- [ ] Signature-ready (digital signature for submission)

**Priority**: Should-have  
**Effort**: Medium  
**Story Points**: 8

---

## 3.6 Story Prioritization Summary

| Priority | Stories | Total Points |
|----------|---------|--------------|
| **Must-have** | 1, 3, 5, 9 | 39 |
| **Should-have** | 2, 4, 7, 10 | 32 |
| **Could-have** | 6, 8 | 42 |
| **Won't-have (Phase 1)** | — | 0 |

**MVP Scope**: Must-have stories only (39 points, ~2 months with 2 engineers)
