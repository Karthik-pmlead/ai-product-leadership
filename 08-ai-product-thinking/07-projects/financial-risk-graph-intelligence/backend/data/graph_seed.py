nodes = [
    {"id": "bank_a", "label": "Bank A", "type": "Bank", "risk": 20},
    {"id": "fund_x", "label": "Fund X", "type": "Hedge Fund", "risk": 15},
    {"id": "exchange_z", "label": "Exchange Z", "type": "Exchange", "risk": 10},
    {"id": "trader_k", "label": "Trader K", "type": "Trader", "risk": 5},
    {"id": "company_q", "label": "Company Q", "type": "Company", "risk": 8},
]

edges = [
    ("bank_a", "fund_x"),
    ("fund_x", "exchange_z"),
    ("exchange_z", "trader_k"),
    ("fund_x", "company_q"),
]
