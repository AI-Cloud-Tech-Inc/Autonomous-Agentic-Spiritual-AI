from datetime import datetime

from pydantic import BaseModel


class SessionCreate(BaseModel):
    """Schema for creating a new guidance session."""

    title: str | None = None
    intention: str | None = None


class SessionResponse(BaseModel):
    """Schema for session API responses."""

    id: str
    title: str | None = None
    intention: str | None = None
    status: str
    created_at: datetime

    model_config = {"from_attributes": True}
