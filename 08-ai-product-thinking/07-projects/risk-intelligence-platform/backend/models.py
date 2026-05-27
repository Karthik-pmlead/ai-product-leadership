from pydantic import BaseModel
from typing import List


class Transaction(BaseModel):
    id: int
    user: str
    amount: float
    country: str
    velocity_score: float
    geo_risk: float
    device_risk: float
    sanctions_match: float
    risk_score: float


class Alert(BaseModel):
    id: int
    transaction_id: int
    risk_score: float
    risk_level: str
    reasons: List[str]
