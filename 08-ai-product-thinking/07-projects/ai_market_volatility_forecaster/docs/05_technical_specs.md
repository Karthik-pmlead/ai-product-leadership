# 5. Technical Specifications

## 5.1 System Architecture
```
┌─────────────────────────────────────────────────────────────┐
│ Streamlit Dashboard │
│ (Stock Selector, Forecast Chart, Vol Chart, Metrics) │
└──────────────────────┬──────────────────────────────────────┘
│ HTTP/REST
▼
┌─────────────────────────────────────────────────────────────┐
│ Flask API │
│ Endpoints: /api/predict, /api/data, /api/health, /api/stocks│
└──────────────────────┬──────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ LSTM Forecaster │
│ PyTorch Model: input=60-day seq, hidden=64, layers=2 │
└──────────────────────┬──────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ yfinance │
│ Real-time OHLCV data (AAPL, MSFT, GOOGL, TSLA, SPY) │
└─────────────────────────────────────────────────────────────┘
```


---

## 5.2 ML Model Architecture

### LSTM Model Definition (`backend/app/models/lstm_forecaster.py`)

```python
import torch
import torch.nn as nn

class LSTMVolatilityForecaster(nn.Module):
    """LSTM for time-series volatility forecasting."""
    
    def __init__(self, input_size=1, hidden_size=64, num_layers=2, output_size=1):
        super().__init__()
        
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # LSTM layer
        self.lstm = nn.LSTM(
            input_size=input_size,
            hidden_size=hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=0.2  # 20% dropout to prevent overfitting
        )
        
        # Fully connected layers
        self.fc = nn.Sequential(
            nn.Linear(hidden_size, 32),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(32, output_size)
        )
    
    def forward(self, x):
        # LSTM output: (batch, seq_len, hidden_size)
        lstm_out, (h_n, c_n) = self.lstm(x)
        
        # Use last hidden state
        out = self.fc(lstm_out[:, -1, :])
        
        return out
```

**Hyperparameters**:
| Parameter | Value | Reason |
|-----------|-------|--------|
| `input_size` | 1 | Single feature (price or return) |
| `hidden_size` | 64 | Balance between capacity and overfitting |
| `num_layers` | 2 | Deeper than 1, but not too deep (vanishing gradient) |
| `dropout` | 0.2 | Regularization (20% neurons dropped per batch) |
| `seq_length` | 60 | 60-day lookback (~3 months of trading days) |
| `output_size` | 1 | Single prediction (next-day volatility) |

---

### Training Pipeline

```python
def train_lstm(X_train, y_train, epochs=100, batch_size=32, lr=0.001):
    model = LSTMVolatilityForecaster()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        for batch_X, batch_y in zip(X_batches, y_batches):
            optimizer.zero_grad()
            output = model(batch_X)
            loss = criterion(output, batch_y)
            loss.backward()
            optimizer.step()
        
        if (epoch + 1) % 20 == 0:
            print(f"Epoch {epoch+1}, Loss: {loss.item():.6f}")
    
    return model
```

