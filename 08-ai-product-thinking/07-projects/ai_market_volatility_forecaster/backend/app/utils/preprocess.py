import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def scale_data(data):
    """Scale data to [0, 1] range."""
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled = scaler.fit_transform(data.reshape(-1, 1))
    return scaled, scaler

def inverse_scale(scaled_data, scaler):
    """Inverse transform scaled data."""
    return scaler.inverse_transform(scaled_data.reshape(-1, 1))

def create_sequences(data, seq_length):
    """Create sequences for LSTM."""
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

def add_technical_features(df):
    """Add technical features for ML model."""
    df = df.copy()
    
    # Returns
    df['Returns'] = df['Close'].pct_change()
    
    # Volatility
    df['Volatility_20d'] = df['Returns'].rolling(window=20).std()
    df['Volatility_50d'] = df['Returns'].rolling(window=50).std()
    
    # Moving averages
    df['MA_20'] = df['Close'].rolling(window=20).mean()
    df['MA_50'] = df['Close'].rolling(window=50).mean()
    
    # Price vs MA
    df['Price_MA20_Ratio'] = df['Close'] / df['MA_20']
    df['Price_MA50_Ratio'] = df['Close'] / df['MA_50']
    
    # RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    exp1 = df['Close'].ewm(span=12, adjust=False).mean()
    exp2 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = exp1 - exp2
    
    # Volume features
    if 'Volume' in df.columns:
        df['Volume_MA_20'] = df['Volume'].rolling(window=20).mean()
        df['Volume_Ratio'] = df['Volume'] / df['Volume_MA_20']
    
    return df.dropna()

def normalize_features(df, columns=None):
    """Normalize specific columns."""
    if columns is None:
        columns = ['Returns', 'Volatility_20d', 'RSI', 'MACD']
    
    df = df.copy()
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df, scaler
