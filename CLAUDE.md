# CLAUDE.md — Developer Guide for AI Film Studio

## Project Overview

**AI Film Studio** by **AI Cloud Tech Inc** — autonomous film production via collaborative AI agents. Six specialized agents (Director, Screenwriter, Cinematographer, Sound Designer, VFX, Editor) work together to create films from a single text prompt.

**Tech Stack:** Python 3.11 / FastAPI (backend) + Next.js 14 / TypeScript / Tailwind (frontend) + PostgreSQL + Redis + Celery

**License:** MIT

---

## Repository Structure

```
Autonomous-Agentic-Spiritual-AI/
├── backend/                         # FastAPI backend
│   ├── main.py                      # Application entry point
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   ├── alembic/                     # DB migrations
│   ├── app/
│   │   ├── core/
│   │   │   └── config.py            # Pydantic settings
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── router.py        # Main API router
│   │   │   │   └── endpoints/       # CRUD endpoints
│   │   │   │       ├── projects.py
│   │   │   │       ├── scripts.py
│   │   │   │       ├── scenes.py
│   │   │   │       ├── storyboards.py
│   │   │   │       ├── voiceovers.py
│   │   │   │       └── videos.py
│   │   │   └── routes/
│   │   │       ├── autonomous.py    # Film pipeline orchestration
│   │   │       └── health.py        # Health check
│   │   ├── agents/                  # AI agents (6 total)
│   │   │   ├── base_agent.py        # Abstract base with Claude API
│   │   │   ├── orchestrator.py      # Coordinates all 6 agents
│   │   │   ├── director_agent.py
│   │   │   ├── screenwriter_agent.py
│   │   │   ├── cinematographer_agent.py
│   │   │   ├── sound_designer_agent.py
│   │   │   ├── vfx_agent.py
│   │   │   └── editor_agent.py
│   │   ├── models/                  # SQLAlchemy ORM
│   │   │   ├── base.py
│   │   │   ├── project.py
│   │   │   ├── scene.py
│   │   │   └── script.py
│   │   ├── schemas/                 # Pydantic request/response schemas
│   │   ├── services/
│   │   │   ├── ai_services.py       # Multi-provider AI integration
│   │   │   ├── ai_generator.py
│   │   │   ├── video_generator.py
│   │   │   ├── video_service.py
│   │   │   ├── audio_generator.py
│   │   │   └── storage_service.py
│   │   ├── database.py              # SQLAlchemy init
│   │   ├── db/session.py            # Async session factory
│   │   ├── middleware/              # Error handling + logging
│   │   └── tasks/                   # Celery async tasks
│   └── tests/
│
├── frontend/                        # Next.js 14 + TypeScript + Tailwind
│   ├── app/
│   │   ├── layout.tsx, page.tsx     # Landing page
│   │   └── create/page.tsx          # Film creation page
│   ├── src/
│   │   ├── services/api.ts          # Axios API client
│   │   └── utils/formatDate.ts
│   ├── package.json, tsconfig.json
│   └── next.config.js, tailwind.config.js
│
├── docker-compose.yml               # Full stack orchestration
├── .github/workflows/               # CI/CD pipelines
├── .env.example                     # Environment template
└── docs/                            # Architecture docs
```

---

## Quick Start

### Backend
```bash
cd backend
cp .env.example .env                 # add your ANTHROPIC_API_KEY
pip install -r requirements.txt
uvicorn main:app --reload            # http://localhost:8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev                          # http://localhost:3000
```

### Docker Compose (full stack)
```bash
cp .env.example .env
docker compose up --build            # backend + frontend + postgres + redis
```

---

## API Routes

All routes live under `/api/v1/`:

| Method | Endpoint | Status |
|--------|----------|--------|
| POST | `/api/v1/autonomous/create-film` | **Implemented** |
| GET | `/api/v1/autonomous/projects` | **Implemented** |
| GET | `/api/v1/autonomous/projects/{id}` | **Implemented** |
| GET | `/api/v1/autonomous/agent-status` | **Implemented** |
| DELETE | `/api/v1/autonomous/clear-memory` | **Implemented** |
| * | `/api/v1/projects/*` | Stub |
| * | `/api/v1/scripts/*` | Partial |
| * | `/api/v1/storyboards/*` | Stub |
| * | `/api/v1/scenes/*` | Stub |
| * | `/api/v1/voiceovers/*` | Partial |
| * | `/api/v1/videos/*` | Stub |

---

## AI Agent Pipeline

The film creation pipeline runs 6 agents in sequence:

1. **Director** — creative vision + scene breakdown
2. **Screenwriter** — script with dialogue, narration, audio cues
3. **Cinematographer** — shot plans, camera, lighting, color palette
4. **Sound Designer** — music, SFX, voiceover guidance
5. **VFX** — color grading, visual effects, quality notes
6. **Editor** — timeline assembly, transitions, final cut

All agents inherit from `BaseAgent`, use the Anthropic Claude API, and return structured JSON with fallbacks.

---

## Development Commands

### Backend
| Command | Description |
|---------|-------------|
| `uvicorn main:app --reload` | Dev server (from `backend/`) |
| `pytest tests/` | Run tests |
| `alembic revision --autogenerate -m "msg"` | Generate migration |
| `alembic upgrade head` | Apply migrations |

### Frontend
| Command | Description |
|---------|-------------|
| `npm run dev` | Next.js dev server |
| `npm run build` | Production build |
| `npm run lint` | ESLint |

---

## Implementation Status

| Component | Status | Notes |
|-----------|--------|-------|
| AI agents (6) | **Done** | Director, Screenwriter, Cinematographer, Sound, VFX, Editor |
| Agent orchestrator | **Done** | Full pipeline with memory management |
| Autonomous API | **Done** | `/autonomous/create-film` end-to-end |
| Database models | **Done** | Project, Scene, Script with relationships |
| V1 CRUD endpoints | **Stub/Partial** | Need real DB integration |
| Celery tasks | **Stub** | Task shells defined, logic TODO |
| Database migrations | **Missing** | Alembic configured, no migrations |
| Frontend | **Partial** | Landing page done, create page scaffolded |
| Tests | **Minimal** | Only health check tests |
| Docker setup | **Done** | Full stack compose |
| CI/CD | **Done** | GitHub Actions pipeline |

---

## Conventions

1. **Backend:** Python, FastAPI, SQLAlchemy, Pydantic
2. **Frontend:** Next.js 14, TypeScript, Tailwind CSS
3. **Config:** use `.env` files, never commit secrets
4. **Routes:** add new endpoints under `backend/app/api/v1/endpoints/` or `backend/app/api/routes/`
5. **Models:** add to `backend/app/models/`, then generate alembic migration
6. **Agents:** inherit from `BaseAgent`, implement async `process()` method
7. **Commit style:** `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
