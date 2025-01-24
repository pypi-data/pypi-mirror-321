import os
from pathlib import Path
import yaml
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    def __init__(self):
        self.config_dir = Path(os.getenv("XDG_CONFIG_HOME", Path.home() / ".config")) / "howdoi"
        self.config_file = self.config_dir / "config.yaml"
        self.load_config()

    def load_config(self):
        # Default configuration
        self.defaults = {
            "provider": "anthropic",  # or "openai"
            "model": "claude-3-5-sonnet-20241022",  # or "gpt-4" for OpenAI
            "max_tokens": 1000,
            "temperature": 0.7,
        }

        # Create config directory if it doesn't exist
        self.config_dir.mkdir(parents=True, exist_ok=True)

        # Load configuration from file if it exists
        if self.config_file.exists():
            with open(self.config_file, "r") as f:
                file_config = yaml.safe_load(f)
                if file_config:
                    self.defaults.update(file_config)

        # Override with environment variables if they exist
        env_mapping = {
            "HOW_PROVIDER": "provider",
            "HOW_MODEL": "model",
            "HOW_MAX_TOKENS": "max_tokens",
            "HOW_TEMPERATURE": "temperature",
        }

        for env_var, config_key in env_mapping.items():
            if os.getenv(env_var):
                self.defaults[config_key] = os.getenv(env_var)

    def get(self, key):
        return self.defaults.get(key)
