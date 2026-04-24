"""
Scripts Endpoint - AI-powered scriptwriting
"""
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.ai_services import openai_service
import asyncio

router = APIRouter()


class ScriptGenerateRequest(BaseModel):
    """Script generation request"""
    project_id: str
    prompt: str
    duration: int = 60  # seconds
    tone: str = "professional"  # professional, casual, dramatic, etc.


class ScriptResponse(BaseModel):
    """Script response schema"""
    id: str
    project_id: str
    content: str
    duration: int
    status: str


# In-memory storage (replace with database later)
scripts_db = {}


@router.post("/generate", response_model=ScriptResponse)
async def generate_script(request: ScriptGenerateRequest, background_tasks: BackgroundTasks):
    """Generate a video script using AI"""
    try:
        # Generate script using OpenAI
        script_content = await openai_service.generate_script(
            prompt=request.prompt,
            duration=request.duration,
            tone=request.tone
        )
        
        script_id = f"script_{hash(request.prompt)}"
        
        script_data = {
            "id": script_id,
            "project_id": request.project_id,
            "content": script_content,
            "duration": request.duration,
            "status": "completed"
        }
        
        scripts_db[script_id] = script_data
        
        return script_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{script_id}", response_model=ScriptResponse)
async def get_script(script_id: str):
    """Get script by ID"""
    if script_id in scripts_db:
        return scripts_db[script_id]
    
    raise HTTPException(status_code=404, detail="Script not found")
