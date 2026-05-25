import random

countries = [
    'US',
    'India',
    'Germany',
    'Brazil',
    'Singapore'
]

users = [
    'alice',
    'bob',
    'charlie',
    'david',
    'emma'
]



def generate_transaction(transaction_id):
    return {
        'id': transaction_id,
        'user': random.choice(users),
        'amount': random.randint(100, 10000),
        'country': random.choice(countries),
        'velocity_score': random.randint(0, 100),
        'geo_risk': random.randint(0, 100),
        'device_risk': random.randint(0, 100),
        'sanctions_match': random.randint(0, 100)
    }
