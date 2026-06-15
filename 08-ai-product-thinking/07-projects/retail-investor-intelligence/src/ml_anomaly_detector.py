import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(prices_df):
    """
    Uses Isolation Forest to detect anomalous stock movements.
    """

    df = prices_df.copy()

    # Feature needed for ML model
    X = df[["price_change_pct"]].fillna(0)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,   # assume 10% anomalies
        random_state=42
    )

    df["anomaly_score"] = model.fit_predict(X)

    # -1 = anomaly, 1 = normal
    df["is_anomaly"] = df["anomaly_score"].apply(lambda x: x == -1)

    return df
