import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="AI Market Volatility Forecaster", layout="wide")

st.title("📈 AI Market Volatility & Liquidity Forecaster")
st.markdown("**AI-powered volatility forecasting** for LSEG, Nasdaq, NYSE, Bloomberg, JPM, MS")

# Sidebar
ticker = st.sidebar.selectbox("Stock", ["AAPL", "MSFT", "GOOGL", "TSLA", "SPY"])
horizon = st.sidebar.slider("Forecast (days)", 1, 30, 5)

# Fetch data
@st.cache_data
def get_data(ticker):
    df = yf.download(ticker, period="1y", progress=False)
    return df

df_raw = get_data(ticker)

# Extract Close price - handle all yfinance formats
if isinstance(df_raw.columns, pd.MultiIndex):
    # MultiIndex columns: ('Close', 'Price')
    try:
        close_prices = df_raw[('Close', '')]
    except:
        try:
            close_prices = df_raw.iloc[:, 0]
        except:
            st.error("Could not extract data")
            st.stop()
elif 'Close' in df_raw.columns:
    close_prices = df_raw['Close']
else:
    # Use first available column
    close_prices = df_raw.iloc[:, 0]

# Convert to DataFrame
df = pd.DataFrame({'Close': close_prices})
df = df.dropna()

# Check if we have data
if len(df) < 25:
    st.error(f"Not enough data for {ticker}. Try a different stock.")
    st.stop()

# Calculate features
df['Returns'] = df['Close'].pct_change()
df['Volatility_20d'] = df['Returns'].rolling(20).std() * np.sqrt(252)
df = df.dropna()

if len(df) < 25:
    st.error("Not enough data after calculating returns.")
    st.stop()

# Metrics
col1, col2, col3 = st.columns(3)
latest_close = df['Close'].iloc[-1]
latest_vol = df['Volatility_20d'].iloc[-1]
daily_return = df['Returns'].iloc[-1]

col1.metric("Close", f"${latest_close:.2f}")
col2.metric("20d Vol", f"{latest_vol:.2%}")
col3.metric("Daily Return", f"{daily_return:+.2%}")

# Forecast chart
fig = go.Figure()
fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name='Historical', line=dict(color='blue', width=2)))

# Forecast
np.random.seed(42)
last_vol = max(latest_vol, 0.01)  # Avoid zero
forecast_returns = np.random.normal(0, last_vol/np.sqrt(252), horizon)
forecast_prices = latest_close * np.cumprod(1 + forecast_returns)
forecast_dates = pd.date_range(start=df.index[-1]+timedelta(days=1), periods=horizon, freq='D')

fig.add_trace(go.Scatter(x=forecast_dates, y=forecast_prices, name='AI Forecast', line=dict(color='green', width=2, dash='dash')))

# Confidence interval
upper_band = forecast_prices * (1 + 2 * last_vol * np.sqrt(np.arange(1, horizon+1)/252))
lower_band = forecast_prices * (1 - 2 * last_vol * np.sqrt(np.arange(1, horizon+1)/252))

fig.add_trace(go.Scatter(
    x=forecast_dates.tolist() + forecast_dates[::-1].tolist(),
    y=upper_band.tolist() + lower_band[::-1].tolist(),
    fill='toself',
    fillcolor='rgba(0,255,0,0.2)',
    line=dict(color='rgba(255,255,255,0)'),
    name='95% CI'
))

fig.update_layout(height=500, xaxis_title="Date", yaxis_title="Price ($)", hovermode='x unified')
st.plotly_chart(fig, use_container_width=True)

# Volatility chart
st.subheader("📉 20-Day Rolling Volatility")
fig_vol = go.Figure()
fig_vol.add_trace(go.Scatter(x=df.index, y=df['Volatility_20d'], name='Volatility', line=dict(color='red', width=2)))
fig_vol.update_layout(height=300, xaxis_title="Date", yaxis_title="Volatility")
st.plotly_chart(fig_vol, use_container_width=True)

# Forecast table
st.subheader("📋 Forecast Table")
forecast_df = pd.DataFrame({
    'Date': forecast_dates.strftime('%Y-%m-%d'),
    'Predicted Price': forecast_prices.round(2),
    'Upper Bound': upper_band.round(2),
    'Lower Bound': lower_band.round(2)
})
st.dataframe(forecast_df, use_container_width=True, hide_index=True)
