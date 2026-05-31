# System Design: AI Market Volatility Forecaster

## 1. High-Level Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│ CLIENT LAYER │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ Streamlit │ │ React (Ph3) │ │ Mobile App │ │
│ │ Dashboard │ │ Frontend │ │ (Phase 3+) │ │
│ └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ │
│ │ │ │ │
│ └───────────────────┼───────────────────┘ │
│ ▼ HTTP/REST │
└─────────────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────┐
│ API GATEWAY LAYER │
│ ┌───────────────────────────────────────────────────────────────┐ │
│ │ Flask API (FastAPI Phase 3) │ │
│ │ Endpoints: /api/predict, /api/data, /api/health, /api/stocks │ │
│ │ Features: Rate limiting, JWT auth (Ph2), Request validation │ │
│ └───────────────────────┬───────────────────────────────────────┘ │
│ │ │
└──────────────────────────┼──────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────┐
│ APPLICATION LAYER │
│ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │ LSTM Forecaster │ │ Regime Detector │ │
│ │ (PyTorch) │ │ (Phase 2) │ │
│ │ input: 60-day seq │ │ High/Low vol cls │ │
│ │ output: vol forecast│ │ │ │
│ └──────────┬───────────┘ └──────────┬───────────┘ │
│ │ │ │
│ └───────────┬─────────────┘ │
│ ▼ │
│ ┌──────────────────────┐ │
│ │ Feature Engineer │ │
│ │ - Returns │ │
│ │ - Volatility (20d) │ │
│ │ - RSI, MACD │ │
│ │ - Volume Ratio │ │
│ └──────────┬───────────┘ │
└─────────────────────────┼──────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────────┐
│ DATA LAYER │
│ ┌──────────────────────┐ ┌──────────────────────┐ │
│ │ yfinance (MVP) │ │ kdb+ (Phase 3) │ │
│ │ Free OHLCV data │ │ 150K tx/sec │ │
│ │ 1–730 days │ │ Limit Order Book │ │
│ └──────────┬───────────┘ └──────────┬───────────┘ │
│ │ │ │
│ └───────────┬─────────────┘ │
│ ▼ │
│ ┌──────────────────────┐ │
│ │ Redis Cache │ │
│ │ - Forecasts (1hr) │ │
│ │ - Stock metadata │ │
│ └──────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```


---

## 2. Component Details

### 2.1 Frontend (Streamlit MVP)

**Technology**: Streamlit (Python)  
**Purpose**: Dashboard for traders to view forecasts, volatility, metrics  
**Key Features**:
- Stock selector (dropdown)
- Forecast horizon slider (1–30 days)
- Interactive Plotly charts (price forecast, volatility, confidence intervals)
- Forecast table (dates, prices, upper/lower bounds)
- Download CSV button

**Why Streamlit?**
- 100 lines of code vs. 600 for React
- Built-in widgets (`st.selectbox`, `st.slider`)
- Built-in Plotly support (`st.plotly_chart`)
- 2–3 hour build time for MVP

**Future**: Replace with React (Phase 3) for:
- Better performance (virtualized tables for 50+ stocks)
- Real-time WebSocket updates (no page refresh)
- Mobile responsiveness

---

### 2.2 API Layer (Flask)

**Technology**: Flask (Python) → FastAPI (Phase 3)  
**Purpose**: REST endpoints for forecast, data, health check  
**Endpoints**:
- `GET /api/health` — Health check
- `GET /api/stocks` — List stocks
- `GET /api/data` — Fetch historical data
- `POST /api/predict` — Generate forecast (core)
- `POST /api/train` — Trigger retraining (Phase 2)
- `GET /api/metrics` — Model performance (Phase 2)

**Key Features**:
- Request validation (Pydantic)
- Error handling (custom error messages)
- Rate limiting (Flask-Limiter)
- CORS enabled (for frontend)
- JWT authentication (Phase 2)

**Why Flask?**
- Simple, lightweight, Python-native
- Easy to test (pytest)
- 500 lines of code for full API
- Production-ready with Gunicorn + Nginx

---

### 2.3 ML Model (LSTM Forecaster)

**Technology**: PyTorch (Python)  
**Purpose**: Time-series volatility prediction  
**Architecture**:
```python
class LSTMVolatilityForecaster(nn.Module):
    lstm = nn.LSTM(input_size=1, hidden_size=64, num_layers=2, dropout=0.2)
    fc = nn.Sequential(nn.Linear(64, 32), nn.ReLU(), nn.Dropout(0.2), nn.Linear(32, 1))
