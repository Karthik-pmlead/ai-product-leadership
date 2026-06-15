def rank_signals(signals):
    severity_score = {
        "high": 3,
        "medium": 2,
        "low": 1
    }

    return sorted(
        signals,
        key=lambda x: severity_score.get(x["severity"], 1),
        reverse=True
    )
