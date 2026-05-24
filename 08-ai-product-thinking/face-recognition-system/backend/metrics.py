from collections import defaultdict
from datetime import datetime

METRICS = {
    "total_auth": 0,
    "success": 0,
    "failed": 0,
    "scores": [],
    "hourly_hits": defaultdict(int)
}

def log_auth(success: bool, score: float):
    METRICS["total_auth"] += 1

    if success:
        METRICS["success"] += 1
    else:
        METRICS["failed"] += 1

    METRICS["scores"].append(score)

    hour = datetime.utcnow().hour
    METRICS["hourly_hits"][hour] += 1


def get_metrics():
    total = METRICS["total_auth"]
    success = METRICS["success"]
    failed = METRICS["failed"]

    avg_score = (
        sum(METRICS["scores"]) / len(METRICS["scores"])
        if METRICS["scores"]
        else 0
    )

    return {
        "total_auth": total,
        "success_rate": round(success / total * 100, 2) if total else 0,
        "failure_rate": round(failed / total * 100, 2) if total else 0,
        "avg_confidence": round(avg_score * 100, 2),
        "hourly_hits": dict(METRICS["hourly_hits"])
    }
