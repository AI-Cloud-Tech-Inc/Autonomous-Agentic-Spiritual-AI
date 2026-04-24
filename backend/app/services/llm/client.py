"""Unified LLM client that abstracts over multiple providers."""

from app.core.config import settings


class LLMClient:
    """A provider-agnostic LLM client.

    Supports Anthropic (Claude) and OpenAI as backend providers.
    The provider is selected via configuration.
    """

    def __init__(self, provider: str | None = None, model: str | None = None) -> None:
        self.provider = provider or settings.DEFAULT_LLM_PROVIDER
        self.model = model or settings.DEFAULT_MODEL

    async def generate(self, messages: list[dict], system_prompt: str | None = None) -> str:
        """Send messages to the LLM and return the response text.

        Args:
            messages: List of {"role": ..., "content": ...} message dicts.
            system_prompt: Optional system-level instruction.

        Returns:
            The model's response as a string.
        """
        # TODO: Implement actual API calls to Anthropic/OpenAI
        raise NotImplementedError("LLM client not yet connected to a provider")
