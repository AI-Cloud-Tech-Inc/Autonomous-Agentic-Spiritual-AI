"""
API Router - Version 1

Combines Film Studio and Spiritual AI routes under /api/v1/.
"""
from fastapi import APIRouter
from app.api.v1.endpoints import (
    scripts,
    storyboards,
    scenes,
    voiceovers,
    videos,
    projects
)
from app.api.routes import autonomous
from app.api.routes import chat, users, sessions

api_router = APIRouter()

# --- Film Studio ---
api_router.include_router(autonomous.router, prefix="/autonomous", tags=["Autonomous"])
api_router.include_router(projects.router, prefix="/projects", tags=["Projects"])
api_router.include_router(scripts.router, prefix="/scripts", tags=["Scripts"])
api_router.include_router(storyboards.router, prefix="/storyboards", tags=["Storyboards"])
api_router.include_router(scenes.router, prefix="/scenes", tags=["Scenes"])
api_router.include_router(voiceovers.router, prefix="/voiceovers", tags=["Voiceovers"])
api_router.include_router(videos.router, prefix="/videos", tags=["Videos"])

# --- Spiritual AI ---
api_router.include_router(chat.router, prefix="/chat", tags=["Spiritual Chat"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(sessions.router, prefix="/sessions", tags=["Sessions"])
