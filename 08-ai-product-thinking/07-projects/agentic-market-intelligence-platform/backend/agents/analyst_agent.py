from services.market_service import MarketService

class AnalystAgent:

    def __init__(self):
        self.market_service = MarketService()

    def analyze(
        self,
        company: str,
        plan: dict
    ):

        return self.market_service.get_company_intelligence(
            company
        )
