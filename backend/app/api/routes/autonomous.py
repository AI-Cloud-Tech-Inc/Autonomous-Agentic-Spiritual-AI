"""
Autonomous Film Creation API Routes
"""
import json
import uuid
import logging
from typing import Optional, Dict, Any, List

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy import func
from sqlalchemy.orm import Session, selectinload

from app.agents.orchestrator import AgentOrchestrator
from app.database import get_db
from app.models.project import Project, Scene, Script, ProjectStatus

logger = logging.getLogger(__name__)

router = APIRouter()

# Cache of orchestrators keyed by model name — avoids re-creating on every request
# while still honouring per-request model selection.
_orchestrators: Dict[str, AgentOrchestrator] = {}


def _get_orchestrator(model: str) -> AgentOrchestrator:
    if model not in _orchestrators:
        from app.core.config import settings
        _orchestrators[model] = AgentOrchestrator(
            model=model,
            anthropic_api_key=settings.ANTHROPIC_API_KEY,
        )
    return _orchestrators[model]


# ---------------------------------------------------------------------------
# Request / Response schemas
# ---------------------------------------------------------------------------

class FilmRequest(BaseModel):
    prompt: str = Field(..., min_length=10, description="Film concept / idea")
    style: str = Field(default="cinematic", description="Visual style")
    duration: int = Field(default=30, ge=5, le=300, description="Target duration in seconds")
    model: str = Field(default="claude-opus-4-6", description="Claude model to use")


class FilmResponse(BaseModel):
    status: str
    project_id: str
    message: str
    persisted: bool = True
    data: Optional[Dict[str, Any]] = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _persist_project(db: Session, request: FilmRequest, result: Dict[str, Any]) -> Project:
    """Save the completed film pipeline result to the database and return the Project."""
    director_out = result.get("director", {})
    script_out = result.get("script", {})
    scenes_raw: List[Dict] = director_out.get("scenes", [])
    script_scenes: List[Dict] = script_out.get("script_scenes", [])

    project = Project(
        id=str(uuid.uuid4()),
        title=request.prompt[:120],
        prompt=request.prompt,
        style=request.style,
        duration=request.duration,
        model=request.model,
        status=ProjectStatus.completed,
        director_vision=director_out.get("vision", ""),
    )
    db.add(project)
    db.flush()  # populate project.id before adding children

    # Persist each scene
    script_lookup = {s.get("scene_number"): s for s in script_scenes}
    for scene_data in scenes_raw:
        sn = scene_data.get("scene_number", 0)
        script_scene = script_lookup.get(sn, {})
        scene = Scene(
            id=str(uuid.uuid4()),
            project_id=project.id,
            scene_number=sn,
            description=scene_data.get("description", ""),
            shot_type=scene_data.get("shot_type", "medium"),
            mood=scene_data.get("mood", "neutral"),
            duration=scene_data.get("duration", 10),
            visual_prompt=scene_data.get("visual_prompt", ""),
            narration=script_scene.get("narration", ""),
            dialogue=script_scene.get("dialogue", []),
            audio_cues=script_scene.get("audio_cues", []),
        )
        db.add(scene)

    # Persist combined script as a single Script record
    if script_scenes:
        script = Script(
            id=str(uuid.uuid4()),
            project_id=project.id,
            content=json.dumps(script_scenes),
            scene_count=len(script_scenes),
        )
        db.add(script)

    db.commit()
    db.refresh(project)
    return project


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/create-film", response_model=FilmResponse)
async def create_autonomous_film(request: FilmRequest, db: Session = Depends(get_db)):
    """
    Orchestrate the full autonomous film pipeline:
    Director -> Screenwriter -> Cinematographer -> Sound Designer -> Editor
    """
    logger.info(f"Film creation started: {request.prompt[:60]}...")

    orchestrator = _get_orchestrator(request.model)

    result = await orchestrator.create_film(
        user_prompt=request.prompt,
        style=request.style,
        duration=request.duration,
    )

    if result.get("status") == "error":
        raise HTTPException(status_code=500, detail=result.get("error", "Unknown error"))

    # Persist to DB; surface a clear flag rather than silently swallowing failures.
    persisted = True
    try:
        project = _persist_project(db, request, result)
        project_id = project.id
    except Exception as exc:
        logger.error(f"DB persistence failed: {exc}")
        persisted = False
        project_id = str(uuid.uuid4())

    director_out = result.get("director", {})
    scenes = director_out.get("scenes", [])

    return FilmResponse(
        status="success",
        project_id=project_id,
        persisted=persisted,
        message=f"Film pipeline complete — {len(scenes)} scenes created"
        + ("" if persisted else " (warning: DB persistence failed)"),
        data={
            "project_id": project_id,
            "prompt": request.prompt,
            "style": request.style,
            "duration": request.duration,
            "scene_count": len(scenes),
            "total_duration": sum(s.get("duration", 0) for s in scenes),
            "director": director_out,
            "script": result.get("script", {}),
            "cinematography": result.get("cinematography", {}),
            "sound": result.get("sound", {}),
            "media_assets": result.get("media_assets", {}),
            "final_timeline": result.get("final_timeline", {}),
            "workflow_steps": result.get("workflow_steps", []),
        },
    )


@router.get("/projects", response_model=List[Dict[str, Any]])
def list_projects(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    """List all film projects, newest first."""
    # Use a COUNT subquery to avoid the N+1 per-project lazy-load.
    scene_count_sq = (
        db.query(func.count(Scene.id))
        .filter(Scene.project_id == Project.id)
        .correlate(Project)
        .scalar_subquery()
    )
    rows = (
        db.query(Project, scene_count_sq.label("scene_count"))
        .order_by(Project.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )
    return [
        {
            "id": p.id,
            "title": p.title,
            "style": p.style,
            "duration": p.duration,
            "status": p.status,
            "scene_count": count,
            "created_at": p.created_at.isoformat(),
        }
        for p, count in rows
    ]


@router.get("/projects/{project_id}", response_model=Dict[str, Any])
def get_project(project_id: str, db: Session = Depends(get_db)):
    """Get a single project with all its scenes and script."""
    project = (
        db.query(Project)
        .options(selectinload(Project.scenes), selectinload(Project.scripts))
        .filter(Project.id == project_id)
        .first()
    )
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    script_content: List = []
    if project.scripts:
        try:
            script_content = json.loads(project.scripts[0].content)
        except Exception:
            pass

    return {
        "id": project.id,
        "title": project.title,
        "prompt": project.prompt,
        "style": project.style,
        "duration": project.duration,
        "model": project.model,
        "status": project.status,
        "director_vision": project.director_vision,
        "created_at": project.created_at.isoformat(),
        "scenes": [
            {
                "scene_number": s.scene_number,
                "description": s.description,
                "shot_type": s.shot_type,
                "mood": s.mood,
                "duration": s.duration,
                "visual_prompt": s.visual_prompt,
                "narration": s.narration,
                "dialogue": s.dialogue,
                "audio_cues": s.audio_cues,
            }
            for s in sorted(project.scenes, key=lambda x: x.scene_number)
        ],
        "script": script_content,
    }


@router.get("/agent-status")
def get_agent_status():
    """Return memory stats for all running orchestrators."""
    return {
        "status": "active",
        "orchestrators": {
            model: orch.get_agent_status()
            for model, orch in _orchestrators.items()
        },
    }


@router.post("/clear-memory")
def clear_agent_memory():
    """Clear in-memory context from all agents."""
    for orch in _orchestrators.values():
        orch.clear_all_memory()
    return {"status": "success", "message": "All agent memories cleared"}
