def generate_actions(
    sentiment_score,
    metrics,
    anomalies
):

    actions = []

    if sentiment_score < 0:
        actions.append(
            "Review customer complaints and UX feedback."
        )

    if metrics["mobile_latency"] > 400:
        actions.append(
            "Investigate mobile performance bottlenecks."
        )

    if metrics["checkout_failure_rate"] > 20:
        actions.append(
            "Audit payment and checkout infrastructure."
        )

    if anomalies:
        actions.append(
            "Escalate anomalies to operations team."
        )

    return actions
