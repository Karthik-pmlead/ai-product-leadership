from data.sample_metrics import metrics


def analyze_metrics():

    return {
        "conversion_change":
            metrics["conversion_rate_change"],

        "bounce_rate_change":
            metrics["bounce_rate_change"],

        "checkout_failure_rate":
            metrics["checkout_failure_rate"],

        "mobile_latency":
            metrics["mobile_latency_ms"]
    }
