class DynamicPlanner:

    def create_plan(self, intent: str):

        if intent == "company_analysis":

            return [
                "risk",
                "opportunity",
                "recommendation"
            ]

        if intent == "competitor_analysis":

            return [
                "competitor",
                "risk",
                "opportunity",
                "recommendation"
            ]

        return [
            "risk",
            "opportunity"
        ]
