"""
Projects Endpoint - Manage video projects
"""
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()


class ProjectCreate(BaseModel):
    """Project creation schema"""
    title: str
    description: str
    format: str = "landscape"  # landscape, portrait, square


class ProjectResponse(BaseModel):
    """Project response schema"""
    id: str
    title: str
    description: str
    format: str
    status: str
    created_at: str


@router.post("/", response_model=ProjectResponse)
async def create_project(project: ProjectCreate):
    """Create a new video project"""
    return {
        "id": "proj_123",
        "title": project.title,
        "description": project.description,
        "format": project.format,
        "status": "created",
        "created_at": "2026-02-01T00:00:00Z"
    }


@router.get("/", response_model=List[ProjectResponse])
async def list_projects():
    """List all projects"""
    return []


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(project_id: str):
    """Get project details"""
    raise HTTPException(status_code=404, detail="Project not found")
