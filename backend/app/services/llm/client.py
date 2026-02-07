"""LLM client supporting OpenAI-compatible local servers (Ollama, vLLM, LocalAI)."""
from typing import AsyncGenerator

import httpx
from pydantic import BaseModel

from app.core.config import settings


class LLMResponse(BaseModel):
    """Response from LLM."""
    content: str
    finish_reason: str | None = None


class LLMClient:
    """Unified LLM client for local and cloud providers."""

    def __init__(self):
        self.base_url = settings.OLLAMA_BASE_URL or "http://localhost:11434"
        self.model = settings.LLM_MODEL or "mistral"

    async def generate(self, prompt: str, stream: bool = False) -> LLMResponse | AsyncGenerator[str, None]:
        """Generate a response from the LLM.
        
        Args:
            prompt: The prompt to send to the LLM
            stream: Whether to stream the response
            
        Returns:
            LLMResponse or async generator for streaming
        """
        async with httpx.AsyncClient(timeout=120.0) as client:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": stream,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                }
            }
            
            if stream:
                return self._stream_response(client, payload)
            else:
                response = await client.post(f"{self.base_url}/api/generate", json=payload)
                response.raise_for_status()
                data = response.json()
                return LLMResponse(content=data.get("response", ""))

    async def chat(self, messages: list[dict], stream: bool = False) -> LLMResponse | AsyncGenerator[str, None]:
        """Generate a chat response.
        
        Args:
            messages: List of chat messages [{"role": "user", "content": "..."}]
            stream: Whether to stream the response
            
        Returns:
            LLMResponse or async generator for streaming
        """
        async with httpx.AsyncClient(timeout=120.0) as client:
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": stream,
            }
            
            if stream:
                return self._stream_chat_response(client, payload)
            else:
                response = await client.post(f"{self.base_url}/v1/chat/completions", json=payload)
                response.raise_for_status()
                data = response.json()
                content = data["choices"][0]["message"]["content"]
                return LLMResponse(content=content)

    async def _stream_response(self, client: httpx.AsyncClient, payload: dict) -> AsyncGenerator[str, None]:
        """Stream response from local Ollama/vLLM."""
        async with client.stream("POST", f"{self.base_url}/api/generate", json=payload) as response:
            async for line in response.aiter_lines():
                if line:
                    import json
                    try:
                        data = json.loads(line)
                        if "response" in data:
                            yield data["response"]
                    except json.JSONDecodeError:
                        continue

    async def _stream_chat_response(self, client: httpx.AsyncClient, payload: dict) -> AsyncGenerator[str, None]:
        """Stream response from OpenAI-compatible API."""
        async with client.stream("POST", f"{self.base_url}/v1/chat/completions", json=payload) as response:
            async for line in response.aiter_lines():
                if line.startswith("data: "):
                    import json
                    data = json.loads(line[6:])
                    if "choices" in data:
                        delta = data["choices"][0].get("delta", {})
                        content = delta.get("content", "")
                        if content:
                            yield content


# Singleton instance
llm_client = LLMClient()
