class PlannerAgent:

    def plan(self, intent):

        if intent == "company_analysis":

            return [
                "Risk Analysis",
                "Opportunity Analysis",
                "Recommendation Generation",
                "Executive Briefing"
            ]

        return [
            "General Analysis"
        ]
