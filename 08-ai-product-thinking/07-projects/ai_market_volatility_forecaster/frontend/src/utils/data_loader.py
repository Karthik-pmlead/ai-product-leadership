import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def fetch_stock_data(ticker, start=None, end=None, period="1y"):
    """Fetch stock data from yfinance."""
    if start is None:
        start = datetime.today() - timedelta(days=365)
    if end is None:
        end = datetime.today()
    
    try:
        data = yf.download(ticker, start=start, end=end, progress=False)
        if data.empty:
            return None
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def calculate_volatility(df, window=20, annualize=True):
    """Calculate rolling realized volatility."""
    df = df.copy()
    df['Returns'] = df['Close'].pct_change()
    vol = df['Returns'].rolling(window=window).std()
    
    if annualize:
        vol = vol * (252 ** 0.5)
    
    df['Volatility'] = vol
    return df

def prepare_sequences(data, seq_length=60):
    """Prepare sequences for LSTM."""
    from sklearn.preprocessing import MinMaxScaler
    import numpy as np
    
    close_prices = data['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(close_prices)
    
    X, y = [], []
    for i in range(len(scaled_data) - seq_length):
        X.append(scaled_data[i:i+seq_length])
        y.append(scaled_data[i+seq_length])
    
    return np.array(X), np.array(y), scaler

def get_available_stocks():
    """Return list of popular stocks for demo."""
    return ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY", "AMZN", "NVDA", "META", "JPM", "BAC"]
