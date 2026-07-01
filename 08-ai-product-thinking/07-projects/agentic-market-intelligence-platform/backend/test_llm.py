from services.llm_service import LLMService

llm = LLMService()

prompt = """
Return ONLY JSON.

{
  "risks": [
    "...",
    "...",
    "..."
  ]
}

Analyze Tesla.
"""

print(
    llm.generate_json(prompt)
)
