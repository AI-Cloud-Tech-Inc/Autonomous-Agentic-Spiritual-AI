"""
Base Agent Class for AI Film Studio
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import logging
from anthropic import AsyncAnthropic

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-opus-4-6"


class BaseAgent(ABC):
    """Abstract base class for all AI agents"""

    def __init__(self, name: str, model: str = DEFAULT_MODEL, anthropic_api_key: str = ""):
        self.name = name
        self.model = model
        self.memory: list[Dict[str, Any]] = []
        self._client: Optional[AsyncAnthropic] = None
        if anthropic_api_key:
            self._client = AsyncAnthropic(api_key=anthropic_api_key)
        logger.info(f"Initialized {self.name} agent with model {self.model}")

    @classmethod
    def from_settings(cls, **kwargs):
        from app.core.config import settings
        return cls(anthropic_api_key=settings.ANTHROPIC_API_KEY, **kwargs)

    async def _ask_claude(self, prompt: str, system: str, max_tokens: int = 4096) -> str:
        """Call Claude and return the text response."""
        if not self._client:
            raise RuntimeError(f"{self.name}: Anthropic client not initialised — set ANTHROPIC_API_KEY")
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            system=system,
            messages=[{"role": "user", "content": prompt}],
        )
        for block in response.content:
            if block.type == "text":
                return block.text
        return ""

    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        pass

    def add_to_memory(self, data: Dict[str, Any]):
        self.memory.append(data)

    def clear_memory(self):
        self.memory = []

    def get_context(self, max_items: int = 10) -> list[Dict[str, Any]]:
        return self.memory[-max_items:]
