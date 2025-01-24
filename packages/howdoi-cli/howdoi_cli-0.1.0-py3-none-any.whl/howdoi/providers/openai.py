import os
from .base import BaseProvider
import openai

class OpenAIProvider(BaseProvider):
    def __init__(self, config):
        super().__init__(config)
        self.client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_command(self, query, shell):
        prompt = (
            f"Given this user request: '{query}', respond with ONLY a {shell} shell command "
            f"that would achieve their goal. The command should work in {shell} specifically. "
            "Do not include any explanation, backticks, quotes, or additional text. "
            "Format the response as a plain command that could be directly copied into the terminal."
        )

        response = self.client.chat.completions.create(
            model=self.config.get("model"),
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=self.config.get("max_tokens"),
            temperature=self.config.get("temperature")
        )

        return response.choices[0].message.content.strip()
