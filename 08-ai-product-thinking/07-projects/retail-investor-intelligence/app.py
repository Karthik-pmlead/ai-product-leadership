import streamlit as st
import pandas as pd

from src.data_loader import load_sample_data
from src.feature_engineering import compute_features
from src.ml_anomaly_detector import detect_anomalies
from src.signal_engine import generate_signals
from src.ranking_engine import rank_signals
from src.insight_generator import generate_insights
from src.portfolio_analyzer import generate_portfolio_insights

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Decision Intelligence Platform",
    layout="wide"
)

st.title("🧠 Decision Intelligence Platform")
st.subheader("AI + Analytics for Retail Investor Decision Support")

# -----------------------------
# LOAD DATA
# -----------------------------
prices, portfolio = load_sample_data()

# -----------------------------
# FEATURE ENGINEERING LAYER
# -----------------------------
prices_fe = compute_features(prices)

# -----------------------------
# ML ANOMALY DETECTION (Isolation Forest)
# -----------------------------
ml_prices = detect_anomalies(prices_fe)

# -----------------------------
# PORTFOLIO ANALYSIS LAYER
# -----------------------------
portfolio_insights = generate_portfolio_insights(portfolio)

# -----------------------------
# SIGNAL ENGINE (RULES + ML)
# -----------------------------
signals = generate_signals(prices_fe, portfolio, ml_prices)

# -----------------------------
# RANKING ENGINE
# -----------------------------
ranked_signals = rank_signals(signals)

# -----------------------------
# INSIGHT GENERATION
# -----------------------------
insights = generate_insights(ranked_signals)

# -----------------------------
# DASHBOARD UI
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("## 📁 Portfolio Overview")
    st.dataframe(portfolio)

    st.markdown("### 📊 Portfolio Intelligence")
    st.json(portfolio_insights)

with col2:
    st.markdown("## 📈 Market Data (Engineered Features)")
    st.dataframe(prices_fe.head(10))

    st.markdown("## 🤖 ML Anomaly Detection")
    st.dataframe(
        ml_prices[["stock", "price_change_pct", "is_anomaly"]].head(10)
    )

# -----------------------------
# TOP INSIGHTS SECTION
# -----------------------------
st.markdown("---")
st.markdown("## 🚨 Top 3 Decision Insights")

if insights:
    for i, ins in enumerate(insights[:3], 1):
        st.markdown(f"### {i}. {ins}")
else:
    st.write("No significant insights detected.")

# -----------------------------
# DEBUG / TRANSPARENCY LAYERS
# -----------------------------
with st.expander("🧠 Raw Signals (Rule + ML Combined)"):
    st.json(signals)

with st.expander("📊 Ranked Signals"):
    st.json(ranked_signals)

with st.expander("📉 ML Anomaly Output (Isolation Forest)"):
    st.dataframe(ml_prices)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    """
    🧠 Decision Intelligence System (Hybrid AI + Rules)  
    ⚙️ Feature Engineering + Signal Detection + ML Anomaly Layer  
    📊 Designed for retail investor decision acceleration  
    """
)
