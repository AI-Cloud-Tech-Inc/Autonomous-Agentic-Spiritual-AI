# CLAUDE.md — AI Assistant Guide for Autonomous-Agentic-Spiritual-AI

## Project Overview

**Autonomous-Agentic-Spiritual-AI** is an autonomous, agentic AI spiritual agent designed to support inner growth, reflection, and well-being. It adapts to user context, emotions, and values, offering ethical, non-dogmatic guidance for mindfulness, self-awareness, and conscious living while preserving human autonomy.

- **Organization:** AI Cloud Tech Inc
- **License:** MIT (2026)
- **Tech Stack:** Python 3.11 / FastAPI (backend) + React 19 / TypeScript / Vite (frontend) + PostgreSQL

## Repository Structure

```
Autonomous-Agentic-Spiritual-AI/
├── CLAUDE.md                          # This file — AI assistant guide
├── README.md                          # Project overview
├── LICENSE                            # MIT License
├── docker-compose.yml                 # Full-stack Docker orchestration
├── .gitignore
├── .github/
│   └── workflows/
│       └── ci.yml                     # GitHub Actions CI pipeline
├── docs/
│   └── architecture.md                # System architecture diagram
├── scripts/
│   └── dev.sh                         # Dev environment helper
│
├── backend/                           # Python / FastAPI backend
│   ├── pyproject.toml                 # Python deps, ruff, pytest, mypy config
│   ├── Dockerfile
│   ├── .env.example                   # Env var template (copy to .env)
│   ├── app/
│   │   ├── main.py                    # FastAPI app factory
│   │   ├── core/
│   │   │   ├── config.py              # Pydantic settings (env vars)
│   │   │   └── security.py            # Auth helpers (JWT, password hashing)
│   │   ├── api/routes/
│   │   │   ├── health.py              # GET /health
│   │   │   ├── chat.py                # POST /api/v1/chat
│   │   │   ├── users.py               # /api/v1/users (register, login, me)
│   │   │   └── sessions.py            # /api/v1/sessions (CRUD)
│   │   ├── models/                    # SQLAlchemy ORM models
│   │   │   ├── base.py                # Base, UUID mixin, timestamp mixin
│   │   │   ├── user.py
│   │   │   ├── session.py
│   │   │   └── message.py
│   │   ├── schemas/                   # Pydantic request/response schemas
│   │   │   ├── chat.py
│   │   │   ├── user.py
│   │   │   └── session.py
│   │   ├── services/
│   │   │   ├── agent/
│   │   │   │   └── spiritual_agent.py # Core autonomous agent loop
│   │   │   ├── spiritual/
│   │   │   │   └── guidance.py        # Non-dogmatic guidance strategies
│   │   │   ├── emotion/
│   │   │   │   └── detector.py        # Emotion detection from text
│   │   │   └── llm/
│   │   │       └── client.py          # Unified LLM client (Anthropic/OpenAI)
│   │   ├── db/
│   │   │   └── session.py             # Async SQLAlchemy session factory
│   │   └── utils/
│   └── tests/
│       ├── unit/
│       │   └── test_health.py
│       └── integration/
│
└── frontend/                          # React / TypeScript / Vite frontend
    ├── package.json
    ├── tsconfig.json
    ├── vite.config.ts
    ├── index.html
    ├── Dockerfile
    ├── nginx.conf                     # Production reverse proxy config
    ├── public/
    ├── src/
    │   ├── main.tsx                    # App entry point
    │   ├── App.tsx                     # Router setup
    │   ├── index.css                   # Global styles / CSS variables
    │   ├── pages/
    │   │   ├── HomePage.tsx
    │   │   └── ChatPage.tsx
    │   ├── components/
    │   │   ├── chat/
    │   │   │   ├── ChatWindow.tsx      # Main chat container
    │   │   │   ├── MessageList.tsx
    │   │   │   ├── MessageBubble.tsx
    │   │   │   └── MessageInput.tsx
    │   │   ├── common/
    │   │   │   └── Layout.tsx
    │   │   ├── meditation/
    │   │   │   └── MeditationTimer.tsx
    │   │   └── reflection/
    │   │       └── ReflectionPrompt.tsx
    │   ├── hooks/
    │   │   └── useChat.ts
    │   ├── services/
    │   │   ├── api.ts                  # Axios instance with auth interceptor
    │   │   └── chatService.ts          # Chat & session API calls
    │   ├── store/
    │   │   ├── chatStore.ts            # Zustand chat state
    │   │   └── authStore.ts            # Zustand auth state
    │   ├── types/
    │   │   ├── chat.ts
    │   │   └── user.ts
    │   ├── utils/
    │   │   └── formatDate.ts
    │   └── assets/
    └── tests/
```

