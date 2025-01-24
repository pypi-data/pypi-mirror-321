from .base import BaseProvider
import anthropic
import os

class AnthropicProvider(BaseProvider):
    def __init__(self, config):
        super().__init__(config)
        self.client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))

    def get_command(self, query, shell):
        prompt = (
            f"Given this user request: '{query}', respond with ONLY a {shell} shell command "
            f"that would achieve their goal. The command should work in {shell} specifically. "
            "Do not include any explanation, backticks, quotes, or additional text. "
            "Format the response as a plain command that could be directly copied into the terminal."
        )

        response = self.client.messages.create(
            model=self.config.get("model"),
            max_tokens=self.config.get("max_tokens"),
            temperature=self.config.get("temperature"),
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        return response.content[0].text.strip()
