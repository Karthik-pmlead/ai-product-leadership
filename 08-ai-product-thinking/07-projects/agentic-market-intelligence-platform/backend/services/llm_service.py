import requests
import json
from typing import Optional


class LLMService:

    def __init__(
        self,
        model: str = "qwen3:8b",
        base_url: str = "http://localhost:11434"
    ):
        self.model = model
        self.base_url = base_url

    def generate(
        self,
        prompt: str,
        temperature: float = 0.3
    ) -> str:

        try:

            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": temperature
                    }
                },
                timeout=120
            )

            response.raise_for_status()

            result = response.json()

            return result.get(
                "response",
                ""
            ).strip()

        except Exception as e:

            print(
                f"LLM Error: {str(e)}"
            )

            return (
                "Unable to generate response "
                "from local model."
            )

    def generate_json(
        self,
        prompt: str
    ) -> Optional[dict]:

        try:

            response = self.generate(prompt)

            start = response.find("{")
            end = response.rfind("}") + 1

            if start == -1 or end == 0:
                return None

            json_str = response[start:end]

            return json.loads(
                json_str
            )

        except Exception as e:

            print(
                f"JSON Parse Error: {str(e)}"
            )

            return None

    def health_check(self) -> bool:

        try:

            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=10
            )

            return response.status_code == 200

        except Exception:

            return False
