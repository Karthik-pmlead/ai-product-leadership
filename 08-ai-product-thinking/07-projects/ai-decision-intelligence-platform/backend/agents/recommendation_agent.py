def generate_actions(
    sentiment_score,
    metrics,
    anomalies
):

    actions = []

    # -----------------------------------
    # SENTIMENT-BASED ACTIONS
    # -----------------------------------
    if sentiment_score < 0:

        actions.append(
            "Investigate negative customer feedback trends."
        )

        actions.append(
            "Review checkout and mobile UX flows."
        )

    # -----------------------------------
    # METRIC-BASED ACTIONS
    # -----------------------------------
    if metrics["conversion_change"] < 0:

        actions.append(
            "Analyze conversion funnel drop-off points."
        )

    if metrics["checkout_failure_rate"] > 20:

        actions.append(
            "Audit payment gateway reliability."
        )

    if metrics["mobile_latency"] > 400:

        actions.append(
            "Optimize mobile application performance."
        )

    # -----------------------------------
    # ANOMALY-BASED ACTIONS
    # -----------------------------------
    if anomalies:

        actions.append(
            "Escalate anomalies to operations team."
        )

    return actions
