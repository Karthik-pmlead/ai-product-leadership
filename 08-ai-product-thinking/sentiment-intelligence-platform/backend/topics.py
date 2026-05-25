TOPIC_RULES = {
    "Logistics": [
        "delivery",
        "shipping",
        "late",
        "delay"
    ],

    "Product Quality": [
        "broken",
        "damaged",
        "poor quality",
        "defect"
    ],

    "Customer Support": [
        "refund",
        "support",
        "service"
    ],

    "Trust & Safety": [
        "fake",
        "scam",
        "fraud"
    ]
}


def detect_topic(text):
    lower_text = text.lower()

    for topic, keywords in TOPIC_RULES.items():
        for keyword in keywords:
            if keyword in lower_text:
                return topic

    return "General"
