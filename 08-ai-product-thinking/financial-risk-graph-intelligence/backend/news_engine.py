import random
from data.sample_news import sample_news
from risk_engine import propagate_risk


def simulate_news_event():

    news = random.choice(sample_news)

    impact = int(abs(news["sentiment"]) * 50)

    if news["sentiment"] < 0:
        propagate_risk(news["entity"], impact)

    return {
        "headline": news["headline"],
        "entity": news["entity"],
        "impact": impact
    }
