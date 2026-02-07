from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.agent.spiritual_agent import SpiritualAgent

router = APIRouter()
agent = SpiritualAgent()


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


@router.post("/", response_model=ChatResponse)
async def send_message(request: ChatRequest) -> ChatResponse:
    """Handle an incoming chat message and return the agent's response."""
    try:
        response = await agent.respond(request.message, request.context)
        return ChatResponse(
            session_id=request.session_id,
            message=response["message"],
            emotion_detected=response.get("emotion_detected"),
            suggestions=response.get("suggestions", []),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
