def calculate_risk(transaction):
    score = (
        transaction['velocity_score'] * 0.25 +
        transaction['geo_risk'] * 0.20 +
        transaction['device_risk'] * 0.20 +
        transaction['amount'] / 1000 * 0.20 +
        transaction['sanctions_match'] * 0.15
    )

    return min(round(score, 2), 100)



def get_risk_level(score):
    if score >= 70:
        return 'HIGH'

    if score >= 40:
        return 'MEDIUM'

    return 'LOW'



def explain_risk(transaction):
    reasons = []

    if transaction['velocity_score'] > 70:
        reasons.append('High transaction velocity detected')

    if transaction['geo_risk'] > 60:
        reasons.append('Geo mismatch identified')

    if transaction['device_risk'] > 60:
        reasons.append('Untrusted device fingerprint')

    if transaction['amount'] > 5000:
        reasons.append('Abnormally high transaction amount')

    if transaction['sanctions_match'] > 50:
        reasons.append('Potential sanctions watchlist match')

    return reasons
