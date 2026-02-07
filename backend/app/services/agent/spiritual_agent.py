"""Core spiritual AI agent — orchestrates conversation, emotion detection, and guidance."""
from typing import AsyncGenerator

from app.services.llm.client import llm_client


# System prompt for the spiritual agent
SPIRITUAL_SYSTEM_PROMPT = """You are a compassionate spiritual guide and mindfulness companion. Your purpose is to:

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


class SpiritualAgent:
    """Autonomous agent that provides spiritual guidance."""

    def __init__(self) -> None:
        self.llm = llm_client

    async def respond(self, user_message: str, session_context: dict | None = None) -> dict:
        """Generate a contextual spiritual guidance response."""
        # Build the conversation
        messages = [
            {"role": "system", "content": SPIRITUAL_SYSTEM_PROMPT},
        ]
        
        # Add conversation history if available
        if session_context and "messages" in session_context:
            for msg in session_context["messages"][-10:]:  # Last 10 messages
                messages.append({"role": msg.get("role", "user"), "content": msg.get("content", "")})
        else:
            # First message
            messages.append({"role": "user", "content": user_message})

        try:
            response = await self.llm.chat(messages)
            return {
                "message": response.content,
                "emotion_detected": None,  # TODO: Add emotion detection
                "suggestions": [],
            }
        except Exception as e:
            return {
                "message": f"I'm here to listen. {user_message}",
                "emotion_detected": None,
                "suggestions": [],
            }

    async def stream_response(self, user_message: str, session_context: dict | None = None) -> AsyncGenerator[str, None]:
        """Stream a contextual spiritual guidance response."""
        messages = [
            {"role": "system", "content": SPIRITUAL_SYSTEM_PROMPT},
        ]
        
        if session_context and "messages" in session_context:
            for msg in session_context["messages"][-10:]:
                messages.append({"role": msg.get("role", "user"), "content": msg.get("content", "")})
        else:
            messages.append({"role": "user", "content": user_message})

        async for chunk in self.llm.chat(messages, stream=True):
            yield chunk
