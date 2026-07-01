from services.llm_service import LLMService
from services.retrieval_service import RetrievalService


class CompetitorAgent:

    def __init__(self):

        self.llm = LLMService()

        self.retriever = RetrievalService()

    def analyze(
        self,
        company_a,
        company_b
    ):

        query = f"{company_a} {company_b} competition comparison"

        retrieval = (
            self.retriever.retrieve_context(
                query,
                top_k=5
            )
        )

        context = retrieval["context"]
        sources = retrieval["sources"]

        prompt = f"""
You are a senior equity research analyst.

Compare the following companies:

Company A: {company_a}
Company B: {company_b}

Context:
{context}

Return ONLY JSON:

{{
  "company_a_strengths": [],
  "company_b_strengths": [],
  "key_differences": [],
  "strategic_risks": [],
  "winner": ""
}}
"""

        result = self.llm.generate_json(prompt)

        if result:

            return {
                "comparison": result,
                "sources": sources
            }

        return {
            "comparison": {
                "company_a_strengths": [],
                "company_b_strengths": [],
                "key_differences": [],
                "strategic_risks": [],
                "winner": "unknown"
            },
            "sources": sources
        }
