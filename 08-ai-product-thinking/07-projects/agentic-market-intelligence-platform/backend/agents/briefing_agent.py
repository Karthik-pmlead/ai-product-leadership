from services.llm_service import LLMService
from services.prompt_service import PromptService


class BriefingAgent:

    def __init__(self):

        self.llm = LLMService()

    def generate(
        self,
        company,
        risks,
        opportunities,
        recommendations
    ):

        prompt = (
            PromptService
            .executive_brief_prompt(
                company,
                risks,
                opportunities,
                recommendations
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
            "summary"
            in result
        ):
            summary = result[
                "summary"
            ]

        else:

            summary = (
                f"{company} faces "
                f"strategic risks while "
                f"benefiting from growth "
                f"opportunities."
            )

        return {
            "summary": summary,
            "risks": risks,
            "opportunities":
                opportunities,
            "recommendations":
                recommendations
        }
