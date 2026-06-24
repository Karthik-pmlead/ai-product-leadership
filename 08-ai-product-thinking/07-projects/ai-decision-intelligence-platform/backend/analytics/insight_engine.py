def generate_insights(
    sentiment_score,
    metrics,
    anomalies,
    trends
):

    insights = []

    if sentiment_score < 0:
        insights.append(
            "Customer sentiment is trending negative."
        )

    if metrics["conversion_change"] < 0:
        insights.append(
            "Conversion performance declined."
        )

    if anomalies:
        insights.append(
            "Operational anomalies detected."
        )

    if trends["declining_regions"]:
        insights.append(
            f"Sales declining in: {', '.join(trends['declining_regions'])}"
        )

    return insights
