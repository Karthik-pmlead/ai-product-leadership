def generate_explanation(insights):

    explanations = []

    if insights["sentiment_score"] < 0:
        explanations.append(
            "Customer sentiment trend is negative."
        )

    if insights["conversion_change"] < 0:
        explanations.append(
            "Conversion metrics show a decline."
        )

    if insights["incident_count"] > 2:
        explanations.append(
            "Operational incidents increased recently."
        )

    return explanations
