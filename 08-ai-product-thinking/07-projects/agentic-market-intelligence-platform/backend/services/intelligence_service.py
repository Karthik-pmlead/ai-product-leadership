class IntelligenceService:

    def generate_summary(
        self,
        company: str,
        risks: list,
        opportunities: list
    ):

        return (
            f"{company} faces strategic risks including "
            f"{risks[0].lower()} while benefiting from "
            f"{opportunities[0].lower()}."
        )

    def generate_recommendations(self):

        return [
            "Monitor competitor activity",
            "Track growth initiatives",
            "Review operational risks"
        ]