## Quick Start

### Prerequisites

- Python 3.11+
- Node.js 22+
- PostgreSQL 16+ (or use Docker Compose)

### Backend

```bash
cd backend
cp .env.example .env          # configure your env vars
pip install -e ".[dev]"       # install deps
uvicorn app.main:app --reload # start dev server on :8000
```

### Frontend

```bash
cd frontend
npm install                   # install deps
npm run dev                   # start Vite dev server on :3000
```

### Docker Compose (full stack)

```bash
docker compose up --build     # backend :8000 + frontend :3000 + postgres :5432
```

## Development Commands

### Backend

| Command | Description |
|---------|-------------|
| `uvicorn app.main:app --reload` | Run dev server |
| `pytest --cov=app tests/` | Run tests with coverage |
| `ruff check .` | Lint Python code |
| `ruff format .` | Format Python code |
| `mypy app` | Type-check Python code |

### Frontend

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server |
| `npm run build` | Production build |
| `npm run lint` | Lint with ESLint |
| `npm run format` | Format with Prettier |
| `npm test` | Run tests with Vitest |

## Architecture

See [docs/architecture.md](docs/architecture.md) for the full diagram.

**Key layers:**
1. **Frontend** — React SPA with chat UI, meditation timer, reflection prompts
2. **API** — FastAPI REST endpoints for chat, users, and sessions
3. **Agent Layer** — `SpiritualAgent` orchestrates emotion detection, intent classification, prompt building, and LLM calls
4. **Services** — `GuidanceService` (spiritual content), `EmotionDetector`, `LLMClient`
5. **Database** — PostgreSQL via async SQLAlchemy (Users, Sessions, Messages)

## Conventions for AI Assistants

### General Principles

1. **Respect the project's ethical mission.** All code and content must be non-dogmatic, inclusive, and respectful of diverse spiritual traditions and secular perspectives.
2. **Preserve human autonomy.** The system should guide and suggest, never coerce or manipulate.
3. **Keep it simple.** Prefer clear, maintainable code over clever abstractions.
4. **No hardcoded spiritual bias.** Avoid embedding assumptions about any specific religion, philosophy, or spiritual tradition into core logic.

### Code Contributions

- Read existing code before modifying it
- Make minimal, focused changes — avoid scope creep
- Do not add unnecessary dependencies
- Write clear commit messages that explain the "why"
- Do not commit secrets, API keys, or credentials (use `.env`)
- Backend: follow `ruff` linting and `mypy` strict type checking
- Frontend: follow ESLint + Prettier conventions, use TypeScript strictly

### When Adding New Features

1. **Backend:** Add route in `api/routes/`, schema in `schemas/`, service logic in `services/`, model in `models/`
2. **Frontend:** Add page in `pages/`, component in `components/<domain>/`, types in `types/`
3. **Tests:** Add unit tests in `tests/unit/`, integration tests in `tests/integration/`
4. **Update this file** when project structure or workflows change

## Key Domain Concepts

- **Agentic AI:** The system operates autonomously within ethical boundaries
- **Spiritual guidance:** Reflective prompts, mindfulness exercises, and well-being support — not medical or psychological advice
- **Context adaptation:** Adapts to user emotions, values, and personal context
- **Non-dogmatic approach:** Guidance is universal, not tied to any specific religious framework
- **Conscious living:** Supporting intentional and mindful living

## Environment Variables

See `backend/.env.example` for the full list. Key variables:

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | PostgreSQL connection string |
| `SECRET_KEY` | JWT signing key (change in production) |
| `ANTHROPIC_API_KEY` | Anthropic Claude API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `DEFAULT_LLM_PROVIDER` | `anthropic` or `openai` |
| `DEFAULT_MODEL` | Model ID (e.g. `claude-sonnet-4-5-20250929`) |
