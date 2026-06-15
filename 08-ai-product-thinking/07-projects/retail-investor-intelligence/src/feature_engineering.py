import pandas as pd

def compute_features(prices_df):
    """
    Convert raw price data into meaningful features
    """

    df = prices_df.copy()

    # % change (core signal feature)
    df["price_change_pct"] = df.groupby("stock")["price"].pct_change() * 100

    # Rolling volatility (simple signal support)
    df["volatility_3d"] = df.groupby("stock")["price"].rolling(3).std().reset_index(0, drop=True)

    # Moving average trend
    df["ma_3"] = df.groupby("stock")["price"].rolling(3).mean().reset_index(0, drop=True)

    return df
