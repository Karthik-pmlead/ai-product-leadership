def generate_recommendations(insights):

    recommendations = []

    if insights["sentiment_score"] < 0:
        recommendations.append(
            "Investigate negative customer feedback."
        )

    if insights["conversion_change"] < 0:
        recommendations.append(
            "Analyze checkout funnel performance."
        )

    if insights["incident_count"] > 2:
        recommendations.append(
            "Escalate operational reliability review."
        )

    return recommendations
