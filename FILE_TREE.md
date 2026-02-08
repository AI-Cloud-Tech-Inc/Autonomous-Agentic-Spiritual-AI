# Autonomous Agentic Spiritual AI - Project Structure

```
Autonomous-Agentic-Spiritual-AI/
│
├── .env.example                  # Environment variables template
├── .gitignore                     # Git ignore rules
├── CLAUDE.md                      # Claude AI assistant instructions
├── docker-compose.yaml            # Docker Compose configuration
├── LICENSE                        # Project license
├── README.md                      # Project documentation
├── requirements.txt              # Python dependencies
├── files (1).zip                  # Archived files
│
├── .qodo/                         # Qodo configuration directory
│
├── backend/                       # Backend API service (Flask/FastAPI)
│   ├── main.py                    # Backend entry point
│   ├── requirements.txt          # Backend dependencies
│   ├── app/
│   │   ├── __init__.py
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes/
│   │   │       ├── __init__.py
│   │   │       ├── chat.py        # Chat API endpoints
│   │   │       ├── health.py      # Health check endpoints
│   │   │       ├── sessions.py    # Session management
│   │   │       └── users.py       # User management
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── security.py        # Security utilities
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   └── session.py         # Database session
│   │   └── models/
│   │       ├── __init__.py
│   │       ├── base.py            # Base model class
│   │       ├── message.py         # Message model
│   │       └── session.py         # Session model
│   │
│   └── Dockerfile                # Backend Docker image
│
├── config/                        # Configuration files
│   └── config.yaml               # Main configuration file
│
├── data/                         # Data directories
│   ├── prompts/                  # Prompt templates
│   │   └── meditation_prompts.md # Meditation guidance prompts
│   ├── teachings/               # Spiritual teachings content
│   └── user_data/               # User-specific data storage
│
├── docker/                       # Docker configurations
│   └── (Docker-related files)
│
├── frontend/                     # Frontend application (React)
│   ├── index.html               # HTML entry point
│   ├── package.json             # Node.js dependencies
│   ├── package-lock.json        # Locked dependency versions
│   ├── vite.config.js           # Vite build configuration
│   └── src/
│       ├── App.jsx              # Main React component
│       └── main.jsx             # React entry point
│
├── scripts/                      # Utility scripts
│   └── (Build/deployment scripts)
│
├── src/                         # Main source code (Spiritual AI Agent)
│   ├── __init__.py
│   ├── main.py                  # Main entry point for CLI agent
│   ├── core/
│   │   ├── __init__.py
│   │   ├── agent.py             # SpiritualAgent core class
│   │   └── constants.py         # Application constants (greetings, prompts)
│   ├── dialogue/
│   │   ├── __init__.py
│   │   └── conversation_handler.py # Conversation management
│   ├── memory/
│   │   ├── __init__.py
│   │   └── memory_manager.py    # User memory & context storage
│   ├── reasoning/
│   │   ├── __init__.py
│   │   └── context_analyzer.py  # Context analysis & understanding
│   └── utils/
│       ├── __init__.py
│       └── (Utility functions)
│
└── tests/                       # Test files
    └── integration/
        └── (Integration tests)
```

## Directory Purpose Summary

| Directory   | Purpose                               |
| ----------- | ------------------------------------- |
| `backend/`  | REST API service for web-based access |
| `frontend/` | React web application UI              |
| `src/`      | Core Spiritual AI Agent (CLI)         |
| `config/`   | Application configuration             |
| `data/`     | Prompts, teachings, user data         |
| `docker/`   | Container deployment configs          |
| `scripts/`  | Build and utility scripts             |

## Key Files

- **[`src/main.py`](src/main.py)**: CLI entry point - run with `python src/main.py`
- **[`backend/main.py`](backend/main.py)**: Backend API server entry point
- **[`config/config.yaml`](config/config.yaml)**: Main configuration file
- **[`frontend/src/App.jsx`](frontend/src/App.jsx)**: Frontend React application
