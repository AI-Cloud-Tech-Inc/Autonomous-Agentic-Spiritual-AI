# CLAUDE.md — Developer Guide for Autonomous-Agentic-Spiritual-AI

## Project Overview

A unified platform by **AI Cloud Tech Inc** combining two autonomous agentic AI systems:

- **Spiritual AI Agent** — supports inner growth, reflection, and well-being through ethical, non-dogmatic guidance (CLI + API)
- **AI Film Studio** — autonomous film production via collaborative AI agents (Director, Screenwriter, Cinematographer, Sound Designer, Editor)

**Tech Stack:** Python 3.11 / FastAPI (backend) + Next.js 14 / TypeScript / Tailwind (frontend) + PostgreSQL + Redis + Celery

**License:** MIT

---

## Repository Structure

```
Autonomous-Agentic-Spiritual-AI/
├── backend/                         # FastAPI backend (unified)
│   ├── main.py                      # Single entry point
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── .env.example
│   ├── alembic/                     # DB migrations (not yet generated)
│   ├── app/
│   │   ├── core/
│   │   │   ├── config.py            # Unified pydantic settings
│   │   │   └── security.py          # JWT + bcrypt auth
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── router.py        # Main router (Film + Spiritual)
│   │   │   │   └── endpoints/       # Film Studio CRUD endpoints
│   │   │   └── routes/
│   │   │       ├── autonomous.py    # Film pipeline orchestration
│   │   │       ├── chat.py          # Spiritual AI chat (stub)
│   │   │       ├── users.py         # User auth (stub)
│   │   │       └── sessions.py      # Session mgmt (stub)
│   │   ├── agents/                  # Film Studio AI agents
│   │   │   ├── orchestrator.py      # Coordinates all agents
│   │   │   ├── director_agent.py
│   │   │   ├── screenwriter_agent.py
│   │   │   ├── cinematographer_agent.py
│   │   │   ├── sound_designer_agent.py
│   │   │   └── editor_agent.py
│   │   ├── models/                  # SQLAlchemy ORM
│   │   │   ├── project.py, scene.py, script.py  # Film Studio
│   │   │   └── user.py, session.py, message.py  # Spiritual AI
│   │   ├── schemas/                 # Pydantic schemas
│   │   ├── services/
│   │   │   ├── agent/spiritual_agent.py  # Spiritual agent (stub)
│   │   │   ├── emotion/detector.py       # Emotion detection (stub)
│   │   │   ├── spiritual/guidance.py     # Guidance service (stub)
│   │   │   ├── llm/client.py             # Unified LLM client (stub)
│   │   │   ├── video_generator.py        # Film Studio service
│   │   │   └── audio_generator.py        # Film Studio service
│   │   ├── db/session.py            # Async SQLAlchemy factory
│   │   ├── database.py              # Sync SQLAlchemy (Film Studio)
│   │   ├── middleware/              # Error handling + logging
│   │   └── tasks/                   # Celery async tasks
│   └── tests/
│
├── frontend/                        # Next.js 14 + TypeScript + Tailwind
│   ├── app/                         # Next.js pages (Film Studio)
│   │   ├── layout.tsx, page.tsx
│   │   └── create/page.tsx
│   ├── src/
│   │   ├── components/              # Spiritual AI UI components
│   │   │   ├── chat/                # ChatWindow, MessageList, etc.
│   │   │   ├── meditation/          # MeditationTimer
│   │   │   └── reflection/          # ReflectionPrompt
│   │   ├── hooks/, services/, store/ # React hooks, API, Zustand state
│   │   ├── types/                   # TypeScript interfaces
│   │   ├── BhaktiTab.jsx            # Bhakti/devotional content
│   │   └── spiritual_content.js     # Spiritual content data
│   ├── package.json, tsconfig.json
│   └── next.config.js, tailwind.config.js
│
├── src/                             # Spiritual AI agent core (standalone CLI)
│   ├── main.py                      # Interactive CLI entry point
│   ├── core/
│   │   ├── agent.py                 # SpiritualAgent class (IMPLEMENTED)
│   │   ├── llm_client.py            # Ollama/OpenAI client
│   │   └── constants.py             # Emotions, crisis keywords
│   ├── memory/memory_manager.py     # Short/long/episodic memory
│   ├── dialogue/conversation_handler.py
│   └── reasoning/context_analyzer.py
│
├── config/config.yaml               # Spiritual AI YAML config
├── data/prompts/                    # Meditation prompt library
├── docker-compose.yml               # Full stack orchestration
├── .github/workflows/               # CI/CD pipelines
├── .env.example                     # Environment template
├── docs/                            # Architecture + integration docs
└── [AGENT_ARCHITECTURE, QUICKSTART, CONTRIBUTING, ...].md
```

