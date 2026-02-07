from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """Schema for user registration."""

    email: EmailStr
    username: str
    password: str
    display_name: str | None = None


class UserResponse(BaseModel):
    """Schema for user API responses."""

    id: str
    email: str
    username: str
    display_name: str | None = None
    is_active: bool

    model_config = {"from_attributes": True}


class TokenResponse(BaseModel):
    """Schema for authentication token response."""

    access_token: str
    token_type: str = "bearer"