**Training Details**:
| Aspect | Specification |
|--------|---------------|
| **Loss Function** | Mean Squared Error (MSE) |
| **Optimizer** | Adam (lr=0.001) |
| **Batch Size** | 32 |
| **Epochs** | 100 (early stopping if val_loss doesn't improve) |
| **Learning Rate** | 0.001 (reduce on plateau if val_loss stagnates) |
| **Validation Split** | 20% of data (walk-forward, not random) |
| **Early Stopping** | Patience=10 epochs (stop if val_loss plateau) |

---

### Data Preprocessing

```python
from sklearn.preprocessing import MinMaxScaler

def prepare_sequences(data, seq_length=60):
    """Prepare sequences for LSTM."""
    # Scale to[1]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.reshape(-1, 1))
    
    # Create sequences
    X, y = [], []
    for i in range(len(scaled_data) - seq_length):
        X.append(scaled_data[i:i+seq_length])
        y.append(scaled_data[i+seq_length])
    
    return np.array(X), np.array(y), scaler
```

**Features Used**:
| Feature | Description | Normalization |
|---------|-------------|---------------|
| `Close` | Closing price | MinMax [0,1] |
| `Returns` | Daily pct_change | Standard (z-score) |
| `Volatility_20d` | 20-day rolling vol | MinMax [0,1] |
| `RSI` | 14-day RSI | MinMax [0,1] |
| `Volume` | Trading volume | Log transform + MinMax |

---

## 5.3 API Specifications

### Endpoint: `/api/predict` (POST)

**Request**:
```json
{
  "ticker": "AAPL",
  "horizon": 5,
  "days_of_data": 365
}
```

**Response**:
```json
{
  "ticker": "AAPL",
  "horizon": 5,
  "latest_close": 178.52,
  "latest_volatility": 0.225,
  "forecast": {
    "dates": ["2026-06-01", "2026-06-02", "2026-06-03", "2026-06-04", "2026-06-05"],
    "prices": [180.12, 181.45, 179.88, 182.30, 183.10],
    "upper_bound": [185.20, 187.50, 186.10, 189.80, 191.50],
    "lower_bound": [175.00, 175.40, 173.60, 174.80, 174.70]
  }
}
```

**Error Response**:
```json
{
  "error": "No data found for ticker"
}
```

---

### Endpoint: `/api/data` (GET)

**Request**:
```
GET /api/data?ticker=MSFT&days=365
```

**Response**:
```json
{
  "ticker": "MSFT",
  "latest_close": 420.15,
  "latest_volatility": 0.185,
  "data": [
    {"Date": "2025-06-01", "Close": 410.20, "Volatility_20d": 0.180},
    {"Date": "2025-06-02", "Close": 412.50, "Volatility_20d": 0.182},
    ...
  ]
}
```

---

### Endpoint: `/api/health` (GET)

**Response**:
```json
{
  "status": "healthy",
  "service": "AI Volatility Forecaster API",
  "version": "1.0.0"
}
```

---

## 5.4 Performance SLAs

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Forecast Latency** | <100ms (1min horizon) | Time from request to response |
| **API Uptime** | 99.9% | Monthly (downtime <43min/month) |
| **Model Accuracy** | 58–62% directional | Rolling 30-day backtest |
| **Data Freshness** | <1 minute delay | Time from market close to data available |
| **Dashboard Load Time** | <3 seconds | From click to fully rendered |
| **Error Rate** | <0.1% | Failed requests / total requests |

---

## 5.5 Infrastructure

### MVP (Phase 1)
| Component | Technology | Cost |
|-----------|------------|------|
| **Frontend** | Streamlit (localhost) | $0 |
| **Backend** | Flask (localhost) | $0 |
| **ML** | PyTorch (CPU/GPU) | $0 (local GPU) |
| **Data** | yfinance (free) | $0 |
| **Hosting** | Local machine | $0 |

### Production (Phase 3)
| Component | Technology | Cost |
|-----------|------------|------|
| **Frontend** | React + CDN | $50/month (Vercel) |
| **Backend** | Flask + Gunicorn + Nginx | $200/month (AWS EC2) |
| **ML** | PyTorch + GPU (p3.2xlarge) | $900/month (AWS) |
| **Data** | kdb+ license + Bloomberg API | $75,000/year |
| **Database** | kdb+ time-series | $50,000/year |
| **Monitoring** | Prometheus + Grafana | $100/month |
| **Total** | — | **~$130,000/year** |

---

## 5.6 Security & Compliance

| Requirement | Implementation |
|-------------|----------------|
| **API Authentication** | JWT tokens (Phase 2), API keys (Phase 3) |
| **Data Encryption** | TLS 1.3 (HTTPS) for all API calls |
| **Audit Trail** | Log all predictions (who, when, what) |
| **GDPR** | Anonymize trader data, data retention policy (Phase 3) |
| **MiFID II Art. 17** | Algorithmic trading risk controls documented [web:16] |
| **SEC Rule 15c3-5** | Market risk control logs retained 7 years |

---

## 5.7 Integration Points

| System | Integration Method | Purpose |
|--------|-------------------|---------|
| **Bloomberg Terminal** | Bloomberg API (BLPAPI) | Fetch implied volatility (IV) surface |
| **Refinitiv Eikon** | Refinitiv API | Alternative data source |
| **FIX Protocol** | FIX 4.4 | Connect to trading systems (Phase 3) |
| **Kdb+** | kdb+ Python API | Time-series database (Phase 3) |
| **Slack/Teams** | Webhooks | SNS alerts for volatility spikes |
| **Risk Systems** | REST API | Push VaR, stress test results |
