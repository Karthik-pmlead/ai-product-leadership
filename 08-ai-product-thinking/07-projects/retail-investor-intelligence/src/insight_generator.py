def generate_insights(ranked_signals):
    insights = []

    for s in ranked_signals:
        if s["type"] == "price_spike":
            insights.append(
                f"{s['stock']} shows unusual price movement ({s['value']}%)"
            )

        elif s["type"] == "concentration_risk":
            insights.append(
                f"High portfolio concentration detected in {s['sector']} sector"
            )

    return insights
