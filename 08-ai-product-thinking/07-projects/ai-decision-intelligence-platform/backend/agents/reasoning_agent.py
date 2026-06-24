def generate_reasoning(
    sentiment_score,
    anomalies,
    trends
):

    reasoning = []

    if sentiment_score < 0:
        reasoning.append(
            "Negative review sentiment contributed to the alert."
        )

    if anomalies:
        reasoning.append(
            "Operational anomalies amplified business risk."
        )

    if trends["declining_regions"]:
        reasoning.append(
            "Regional sales decline influenced overall performance."
        )

    return reasoning
