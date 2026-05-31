from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"})

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    ticker = data.get("ticker", "AAPL")
    horizon = int(data.get("horizon", 5))
    
    df = yf.download(ticker, period="1y", progress=False)
    df['Returns'] = df['Close'].pct_change()
    last_vol = df['Returns'].rolling(20).std().iloc[-1] * np.sqrt(252)
    last_price = df['Close'].iloc[-1]
    
    np.random.seed(42)
    forecast_prices = last_price * np.cumprod(1 + np.random.normal(0, last_vol/np.sqrt(252), horizon))
    forecast_dates = pd.date_range(start=df.index[-1]+timedelta(days=1), periods=horizon, freq='D')
    
    return jsonify({
        "ticker": ticker,
        "forecast_dates": forecast_dates.strftime('%Y-%m-%d').tolist(),
        "forecast_prices": forecast_prices.round(2).tolist()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
