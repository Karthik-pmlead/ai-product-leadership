from data.sample_metrics import metrics
from data.sample_incidents import incidents


def detect_anomalies():

    anomalies = []

    if metrics["checkout_failure_rate"] > 20:
        anomalies.append(
            "Checkout failure rate spike detected."
        )

    if metrics["mobile_latency_ms"] > 400:
        anomalies.append(
            "High mobile latency detected."
        )

    if len(incidents) > 2:
        anomalies.append(
            "Operational incident volume elevated."
        )

    return anomalies
