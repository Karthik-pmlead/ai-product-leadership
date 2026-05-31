from flask import Blueprint, request, jsonify
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta
import torch
from ..models.lstm_forecaster import LSTMVolatilityForecaster, prepare_sequences
from ..utils.config import Config

api = Blueprint('api', __name__)

@api.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "AI Volatility Forecaster API",
        "version": "1.0.0"
    })

@api.route("/stocks", methods=["GET"])
def get_stocks():
    """Return list of available stocks."""
    return jsonify({"stocks": Config.AVAILABLE_STOCKS})

@api.route("/data", methods=["GET"])
def get_stock_data():
    """Fetch historical stock data."""
    ticker = request.args.get("ticker", "AAPL")
    days = int(request.args.get("days", Config.DEFAULT_DAYS))
    
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    
    try:
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        if df.empty:
            return jsonify({"error": "No data found"}), 404
        
        # Add features
        df['Returns'] = df['Close'].pct_change()
        df['Volatility_20d'] = df['Returns'].rolling(window=20).std() * np.sqrt(252)
        
        result = {
            "ticker": ticker,
            "data": df.reset_index().to_dict(orient="records"),
            "latest_close": float(df['Close'].iloc[-1]),
            "latest_volatility": float(df['Volatility_20d'].iloc[-1])
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route("/predict", methods=["POST"])
def predict():
    """
    Generate AI forecast.
    
    Request body:
    {
        "ticker": "AAPL",
        "horizon": 5,
        "days_of_data": 365
    }
    """
    data = request.get_json()
    ticker = data.get("ticker", "AAPL")
    horizon = int(data.get("horizon", Config.DEFAULT_HORIZON))
    days_of_data = int(data.get("days_of_data", Config.DEFAULT_DAYS))
    
    try:
        # Fetch historical data
        end_date = datetime.today()
        start_date = end_date - timedelta(days=days_of_data)
        
        df = yf.download(ticker, start=start_date, end=end_date, progress=False)
        
        if df.empty:
            return jsonify({"error": "No data found"}), 404
        
        # Calculate volatility
        df['Returns'] = df['Close'].pct_change()
        last_vol = df['Returns'].rolling(window=20).std().iloc[-1] * np.sqrt(252)
        last_price = df['Close'].iloc[-1]
        
        # Generate forecast (replace with LSTM in production)
        np.random.seed(42)
        forecast_returns = np.random.normal(0, last_vol/np.sqrt(252), horizon)
        forecast_prices = last_price * np.cumprod(1 + forecast_returns)
        
        forecast_dates = pd.date_range(
            start=df.index[-1] + pd.Timedelta(days=1),
            periods=horizon,
            freq='D'
        )
        
        # Confidence intervals
        upper_band = forecast_prices * (1 + 2 * last_vol * np.sqrt(np.arange(1, horizon+1)/252))
        lower_band = forecast_prices * (1 - 2 * last_vol * np.sqrt(np.arange(1, horizon+1)/252))
        
        result = {
            "ticker": ticker,
            "horizon": horizon,
            "latest_close": float(last_price),
            "latest_volatility": float(last_vol),
            "forecast": {
                "dates": forecast_dates.strftime('%Y-%m-%d').tolist(),
                "prices": forecast_prices.round(2).tolist(),
                "upper_bound": upper_band.round(2).tolist(),
                "lower_bound": lower_band.round(2).tolist()
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@api.route("/train", methods=["POST"])
def train():
    """Train/retrain LSTM model (demo endpoint)."""
    return jsonify({
        "message": "Training endpoint - implement LSTM training in production",
        "status": "demo"
    })
