"""LLM client for connecting to Ollama or OpenAI."""
import os
import json
from typing import Optional, Dict, Any, List
from abc import ABC, abstractmethod


class LLMClient(ABC):
    """Abstract base class for LLM clients."""
    
    @abstractmethod
    def complete(self, messages: List[Dict[str, str]], context: Dict[str, Any]) -> str:
        """Generate a completion."""
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        """Check if the LLM service is available."""
        pass


class OllamaClient(LLMClient):
    """Client for Ollama local LLM."""
    
    def __init__(self, model: str = "llama3.2", base_url: str = "http://localhost:11434"):
        """Initialize Ollama client."""
        self.model = model
        self.base_url = base_url
        self.api_url = f"{base_url}/api/generate"
    
    def is_available(self) -> bool:
        """Check if Ollama is running."""
        try:
            import requests
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except Exception:
            return False
    
    def complete(self, messages: List[Dict[str, str]], context: Dict[str, Any]) -> str:
        """Generate completion using Ollama."""
        try:
            import requests
            
            # Build system prompt from context
            system_prompt = self._build_system_prompt(context)
            
            # Prepare messages for Ollama
            ollama_messages = [{"role": "system", "content": system_prompt}]
            ollama_messages.extend(messages)
            
            payload = {
                "model": self.model,
                "messages": ollama_messages,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "top_p": 0.9,
                }
            }
            
            response = requests.post(self.api_url, json=payload, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result.get("response", "")
            
        except Exception as e:
            print(f"Ollama error: {e}")
            raise
    
    def _build_system_prompt(self, context: Dict[str, Any]) -> str:
        """Build system prompt with spiritual context."""
        base_prompt = """You are a compassionate spiritual guide and mindfulness companion. Your purpose is to:

1. Listen deeply and reflect thoughtfully
2. Offer gentle guidance without being prescriptive
3. Draw from various spiritual traditions and philosophical perspectives
4. Help users explore their inner world with curiosity and kindness
5. Encourage mindfulness, self-reflection, and conscious living
6. Be inclusive and respectful of diverse beliefs and backgrounds

You are NOT:
- A religious authority
- A medical or psychological professional
- Someone who gives absolute answers

Your tone: Warm, contemplative, wise but humble, peaceful.

Remember: You are here to guide and support, not to tell people what to believe or do. Help them find their own answers."""
        
        # Add context about detected emotions/intent
        emotion = context.get("emotion")
        intent = context.get("intent")
        
        if emotion:
            base_prompt += f"\n\nThe user seems to be feeling: {emotion}"
        if intent:
            base_prompt += f"\nThe user's intent appears to be: {intent}"
            
        return base_prompt


class OpenAIClient(LLMClient):
    """Client for OpenAI API."""
    
    def __init__(self, model: str = "gpt-3.5-turbo", api_key: Optional[str] = None):
        """Initialize OpenAI client."""
        self.model = model
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.api_url = "https://api.openai.com/v1/chat/completions"
    
    def is_available(self) -> bool:
        """Check if OpenAI is available."""
        return bool(self.api_key)
    
    def complete(self, messages: List[Dict[str, str]], context: Dict[str, Any]) -> str:
        """Generate completion using OpenAI."""
        try:
            import requests
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.7
            }
            
            response = requests.post(self.api_url, json=payload, headers=headers, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except Exception as e:
            print(f"OpenAI error: {e}")
            raise
    
    def _build_system_prompt(self, context: Dict[str, Any]) -> str:
        """Build system prompt with spiritual context."""
        return """You are a compassionate spiritual guide and mindfulness companion."""


class MockClient(LLMClient):
    """Mock client for testing without LLM."""
    
    def is_available(self) -> bool:
        """Always available."""
        return True
    
    def complete(self, messages: List[Dict[str, str]], context: Dict[str, Any]) -> str:
        """Return a mock response."""
        user_msg = ""
        for msg in messages:
            if msg.get("role") == "user":
                user_msg = msg.get("content", "")
                break
        
        # Simple keyword-based responses
        msg_lower = user_msg.lower()
        
        if "meditat" in msg_lower:
            return "Take a moment to breathe deeply. Find a comfortable position and close your eyes. With each breath, feel yourself becoming more present and at peace..."
        elif "sad" in msg_lower or "lonely" in msg_lower:
            return "I hear you. It's okay to feel what you're feeling. Remember that you're not alone on this journey. Would you like to talk about what's on your heart?"
        elif "grateful" in msg_lower or "thankful" in msg_lower:
            return "Gratitude is a beautiful practice. Taking time to appreciate what we have cultivates inner wealth. What are you most grateful for today?"
        elif "angry" in msg_lower or "frustrated" in msg_lower:
            return "I see your frustration. It's valid to feel what you feel. Sometimes taking a step back and breathing can help us find clarity."
        elif "wisdom" in msg_lower or "advice" in msg_lower:
            return "The greatest wisdom often comes from within. Trust your inner guidance. What does your heart tell you?"
        else:
            return "I'm here to listen and reflect with you. Take your time to share what's on your mind. I'm here to support you on your spiritual journey."


def get_llm_client(provider: str = "mock") -> LLMClient:
    """Get the appropriate LLM client."""
    providers = {
        "ollama": OllamaClient,
        "openai": OpenAIClient,
        "mock": MockClient,
    }
    
    client_class = providers.get(provider.lower(), MockClient)
    
    if provider.lower() == "ollama":
        model = os.getenv("OLLAMA_MODEL", "llama3.2")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        return OllamaClient(model=model, base_url=base_url)
    elif provider.lower() == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        model = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
        return OpenAIClient(model=model, api_key=api_key)
    else:
        return MockClient()
