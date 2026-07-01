from services.llm_service import LLMService
from services.prompt_service import PromptService


class RecommendationAgent:

    def __init__(self):

        self.llm = LLMService()

    def generate(
        self,
        company,
        risks,
        opportunities
    ):

        prompt = (
            PromptService
            .recommendation_prompt(
                company,
                risks,
                opportunities
            )
        )

        result = (
            self.llm.generate_json(
                prompt
            )
        )

        if (
            result
            and
            "recommendations"
            in result
        ):
            return result[
                "recommendations"
            ]

        return [
            "Monitor competitors",
            "Invest in innovation",
            "Review strategic roadmap"
        ]