```

**Input Features**:
1. `Close` price (scaled to [0,1])
2. Optional (Phase 2): `Returns`, `Volatility_20d`, `RSI`, `Volume`

**Output**:
- Next-day volatility (annualized)
- Multi-horizon forecast (1/5/30 days) via repeated prediction

**Training**:
- Loss: Mean Squared Error (MSE)
- Optimizer: Adam (lr=0.001)
- Batch size: 32
- Epochs: 100 (early stopping patience=10)
- Validation: Walk-forward (no look-ahead bias)

**Inference Latency**: <100ms (CPU), <10ms (GPU)

**Accuracy Target**:
- Directional accuracy: 58–62% (1hr horizon)
- Volatility RMSE: 0.8× GARCH (20% improvement)

---

### 2.4 Data Pipeline

**MVP (Phase 1)**:
- Source: yfinance (free, no API key)
- Frequency: On-demand (fetch when user requests)
- Latency: 2–5 seconds (network + data processing)
- Limitation: Rate-limited (~100 requests/hour)

**Production (Phase 3)**:
- Source: kdb+ time-series database (industry standard)
- Frequency: Real-time streaming (Kafka)
- Latency: <100ms for 1-min horizon
- Data: Limit Order Book (Level 2/3), trade ticks, macro indicators

**Caching Strategy (Redis)**:
- Cache forecast for 1 hour (most users query same ticker/horizon)
- Cache stock metadata (list, sector, market cap)
- Invalidate cache when new model version deployed

---

## 3. Data Flow

### Forecast Generation Flow
```
User selects "AAPL", horizon=10 in Streamlit
│
▼

Streamlit calls Flask POST /api/predict with {ticker: "AAPL", horizon: 10}
│
▼

Flask validates input, checks Redis cache for existing forecast
│
├─ Cache hit → Return cached forecast (10ms)
│
└─ Cache miss → Fetch data from yfinance (2s)
│
▼

Feature Engineer: Calculate Returns, Volatility_20d, RSI, etc.
│
▼

Prepare sequences (60-day lookback, scaled to )
│
▼

LSTM Inference: forward() → volatility forecast (50ms CPU)
│
▼

Generate multi-horizon forecast (repeat prediction 10 times)
│
▼

Calculate 95% confidence intervals (±2σ)
│
▼

Store forecast in Redis (TTL=1 hour)
│
▼

Return JSON to Flask → Streamlit → Render chart
```


**Total Latency**: 2.1 seconds (first request), 10ms (cached)

---

## 4. Scalability Design

### Horizontal Scaling (Phase 3)
```
┌─────────────────────────────────────────────────────────┐
│ Load Balancer │
│ (Nginx / AWS ALB) │
└───────────────────┬─────────────────────────────────────┘
│
┌───────────┼───────────┐
▼ ▼ ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│ Flask │ │ Flask │ │ Flask │
│ Instance│ │ Instance│ │ Instance│
│ (1) │ │ (2) │ │ (3) │
└────┬────┘ └────┬────┘ └────┬────┘
│ │ │
└───────────┼───────────┘
▼
┌───────────────┐
│ Redis │
│ (Cache) │
└───────┬───────┘
│
▼
┌───────────────┐
│ kdb+ │
│ (Database) │
└───────────────┘
```


**Scaling Triggers**:
- CPU >80% for 5 minutes → Add 1 Flask instance
- Memory >85% → Add 1 instance + optimize batch size
- Latency p95 >200ms → Add GPU instance for inference

**Auto-scaling (Kubernetes)**:
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: flask-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: flask-api
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

---

## 5. Failure Handling

### Single Point of Failure (SPOF) Mitigation

| Component | SPOF Risk | Mitigation |
|-----------|-----------|------------|
| **Flask API** | Single instance crashes | Kubernetes auto-restart, 2+ replicas |
| **Redis** | Cache loss → slower response | Redis Cluster (3 nodes), fallback to direct DB query |
| **kdb+** | Database unavailable | Refinitiv API backup, cached data fallback |
| **LSTM Model** | Inference fails | Fallback to EWMA (simple, robust) |
| **yfinance** | Rate-limited/down | Cache last known good data, switch to Refinitiv |

### Circuit Breaker Pattern

```python
@predict_endpoint.route("/api/predict", methods=["POST"])
def predict():
    try:
        forecast = lstm_model.predict(data)
    except ModelError as e:
        # Circuit breaker: switch to EWMA
        forecast = ewma_forecast(data)
        log_circuit_breaker_opened("lstm", str(e))
    
    return jsonify(forecast)
