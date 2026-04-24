# Autonomous-Agentic-Spiritual-AI + AI Film Studio

> A unified platform by **AI Cloud Tech Inc** combining two autonomous agentic AI systems:
> - **Spiritual AI Agent** — supports inner growth, reflection, and well-being through ethical, non-dogmatic guidance
> - **AI Film Studio** — the world's first fully autonomous AI film studio powered by collaborative AI agents

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/next.js-14-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-0.109-green.svg)](https://fastapi.tiangolo.com/)

---

## Spiritual AI Agent

An Autonomous Agentic AI Spiritual Agent designed to support inner growth, reflection, and well-being. It adapts to user context, emotions, and values, offering ethical, non-dogmatic guidance for mindfulness, self-awareness, and conscious living while preserving human autonomy.

---

## AI Film Studio

### The Agent Crew

Meet the autonomous AI agents that create your films:

| Agent | Role | Capabilities |
|-------|------|-------------|
| **Director Agent** | Creative Visionary | Interprets concepts, makes artistic decisions, coordinates agents |
| **Screenwriter Agent** | Storyteller | Writes scripts, develops character arcs, maintains consistency |
| **Cinematographer Agent** | Visual Artist | Plans shots, lighting, compositions, visual continuity |
| **Editor Agent** | Pacing Expert | Assembles scenes, timing, transitions, cut decisions |
| **Sound Designer Agent** | Audio Architect | Music selection, soundscapes, audio mixing, synchronization |
| **VFX Agent** | Enhancement Specialist | Visual effects, color grading, CGI, quality assurance |

### Features

- **AI Scriptwriting** - Generate professional video scripts using GPT-4
- **Smart Storyboarding** - Automatic visual planning from scripts
- **Scene Generation** - AI-powered video scene creation
- **Voice Synthesis** - Natural voiceovers in multiple languages
- **Auto Editing** - Intelligent video compilation and editing
- **Multi-Format** - Support for landscape, portrait, and square videos

Learn more: [Agent Architecture](./AGENT_ARCHITECTURE.md)

---

## Quick Start

### Using Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/AI-Cloud-Tech-Inc/Autonomous-Agentic-Spiritual-AI.git
cd Autonomous-Agentic-Spiritual-AI

# Setup environment variables
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local

# Add your API keys to backend/.env

# Start all services
docker-compose up -d

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000/docs
```

### Using Setup Script

```bash
./setup.sh
# Add your API keys to backend/.env
npm run dev
```

## Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in minutes
- **[Project Structure](PROJECT_STRUCTURE.md)** - Understand the codebase
- **[Contributing Guide](CONTRIBUTING.md)** - How to contribute
- **[Development Guide](DEVELOPMENT.md)** - Detailed development instructions
- **[Agent Architecture](AGENT_ARCHITECTURE.md)** - AI agent system design
- **[API Documentation](http://localhost:8000/docs)** - Interactive API docs

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **PostgreSQL** - Primary database
- **Redis** - Caching and task queue
- **Celery** - Background job processing
- **OpenAI GPT-4** - Script generation
- **ElevenLabs** - Voice synthesis
- **Stability AI** - Image generation

### Frontend
- **Next.js 14** - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **React Query** - Data fetching
- **Framer Motion** - Animations

## Project Structure

```
Autonomous-Agentic-Spiritual-AI/
├── backend/           # FastAPI backend
│   ├── app/
│   │   ├── api/      # API endpoints
│   │   ├── services/ # Business logic
│   │   ├── tasks/    # Celery tasks
│   │   └── core/     # Configuration
│   └── main.py       # Application entry
├── frontend/         # Next.js frontend
│   ├── app/         # Pages and layouts
│   ├── components/  # React components
│   └── lib/         # Utilities
├── src/             # Spiritual AI agent core
├── Film-Agent/      # Film agent modules
├── docs/            # Documentation
└── docker-compose.yml
```

## Film Studio Workflow

1. **Create Project** → Define video parameters
2. **Generate Script** → AI creates the narrative
3. **Storyboard** → Visual scene planning
4. **Generate Scenes** → AI creates video clips
5. **Add Voiceover** → Synthesize narration
6. **Compile** → Assemble final video
7. **Export** → Download your video

## Required API Keys

- **OpenAI** (Required) - [Get API Key](https://platform.openai.com)
- **ElevenLabs** (Optional) - [Get API Key](https://elevenlabs.io)
- **Stability AI** (Optional) - [Get API Key](https://stability.ai)
- **Anthropic** (Optional) - [Get API Key](https://console.anthropic.com)

Add these to `backend/.env` file.

## Development

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `POST /api/v1/projects/` - Create new project
- `POST /api/v1/scripts/generate` - Generate script
- `POST /api/v1/storyboards/generate` - Create storyboard
- `POST /api/v1/scenes/generate` - Generate video scene
- `POST /api/v1/voiceovers/generate` - Create voiceover
- `POST /api/v1/videos/compile` - Compile final video

Full API documentation: http://localhost:8000/docs

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **GitHub**: [AI-Cloud-Tech-Inc](https://github.com/AI-Cloud-Tech-Inc)
- **Issues**: [Report a bug](https://github.com/AI-Cloud-Tech-Inc/Autonomous-Agentic-Spiritual-AI/issues)

---

Made with care by AI Cloud Tech Inc