---

## Quick Start

### Backend
```bash
cd backend
cp .env.example .env                 # add your API keys
pip install -r requirements.txt
uvicorn main:app --reload            # http://localhost:8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev                          # http://localhost:3000
```

### Spiritual AI CLI (standalone)
```bash
pip install -r requirements.txt
python src/main.py                   # interactive chat
```

### Docker Compose (full stack)
```bash
cp .env.example .env
docker compose up --build            # backend + frontend + postgres + redis
```

---

## API Routes

All routes live under `/api/v1/`:

### Film Studio
| Method | Endpoint | Status |
|--------|----------|--------|
| POST | `/api/v1/autonomous/create-film` | Implemented |
| GET | `/api/v1/autonomous/projects` | Implemented |
| GET | `/api/v1/autonomous/projects/{id}` | Implemented |
| GET | `/api/v1/autonomous/agent-status` | Implemented |
| * | `/api/v1/scripts/*` | Stub |
| * | `/api/v1/storyboards/*` | Stub |
| * | `/api/v1/scenes/*` | Stub |
| * | `/api/v1/voiceovers/*` | Stub |
| * | `/api/v1/videos/*` | Stub |
| * | `/api/v1/projects/*` | Stub |

### Spiritual AI
| Method | Endpoint | Status |
|--------|----------|--------|
| POST | `/api/v1/chat/` | Stub |
| POST | `/api/v1/users/register` | Stub |
| POST | `/api/v1/users/login` | Stub |
| GET | `/api/v1/users/me` | Stub |
| POST | `/api/v1/sessions/` | Stub |
| GET | `/api/v1/sessions/{id}` | Stub |

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
| Film Studio agents | **Done** | Director, Screenwriter, Cinematographer, Sound, Editor |
| Film pipeline API | **Done** | `/autonomous/create-film` end-to-end |
| Spiritual AI CLI | **Done** | `python src/main.py` — fully functional |
| Spiritual AI API | **Stub** | Chat, users, sessions need implementation |
| Spiritual AI services | **Stub** | Agent, emotion, guidance, LLM client |
| Database models | **Done** | Film + Spiritual models defined |
| Database migrations | **Missing** | Alembic configured but no migrations |
| Frontend (Film Studio) | **Partial** | Next.js pages scaffolded |
| Frontend (Spiritual AI) | **Partial** | Chat components exist, need wiring |
| Tests | **Minimal** | Only health check tests |
| Docker setup | **Done** | Full stack compose file |
| CI/CD | **Done** | GitHub Actions pipeline |

---

## Conventions

1. **Non-dogmatic, inclusive** — spiritual content must respect all traditions
2. **Preserve autonomy** — guide and suggest, never coerce
3. **Backend:** Python, FastAPI, SQLAlchemy, Pydantic
4. **Frontend:** Next.js 14, TypeScript, Tailwind CSS
5. **Config:** use `.env` files, never commit secrets
6. **Routes:** add new endpoints under `backend/app/api/v1/` or `backend/app/api/routes/`
7. **Models:** add to `backend/app/models/`, then generate alembic migration
8. **Commit style:** `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`