```

**Circuit States**:
- **Closed**: Normal operation (LSTM)
- **Open**: LSTM failing → use EWMA (fallback)
- **Half-Open**: Test LSTM every 10 minutes → if 3/3 succeed, close circuit

---

## 6. Security Design

### Threat Model

| Threat | Impact | Mitigation |
|--------|--------|------------|
| **API abuse** (DDoS) | Service unavailable | Rate limiting (100 req/min), Cloudflare WAF |
| **Unauthorized access** | Data leak | JWT auth (Phase 2), API keys (Phase 3) |
| **Model inversion attack** | Steal training data | Obfuscate model internals, limit query frequency |
| **Data poisoning** | Model accuracy drops | Validate input data (no NaN, no gaps >20%) |
| **Man-in-the-middle** | Intercept forecasts | TLS 1.3 (HTTPS), certificate pinning (mobile) |

### Secrets Management

```bash
# .env file (never commit to Git)
FLASK_SECRET_KEY=super_secret_key_123
JWT_PRIVATE_KEY=path/to/private.key
BLOOMBERG_API_KEY=bbg_api_key_xyz
KDB_PASSWORD=kdb_password_abc
```

**Phase 3**: Use AWS Secrets Manager / HashiCorp Vault

---

## 7. Deployment Diagram

### Development (MVP)
```
Local Machine (Your Laptop)
├── Streamlit (localhost:8501)
├── Flask API (localhost:5000)
├── PyTorch (CPU/GPU local)
└── yfinance (internet)
```

### Production (Phase 3)
```
AWS Cloud (us-east-1)
├── CloudFront (CDN for frontend)
├── S3 (React static assets)
├── ALB (Load balancer)
├── ECS/Fargate (Flask API containers, 3 replicas)
├── EKS (Kubernetes for GPU inference)
├── ElastiCache (Redis Cluster, 3 nodes)
├── RDS (PostgreSQL for user data)
├── kdb+ Cluster (3 nodes, on-prem or cloud)
└── CloudWatch (Logging + Monitoring)
```
**Deployment Pipeline (CI/CD)**:
```
GitHub → GitHub Actions → Docker Build → ECR → ECS Deploy
↓
Unit Tests
Integration Tests
Security Scan (Trivy)
```

---

## 8. Monitoring & Observability

### Metrics to Track

| Metric | Type | Alert Threshold |
|--------|------|-----------------|
| **API Latency (p95)** | Histogram | >200ms for 5min |
| **API Error Rate** | Counter | >0.1% for 5min |
| **Forecast Accuracy** | Gauge | <55% for 3 days |
| **Active Users** | Counter | <10/day for 3 days |
| **GPU Utilization** | Gauge | >90% for 10min → scale up |
| **Redis Hit Rate** | Gauge | <70% → optimize cache keys |

### Logging Strategy

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info(f"Forecast generated for {ticker}, horizon={horizon}")
```

**Log Aggregation**: ELK Stack (Elasticsearch, Logstash, Kibana) or AWS CloudWatch Logs

---

## 9. Technology Stack Summary

| Layer | MVP (Phase 1) | Production (Phase 3) |
|-------|---------------|----------------------|
| **Frontend** | Streamlit (Python) | React + TypeScript |
| **API** | Flask (Python) | FastAPI (Python) |
| **ML** | PyTorch (CPU/GPU local) | PyTorch + GPU (AWS p3.8xlarge) |
| **Database** | yfinance (on-demand) | kdb+ time-series + Redis cache |
| **Auth** | None | JWT + OAuth2 |
| **Hosting** | Local machine | AWS (ECS + EKS + CloudFront) |
| **Monitoring** | Print statements | CloudWatch + Grafana + PagerDuty |
| **CI/CD** | Manual | GitHub Actions + ArgoCD |

---

## 10. Future Enhancements (Phase 4+)

| Feature | Timeline | Impact |
|---------|----------|--------|
| **Transformer Ensemble** | Q3 2026 | 5% more accurate for 30-day horizon |
| **Limit Order Book Feed** | Q3 2026 | Detect microstructure patterns, 10% accuracy boost |
| **Multi-Asset Portfolio Forecast** | Q4 2026 | Portfolio-level vol, hedge ratio suggestions |
| **Options Arbitrage Scanner** | Q4 2026 | Detect IV vs. RV mispricing, $10M savings |
| **FIX Protocol Integration** | Q1 2027 | Direct trade execution from forecast |
| **Mobile App (iOS/Android)** | Q2 2027 | Traders get alerts on phone |
