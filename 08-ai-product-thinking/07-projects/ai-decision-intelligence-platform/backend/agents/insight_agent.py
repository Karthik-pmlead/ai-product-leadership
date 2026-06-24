def generate_insights(
    sentiment_score,
    metrics,
    anomalies,
    trends
):

    insights = []

    # -----------------------------------
    # SENTIMENT INSIGHTS
    # -----------------------------------
    if sentiment_score < 0:

        insights.append(
            "Customer sentiment trend is negative."
        )

    else:

        insights.append(
            "Customer sentiment appears stable."
        )

    # -----------------------------------
    # METRIC INSIGHTS
    # -----------------------------------
    if metrics["conversion_change"] < 0:

        insights.append(
            "Conversion performance declined."
        )

    if metrics["bounce_rate_change"] > 0:

        insights.append(
            "Bounce rate increased recently."
        )

    if metrics["checkout_failure_rate"] > 20:

        insights.append(
            "Checkout failures increased significantly."
        )

    if metrics["mobile_latency"] > 400:

        insights.append(
            "Mobile latency is above acceptable threshold."
        )

    # -----------------------------------
    # ANOMALY INSIGHTS
    # -----------------------------------
    if anomalies:

        insights.append(
            "Operational anomalies detected."
        )

    # -----------------------------------
    # TREND INSIGHTS
    # -----------------------------------
    declining_regions = trends["declining_regions"]

    if declining_regions:

        insights.append(
            f"Sales declining in: {', '.join(declining_regions)}"
        )

    return insights
