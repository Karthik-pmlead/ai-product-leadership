from services.llm_service import (
    LLMService
)

from services.retrieval_service import (
    RetrievalService
)


class OpportunityAgent:

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
            f"[OpportunityAgent] "
            f"Analyzing {company}"
        )

        retrieval = (
            self.retriever
            .retrieve_context(
                f"{company} opportunities",
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
You are a corporate
strategy analyst.

Context:

{context}

Identify the top growth
opportunities for
{company}.

Return ONLY valid JSON.

{{
    "opportunities": [
        "opportunity1",
        "opportunity2",
        "opportunity3"
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
            "opportunities"
            in result
        ):

            return {
                "opportunities":
                    result[
                        "opportunities"
                    ],
                "sources":
                    sources
            }

        return {
            "opportunities": [
                "AI adoption",
                "Market expansion",
                "Product innovation"
            ],
            "sources":
                sources
        }
