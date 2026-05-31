# API Specification: AI Market Volatility Forecaster

## Overview
RESTful API for time-series volatility forecasting. Built with Flask, returns JSON.  
**Base URL**: `http://localhost:5000` (development) / `https://api.volatility.ai` (production)  
**Version**: `v1`  
**Content-Type**: `application/json`

---

## Authentication
**Phase 1 (MVP)**: No authentication (local demo)  
**Phase 2+**: JWT Bearer Token
```http
Authorization: Bearer <your_jwt_token>
```

---

## Endpoints

### 1. `GET /api/health`
**Health check** — verify API is running.

**Request**:
```http
GET /api/health
```

**Response (200 OK)**:
```json
{
  "status": "healthy",
  "service": "AI Volatility Forecaster API",
  "version": "1.0.0",
  "timestamp": "2026-06-01T13:45:00Z"
}
```

**Error Response**:
```json
{
  "status": "unhealthy",
  "error": "Database connection failed"
}
```

---

### 2. `GET /api/stocks`
**List available stocks** for forecasting.

**Request**:
```http
GET /api/stocks
```

**Response (200 OK)**:
```json
{
  "stocks": ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY", "AMZN", "NVDA", "META", "JPM", "BAC"],
  "count": 10
}
```

---

### 3. `GET /api/data`
**Fetch historical stock data** (OHLCV + volatility).

**Query Parameters**:
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `ticker` | string | No | `AAPL` | Stock symbol (e.g., `AAPL`, `MSFT`) |
| `days` | integer | No | `365` | Days of historical data (1–730) |

**Request**:
```http
GET /api/data?ticker=AAPL&days=365
```

**Response (200 OK)**:
```json
{
  "ticker": "AAPL",
  "start_date": "2025-06-01",
  "end_date": "2026-06-01",
  "count": 252,
  "latest_close": 178.52,
  "latest_volatility": 0.225,
  "data": [
    {
      "Date": "2025-06-01",
      "Open": 175.20,
      "High": 176.80,
      "Low": 174.50,
      "Close": 176.10,
      "Volume": 52000000,
      "Returns": 0.008,
      "Volatility_20d": 0.210
    },
    {
      "Date": "2025-06-02",
      "Open": 176.10,
      "High": 177.50,
      "Low": 175.80,
      "Close": 177.20,
      "Volume": 48000000,
      "Returns": 0.006,
      "Volatility_20d": 0.212
    },
    ...
  ]
}
```

**Error Responses**:
```json
// 400 Bad Request
{ "error": "Invalid ticker symbol" }

// 404 Not Found
{ "error": "No data found for ticker AAPL" }

// 500 Internal Server Error
{ "error": "yfinance API rate limit exceeded" }
```

---

### 4. `POST /api/predict`
**Generate AI volatility forecast** (core endpoint).

**Request Body**:
```json
{
  "ticker": "AAPL",
  "horizon": 5,
  "days_of_data": 365
}
```

**Parameters**:
| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `ticker` | string | Yes | — | Stock symbol |
| `horizon` | integer | No | `5` | Forecast days (1–30) |
| `days_of_data` | integer | No | `365` | Training data days (90–730) |

**Request**:
```http
POST /api/predict
Content-Type: application/json

{
  "ticker": "AAPL",
  "horizon": 10,
  "days_of_data": 365
}
```

**Response (200 OK)**:
```json
{
  "ticker": "AAPL",
  "horizon": 10,
  "latest_close": 178.52,
  "latest_volatility": 0.225,
  "forecast_generated_at": "2026-06-01T13:45:00Z",
  "forecast": {
    "dates": [
      "2026-06-02",
      "2026-06-03",
      "2026-06-04",
      "2026-06-05",
      "2026-06-06",
      "2026-06-07",
      "2026-06-08",
      "2026-06-09",
      "2026-06-10",
      "2026-06-11"
    ],
    "prices": [
      180.12,
      181.45,
      179.88,
      182.30,
      183.10,
      184.55,
      183.90,
      185.20,
      186.40,
      187.15
    ],
    "upper_bound_95": [
      185.20,
      187.50,
      186.10,
      189.80,
      191.50,
      193.80,
      193.00,
      195.40,
      197.60,
      199.20
    ],
    "lower_bound_95": [
      175.00,
      175.40,
      173.60,
      174.80,
      174.70,
      175.30,
      174.80,
      175.00,
      175.20,
      175.10
    ],
    "predicted_volatility": [
      0.228,
      0.230,
      0.232,
      0.234,
      0.236,
      0.238,
      0.240,
      0.242,
      0.244,
      0.246
    ]
  },
  "model_version": "lstm_v1.0.0",
  "accuracy_note": "Directional accuracy: 58% (1hr horizon)"
}
```

**Error Responses**:
```json
// 400 Bad Request
{ "error": "Horizon must be between 1 and 30" }

// 404 Not Found
{ "error": "No data found for ticker AAPL" }

// 500 Internal Server Error
{ "error": "LSTM model inference failed: GPU out of memory" }
```

---

### 5. `POST /api/train` (Phase 2+)
**Trigger model retraining** (admin-only).

**Request**:
```http
POST /api/train
Content-Type: application/json

{
  "ticker": "AAPL",
  "days_of_data": 365,
  "epochs": 100
}
```

**Response (202 Accepted)**:
```json
{
  "message": "Training job started",
  "job_id": "train_job_abc123",
  "estimated_completion": "2026-06-01T14:45:00Z"
}
```

**Poll for Status**: `GET /api/train/status/{job_id}`

---

### 6. `GET /api/metrics` (Phase 2+)
**Return real-time model performance metrics**.

**Request**:
```http
GET /api/metrics
```

**Response (200 OK)**:
```json
{
  "directional_accuracy_1hr": 0.58,
  "directional_accuracy_1day": 0.61,
  "volatility_rmse_ratio": 0.82,
  "liquidity_crash_recall": 0.85,
  "false_positive_rate": 0.04,
  "last_backtest_date": "2026-05-31",
  "model_version": "lstm_v1.0.0"
}
```

---

## Rate Limits

| Tier | Requests/Minute | Requests/Day |
|------|-----------------|--------------|
| **Free (demo)** | 10 | 100 |
| **Pro** | 100 | 10,000 |
| **Enterprise** | 1,000 | Unlimited |

**Rate Limit Headers**:
```http
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 7
X-RateLimit-Reset: 1685889900
```

---

## Error Codes

| Code | Meaning | Action |
|------|---------|--------|
| `400` | Bad Request | Check query/body parameters |
| `401` | Unauthorized | Add JWT token (Phase 2+) |
| `403` | Forbidden | Insufficient permissions |
| `404` | Not Found | Ticker doesn't exist |
| `429` | Too Many Requests | Wait and retry |
| `500` | Server Error | Contact support |
| `503` | Service Unavailable | API down for maintenance |

---

## SDK Examples

### Python
```python
import requests

response = requests.post("http://localhost:5000/api/predict", json={
    "ticker": "AAPL",
    "horizon": 5
})

forecast = response.json()
print(forecast["forecast"]["prices"])
```

### JavaScript (Fetch)
```javascript
fetch("http://localhost:5000/api/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ ticker: "AAPL", horizon: 5 })
})
  .then(res 
