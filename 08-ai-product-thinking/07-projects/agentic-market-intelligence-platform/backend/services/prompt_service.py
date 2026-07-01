class PromptService:

    @staticmethod
    def risk_prompt(company: str):

        return f"""
You are a senior market risk analyst.

Analyze the top strategic risks facing {company}.

Return ONLY valid JSON.

{{
  "risks": [
    "risk 1",
    "risk 2",
    "risk 3"
  ]
}}
"""

    @staticmethod
    def opportunity_prompt(company: str):

        return f"""
You are a corporate strategy analyst.

Identify the top growth opportunities for {company}.

Return ONLY valid JSON.

{{
  "opportunities": [
    "opportunity 1",
    "opportunity 2",
    "opportunity 3"
  ]
}}
"""

    @staticmethod
    def recommendation_prompt(
        company: str,
        risks,
        opportunities
    ):

        return f"""
You are a strategy consultant.

Company:
{company}

Risks:
{risks}

Opportunities:
{opportunities}

Generate executive recommendations.

Return ONLY valid JSON.

{{
  "recommendations": [
    "recommendation 1",
    "recommendation 2",
    "recommendation 3"
  ]
}}
"""

    @staticmethod
    def executive_brief_prompt(
        company: str,
        risks,
        opportunities,
        recommendations
    ):

        return f"""
You are an executive strategy advisor.

Create an executive briefing.

Company:
{company}

Risks:
{risks}

Opportunities:
{opportunities}

Recommendations:
{recommendations}

Return ONLY valid JSON.

{{
  "summary":
  "executive summary"
}}
"""
