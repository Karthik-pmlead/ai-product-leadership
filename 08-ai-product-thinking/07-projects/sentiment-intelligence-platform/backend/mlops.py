metrics = {
    "total_predictions": 0,
    "avg_confidence": 0,
    "language_distribution": {},
    "model_version": "v1.0-xlm-roberta"
}


def update_metrics(language, confidence):
    metrics["total_predictions"] += 1

    total = metrics["total_predictions"]

    current_avg = metrics["avg_confidence"]

    metrics["avg_confidence"] = round(
        ((current_avg * (total - 1)) + confidence) / total,
        2
    )

    if language not in metrics["language_distribution"]:
        metrics["language_distribution"][language] = 0

    metrics["language_distribution"][language] += 1


def get_metrics():
    return metrics
