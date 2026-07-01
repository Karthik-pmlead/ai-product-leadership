from services.llm_service import (
    LLMService
)

from services.retrieval_service import (
    RetrievalService
)


class RiskAgent:

    def __init__(self):

        self.llm = LLMService()

        self.retriever = (
            RetrievalService()
        )

    def analyze(
        self,
        company
    ):

        print(
            f"[RiskAgent] "
            f"Analyzing {company}"
        )

        retrieval = (
            self.retriever
            .retrieve_context(
                f"{company} risks",
                top_k=3
            )
        )

        context = retrieval[
            "context"
        ]

        sources = retrieval[
            "sources"
        ]

        prompt = f"""
You are a senior market
risk analyst.

Context:

{context}

Analyze the top
strategic risks for
{company}.

Return ONLY valid JSON.

{{
    "risks": [
        "risk1",
        "risk2",
        "risk3"
    ]
}}
"""

        result = (
            self.llm.generate_json(
                prompt
            )
        )

        if (
            result
            and
            "risks"
            in result
        ):

            return {
                "risks":
                    result["risks"],
                "sources":
                    sources
            }

        return {
            "risks": [
                "Market uncertainty",
                "Competitive pressure",
                "Execution risk"
            ],
            "sources":
                sources
        }
