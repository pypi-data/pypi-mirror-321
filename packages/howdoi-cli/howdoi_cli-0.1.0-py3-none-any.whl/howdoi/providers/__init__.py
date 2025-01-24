# howdoi/providers/__init__.py

from .base import BaseProvider
from .anthropic import AnthropicProvider
from .openai import OpenAIProvider

def get_provider(config):
    providers = {
        "anthropic": AnthropicProvider,
        "openai": OpenAIProvider,
    }

    provider_class = providers.get(config.get("provider"))
    if not provider_class:
        raise ValueError(f"Unknown provider: {config.get('provider')}")

    return provider_class(config)
