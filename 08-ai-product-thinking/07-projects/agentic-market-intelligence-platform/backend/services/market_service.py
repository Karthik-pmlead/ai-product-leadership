class MarketService:

    MARKET_DATA = {

        "Tesla": {
            "risks": [
                "Margin pressure from EV competition",
                "Supply chain volatility",
                "Regulatory uncertainty"
            ],
            "opportunities": [
                "Energy storage expansion",
                "Autonomous driving",
                "Global EV adoption growth"
            ]
        },

        "Nvidia": {
            "risks": [
                "Export restrictions",
                "Supply constraints",
                "AI chip competition"
            ],
            "opportunities": [
                "Enterprise AI demand",
                "Cloud infrastructure growth",
                "Generative AI expansion"
            ]
        },

        "Microsoft": {
            "risks": [
                "Cloud competition",
                "Regulatory scrutiny",
                "AI monetization pressure"
            ],
            "opportunities": [
                "Copilot adoption",
                "Azure growth",
                "Enterprise AI expansion"
            ]
        }
    }

    def get_company_intelligence(
        self,
        company: str
    ):

        return self.MARKET_DATA.get(
            company,
            {
                "risks": [
                    "Market uncertainty",
                    "Competitive pressure"
                ],
                "opportunities": [
                    "Market expansion",
                    "Product innovation"
                ]
            }
        )
