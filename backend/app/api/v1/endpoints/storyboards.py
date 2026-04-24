"""
Storyboards Endpoint - Visual planning
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()


class StoryboardFrame(BaseModel):
    """Individual storyboard frame"""
    scene_number: int
    description: str
    image_url: str = ""


class StoryboardRequest(BaseModel):
    """Storyboard generation request"""
    script_id: str
    num_frames: int = 6


class StoryboardResponse(BaseModel):
    """Storyboard response"""
    id: str
    script_id: str
    frames: List[StoryboardFrame]
    status: str


@router.post("/generate", response_model=StoryboardResponse)
async def generate_storyboard(request: StoryboardRequest):
    """Generate storyboard from script"""
    return {
        "id": "storyboard_123",
        "script_id": request.script_id,
        "frames": [],
        "status": "generating"
    }


@router.get("/{storyboard_id}", response_model=StoryboardResponse)
async def get_storyboard(storyboard_id: str):
    """Get storyboard by ID"""
    return {
        "id": storyboard_id,
        "script_id": "script_123",
        "frames": [],
        "status": "completed"
    }
