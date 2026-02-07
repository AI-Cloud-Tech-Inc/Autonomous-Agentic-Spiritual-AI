from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def send_message() -> dict:
    """Handle an incoming chat message and return the agent's response."""
    # TODO: Integrate with the spiritual agent service
    return {"message": "Chat endpoint — not yet implemented"}
