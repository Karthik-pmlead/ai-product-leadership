import pandas as pd

def compute_portfolio_exposure(portfolio_df):
    """
    Computes portfolio-level exposure metrics
    for decision intelligence signals.
    """

    df = portfolio_df.copy()

    # Total portfolio value (assuming quantity-based proxy)
    df["position_value"] = df["quantity"]

    total_value = df["position_value"].sum()

    # Sector weight
    sector_exposure = (
        df.groupby("sector")["position_value"]
        .sum()
        .reset_index()
    )

    sector_exposure["weight_pct"] = (
        sector_exposure["position_value"] / total_value * 100
    )

    return sector_exposure


def detect_concentration_risk(sector_exposure_df, threshold=40):
    """
    Detects over-concentration risk in any sector.
    """

    risks = []

    for _, row in sector_exposure_df.iterrows():
        if row["weight_pct"] > threshold:
            risks.append({
                "type": "concentration_risk",
                "sector": row["sector"],
                "weight_pct": round(row["weight_pct"], 2),
                "severity": "high" if row["weight_pct"] > 50 else "medium"
            })

    return risks


def compute_diversification_score(sector_exposure_df):
    """
    Simple diversification heuristic:
    Higher score = more diversified portfolio.
    """

    # Herfindahl-style concentration proxy
    weights = sector_exposure_df["weight_pct"] / 100
    concentration_index = (weights ** 2).sum()

    diversification_score = round(1 - concentration_index, 3)

    return {
        "diversification_score": diversification_score,
        "interpretation": (
            "High diversification"
            if diversification_score > 0.7
            else "Moderate/Low diversification"
        )
    }


def generate_portfolio_insights(portfolio_df):
    """
    End-to-end wrapper for portfolio intelligence signals.
    """

    sector_exposure = compute_portfolio_exposure(portfolio_df)
    risks = detect_concentration_risk(sector_exposure)
    diversification = compute_diversification_score(sector_exposure)

    return {
        "sector_exposure": sector_exposure.to_dict(orient="records"),
        "risks": risks,
        "diversification": diversification
    }
