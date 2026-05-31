import numpy as np
import pandas as pd

def realized_volatility(returns, annualize=True):
    """Calculate annualized realized volatility."""
    vol = returns.std()
    if annualize:
        vol = vol * np.sqrt(252)
    return vol

def rolling_volatility(df, window=20, annualize=True):
    """Calculate rolling realized volatility."""
    returns = df['Close'].pct_change()
    vol = returns.rolling(window=window).std()
    
    if annualize:
        vol = vol * np.sqrt(252)
    
    return vol

def forecast_volatility_ewma(df, window=20):
    """Simple EWMA volatility forecast."""
    returns = df['Close'].pct_change().dropna()
    vol = returns.ewm(span=window).std()
    return vol * np.sqrt(252)

def forecast_volatility_simple(last_vol, horizon_days):
    """Simple volatility forecast (sqrt(t) scaling)."""
    return last_vol * np.sqrt(horizon_days / 252)

def calculate_sharpe_ratio(returns, risk_free_rate=0.02):
    """Calculate Sharpe ratio."""
    excess_return = returns.mean() * 252 - risk_free_rate
    volatility = returns.std() * np.sqrt(252)
    return excess_return / volatility if volatility != 0 else 0

def calculate_max_drawdown(prices):
    """Calculate maximum drawdown."""
    rolling_max = prices.cummax()
    drawdown = (prices - rolling_max) / rolling_max
    return drawdown.min()
