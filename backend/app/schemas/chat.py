from pydantic import BaseModel


class ChatRequest(BaseModel):
    """Incoming chat message from a user."""

    session_id: str
    message: str
    context: dict | None = None


class ChatResponse(BaseModel):
    """Agent response to a chat message."""

    session_id: str
    message: str
    emotion_detected: str | None = None
    suggestions: list[str] = []
