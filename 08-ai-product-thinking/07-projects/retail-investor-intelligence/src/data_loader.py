import pandas as pd

def load_sample_data():
    prices = pd.read_csv("data/sample_prices.csv")
    portfolio = pd.read_csv("data/sample_portfolio.csv")
    return prices, portfolio
