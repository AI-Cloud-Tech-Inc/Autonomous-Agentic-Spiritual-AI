"""
Pydantic schemas for API request/response validation
"""
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class ProjectStatus(str, Enum):
    """Project status enum"""
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class VideoFormat(str, Enum):
    """Video format enum"""
    LANDSCAPE = "landscape"
    PORTRAIT = "portrait"
    SQUARE = "square"


class ProjectBase(BaseModel):
    """Base project schema"""
    title: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    video_format: VideoFormat = VideoFormat.LANDSCAPE
    duration: Optional[str] = None


class ProjectCreate(ProjectBase):
    """Schema for creating a project"""
    pass


class ProjectUpdate(BaseModel):
    """Schema for updating a project"""
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    status: Optional[ProjectStatus] = None
    video_format: Optional[VideoFormat] = None
    duration: Optional[str] = None
    output_url: Optional[str] = None


class ProjectResponse(ProjectBase):
    """Schema for project response"""
    id: int
    status: ProjectStatus
    output_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class ScriptBase(BaseModel):
    """Base script schema"""
    content: str = Field(..., min_length=1)
    language: str = Field(default="en", max_length=50)


class ScriptCreate(ScriptBase):
    """Schema for creating a script"""
    project_id: int


class ScriptResponse(ScriptBase):
    """Schema for script response"""
    id: int
    project_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class SceneBase(BaseModel):
    """Base scene schema"""
    sequence_number: int = Field(..., ge=1)
    description: str = Field(..., min_length=1)
    duration: float = Field(default=5.0, gt=0)


class SceneCreate(SceneBase):
    """Schema for creating a scene"""
    project_id: int


class SceneUpdate(BaseModel):
    """Schema for updating a scene"""
    description: Optional[str] = Field(None, min_length=1)
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    duration: Optional[float] = Field(None, gt=0)


class SceneResponse(SceneBase):
    """Schema for scene response"""
    id: int
    project_id: int
    image_url: Optional[str] = None
    video_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
