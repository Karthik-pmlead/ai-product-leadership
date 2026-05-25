from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis"
)


def analyze_sentiment(text):
    result = classifier(text)[0]

    return {
        "sentiment": result["label"].upper(),
        "confidence": round(result["score"], 2)
    }
