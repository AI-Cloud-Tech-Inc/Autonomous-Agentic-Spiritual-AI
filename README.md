# AI Film Studio

> The world's first fully autonomous AI film studio powered by collaborative AI agents — by **AI Cloud Tech Inc**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/next.js-14-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.109-green.svg)](https://fastapi.tiangolo.com/)

---

## The Agent Crew

Six autonomous AI agents collaborate to create your films:

| Agent | Role | Capabilities |
|-------|------|-------------|
| **Director** | Creative Visionary | Interprets concepts, makes artistic decisions, coordinates agents |
| **Screenwriter** | Storyteller | Writes scripts, develops character arcs, maintains consistency |
| **Cinematographer** | Visual Artist | Plans shots, lighting, compositions, visual continuity |
| **Sound Designer** | Audio Architect | Music selection, soundscapes, audio mixing, synchronization |
| **VFX** | Enhancement Specialist | Visual effects, color grading, CGI, quality assurance |
| **Editor** | Pacing Expert | Assembles scenes, timing, transitions, cut decisions |

### Features

- **Autonomous Film Pipeline** - Create a film from a single text prompt
- **AI Scriptwriting** - Generate professional scripts via Claude/GPT-4
- **Smart Storyboarding** - Automatic visual planning from scripts
- **Scene Generation** - AI-powered video scene creation
- **Voice Synthesis** - Natural voiceovers via ElevenLabs
- **VFX & Color Grading** - Automated visual effects pipeline
- **Auto Editing** - Intelligent timeline assembly and compilation
- **Multi-Format** - Support for landscape, portrait, and square videos

Learn more: [Agent Architecture](./AGENT_ARCHITECTURE.md)

---

## Quick Start

### Using Docker (Recommended)

```bash
git clone https://github.com/AI-Cloud-Tech-Inc/Autonomous-Agentic-Spiritual-AI.git
cd Autonomous-Agentic-Spiritual-AI

cp backend/.env.example backend/.env
# Add your ANTHROPIC_API_KEY to backend/.env

docker-compose up -d

# Frontend: http://localhost:3000
# Backend API: http://localhost:8000/docs
```

### Manual Setup

```bash
# Backend
cd backend
cp .env.example .env
pip install -r requirements.txt
uvicorn main:app --reload            # http://localhost:8000

# Frontend (new terminal)
cd frontend
npm install
npm run dev                          # http://localhost:3000
```

---

## Film Creation Workflow

1. **Director** creates vision + scene breakdown from your prompt
2. **Screenwriter** writes dialogue, narration, and audio cues per scene
3. **Cinematographer** plans camera, lighting, and color palette per shot
4. **Sound Designer** designs music, SFX, and voiceover direction
5. **VFX** applies color grading and visual enhancements
6. **Editor** assembles the final timeline with transitions

All via a single API call: `POST /api/v1/autonomous/create-film`

---

## API Endpoints

| Method | Endpoint | Status |
|--------|----------|--------|
| POST | `/api/v1/autonomous/create-film` | **Implemented** |
| GET | `/api/v1/autonomous/projects` | **Implemented** |
| GET | `/api/v1/autonomous/projects/{id}` | **Implemented** |
| GET | `/api/v1/autonomous/agent-status` | **Implemented** |
| * | `/api/v1/projects/*` | Stub |
| * | `/api/v1/scripts/*` | Partial |
| * | `/api/v1/scenes/*` | Stub |
| * | `/api/v1/storyboards/*` | Stub |
| * | `/api/v1/voiceovers/*` | Partial |
| * | `/api/v1/videos/*` | Stub |

Full API documentation: http://localhost:8000/docs

---

## Required API Keys

- **Anthropic** (Required) - [Get API Key](https://console.anthropic.com) — powers all 6 agents
- **OpenAI** (Optional) - [Get API Key](https://platform.openai.com) — script generation fallback
- **ElevenLabs** (Optional) - [Get API Key](https://elevenlabs.io) — voice synthesis
- **Stability AI** (Optional) - [Get API Key](https://stability.ai) — image generation

Add these to `backend/.env`.

---

## Technology Stack

### Backend
- **FastAPI** — Python web framework
- **PostgreSQL** — Primary database
- **Redis** — Caching and task queue
- **Celery** — Background job processing
- **Anthropic Claude** — AI agent backbone
- **ElevenLabs** — Voice synthesis
- **Stability AI** — Image generation

### Frontend
- **Next.js 14** — React framework
- **TypeScript** — Type safety
- **Tailwind CSS** — Styling
- **React Query** — Data fetching
- **Framer Motion** — Animations

---

## Documentation

- **[Quick Start Guide](QUICKSTART.md)**
- **[Project Structure](PROJECT_STRUCTURE.md)**
- **[Agent Architecture](AGENT_ARCHITECTURE.md)**
- **[Development Guide](DEVELOPMENT.md)**
- **[Contributing Guide](CONTRIBUTING.md)**
- **[API Documentation](http://localhost:8000/docs)**

---

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License — see [LICENSE](LICENSE).

## Contact

- **GitHub**: [AI-Cloud-Tech-Inc](https://github.com/AI-Cloud-Tech-Inc)
- **Issues**: [Report a bug](https://github.com/AI-Cloud-Tech-Inc/Autonomous-Agentic-Spiritual-AI/issues)

---

Made with care by AI Cloud Tech Inc
