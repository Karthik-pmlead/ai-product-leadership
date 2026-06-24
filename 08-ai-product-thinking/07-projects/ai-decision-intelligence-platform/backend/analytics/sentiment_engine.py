from data.sample_reviews import reviews


POSITIVE_WORDS = [
    "improved",
    "good",
    "fast",
    "great",
    "excellent"
]

NEGATIVE_WORDS = [
    "slow",
    "failing",
    "irrelevant",
    "delayed",
    "confusing",
    "timeout",
    "degradation",
    "latency"
]


def analyze_sentiment():

    score = 0

    for review in reviews:

        text = review.lower()

        for word in POSITIVE_WORDS:

            if word in text:
                score += 1

        for word in NEGATIVE_WORDS:

            if word in text:
                score -= 1

    return score
