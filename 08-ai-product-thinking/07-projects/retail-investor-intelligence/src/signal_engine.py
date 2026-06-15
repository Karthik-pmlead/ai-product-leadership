def generate_signals(prices, portfolio, ml_df=None):
    signals = []

    # --------------------------
    # RULE-BASED SIGNALS
    # --------------------------
    for _, row in prices.iterrows():
        if abs(row["price_change_pct"]) > 5:
            signals.append({
                "type": "price_spike",
                "stock": row["stock"],
                "value": row["price_change_pct"],
                "severity": "high"
            })

    # --------------------------
    # ML-BASED SIGNALS (Isolation Forest)
    # --------------------------
    if ml_df is not None:
        anomalies = ml_df[ml_df["is_anomaly"] == True]

        for _, row in anomalies.iterrows():
            signals.append({
                "type": "ml_anomaly",
                "stock": row["stock"],
                "value": row["price_change_pct"],
                "severity": "high",
                "source": "isolation_forest"
            })

    return signals
