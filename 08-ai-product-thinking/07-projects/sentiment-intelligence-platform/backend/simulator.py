import random

REVIEWS = [
    {
        "language": "English",
        "text": "Delivery was delayed and packaging was damaged."
    },

    {
        "language": "Hindi",
        "text": "डिलीवरी बहुत लेट थी और प्रोडक्ट खराब था"
    },

    {
        "language": "Tamil",
        "text": "டெலிவரி மிகவும் தாமதமாக வந்தது"
    },

    {
        "language": "Spanish",
        "text": "La entrega fue rápida y excelente."
    },

    {
        "language": "English",
        "text": "Amazing product quality and fast shipping."
    },

    {
        "language": "English",
        "text": "Fake product received. Very disappointed."
    }
]


def generate_review(review_id):
    review = random.choice(REVIEWS)

    return {
        "id": review_id,
        "language": review["language"],
        "text": review["text"]
    }
