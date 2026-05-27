from pydantic import BaseModel


class RiskEvent(BaseModel):
    entity_id: str
    risk_delta: int
    reason: str
