from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register_user() -> dict:
    """Register a new user."""
    # TODO: Implement user registration
    return {"message": "User registration — not yet implemented"}


@router.post("/login")
async def login_user() -> dict:
    """Authenticate a user and return a token."""
    # TODO: Implement user login
    return {"message": "User login — not yet implemented"}


@router.get("/me")
async def get_current_user() -> dict:
    """Return the current authenticated user's profile."""
    # TODO: Implement with auth dependency
    return {"message": "User profile — not yet implemented"}
