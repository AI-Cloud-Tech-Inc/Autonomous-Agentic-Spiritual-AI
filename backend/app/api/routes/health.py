from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check() -> dict:
    """Return service health status."""
    return {"status": "healthy", "service": "spiritual-ai-backend"}
