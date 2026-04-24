# Project Structure Documentation

## Overview

AI Film Studio is a full-stack application with a FastAPI backend and Next.js frontend.

## Directory Structure

```
AI-Film-Studio/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API Routes
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/ # API endpoint handlers
│   │   │   │   └── router.py  # API router configuration
│   │   │   └── routes/        # Additional routes
│   │   ├── agents/            # AI Agent implementations
│   │   ├── core/              # Core configuration
│   │   │   ├── config.py      # Application settings
│   │   │   └── __init__.py
│   │   ├── db/                # Database layer
│   │   │   ├── session.py     # Database session management
│   │   │   └── __init__.py    # Database initialization
│   │   ├── models/            # SQLAlchemy models
│   │   │   ├── base.py        # Base model class
│   │   │   ├── project.py     # Project model
│   │   │   ├── script.py      # Script model
│   │   │   ├── scene.py       # Scene model
│   │   │   └── __init__.py
│   │   ├── schemas/           # Pydantic schemas
│   │   │   └── __init__.py    # Request/Response schemas
│   │   ├── services/          # Business logic
│   │   │   ├── ai_generator.py
│   │   │   ├── ai_services.py
│   │   │   ├── audio_generator.py
│   │   │   ├── storage_service.py
│   │   │   ├── video_generator.py
│   │   │   ├── video_service.py
│   │   │   └── __init__.py
│   │   ├── middleware/        # Custom middleware
│   │   │   ├── error_handler.py  # Error handling
│   │   │   ├── logging.py        # Request logging
│   │   │   └── __init__.py
│   │   ├── tasks/             # Celery tasks
│   │   │   ├── celery.py
│   │   │   └── __init__.py
│   │   └── utils/             # Utility functions
│   │       └── __init__.py
│   ├── alembic/               # Database migrations
│   │   ├── versions/          # Migration files
│   │   ├── env.py             # Alembic environment
│   │   └── script.py.mako     # Migration template
│   ├── tests/                 # Backend tests
│   │   ├── api/               # API tests
│   │   ├── services/          # Service tests
│   │   ├── conftest.py        # Test fixtures
│   │   └── test_main.py       # Main app tests
│   ├── main.py                # Application entry point
│   ├── requirements.txt       # Python dependencies
│   ├── pytest.ini             # Pytest configuration
│   ├── alembic.ini            # Alembic configuration
│   ├── Dockerfile             # Backend Docker image
│   └── .env.example           # Environment template
│
├── frontend/                  # Next.js Frontend
│   ├── app/                   # Next.js App Router
│   │   ├── create/            # Create page
│   │   ├── globals.css        # Global styles
│   │   ├── layout.tsx         # Root layout
│   │   ├── page.tsx           # Home page
│   │   └── providers.tsx      # Context providers
│   ├── components/            # React components
│   ├── lib/                   # Frontend utilities
│   ├── public/                # Static assets
│   ├── package.json           # Node dependencies
│   ├── next.config.js         # Next.js configuration
│   ├── tailwind.config.js     # Tailwind configuration
│   ├── tsconfig.json          # TypeScript configuration
│   ├── Dockerfile             # Frontend Docker image
│   └── .env.local.example     # Environment template
│
├── .github/                   # GitHub configuration
│   └── workflows/
│       └── ci.yml             # CI/CD pipeline
│
├── docs/                      # Documentation
│
├── docker-compose.yml         # Docker Compose configuration
├── setup.sh                   # Setup script
├── QUICKSTART.md              # Quick setup guide
├── CONTRIBUTING.md            # Contributing guidelines
├── README.md                  # Main documentation
└── .gitignore                 # Git ignore rules
```

## Key Components

### Backend

#### Models (`app/models/`)
Database models using SQLAlchemy:
- **Base**: Base model with common fields (id, created_at, updated_at)
- **Project**: Film project information
- **Script**: Generated scripts
- **Scene**: Individual scenes with media

#### Schemas (`app/schemas/`)
Pydantic models for request/response validation:
- Request validation
- Response serialization
- Data transformation

#### API Endpoints (`app/api/v1/endpoints/`)
- `projects.py` - Project management
- `scripts.py` - Script generation
- `scenes.py` - Scene generation
- `storyboards.py` - Storyboard creation
- `voiceovers.py` - Voice synthesis
- `videos.py` - Video compilation

#### Services (`app/services/`)
Business logic layer:
- AI generation services
- Media processing
- Storage management
- Video compilation

#### Middleware (`app/middleware/`)
- Error handling with detailed responses
- Request/response logging
- Performance monitoring

#### Database (`app/db/`)
- Session management
- Connection pooling
- Transaction handling

### Frontend

#### App Router (`app/`)
Next.js 14+ App Router structure:
- Server-side rendering
- Nested layouts
- Loading states
- Error boundaries

#### Components
Reusable React components:
- Form components
- UI elements
- Layout components

### Infrastructure

#### Docker
- Multi-stage builds
- Service orchestration
- Development and production configs

#### CI/CD
- Automated testing
- Build verification
- Deployment pipeline

#### Database Migrations
- Alembic for schema management
- Version-controlled migrations
- Rollback support

## Technology Stack

### Backend
- **Framework**: FastAPI 0.109
- **ORM**: SQLAlchemy 2.0
- **Validation**: Pydantic 2.5
- **Database**: PostgreSQL / SQLite
- **Cache**: Redis
- **Task Queue**: Celery
- **Testing**: Pytest

### Frontend
- **Framework**: Next.js 16
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State**: Zustand
- **Queries**: React Query
- **Forms**: React Hook Form

### AI/ML
- **LLM**: OpenAI GPT-4
- **Voice**: ElevenLabs
- **Images**: Stability AI
- **Video**: Replicate

## Development Practices

### Code Organization
- Separation of concerns
- Dependency injection
- Service layer pattern
- Repository pattern

### Testing
- Unit tests
- Integration tests
- API tests
- End-to-end tests

### Documentation
- Code comments
- API documentation
- Architecture diagrams
- Setup guides

## Configuration

### Environment Variables
Backend requires:
- `DATABASE_URL` - Database connection
- `OPENAI_API_KEY` - OpenAI API key
- `SECRET_KEY` - Application secret

Frontend requires:
- `NEXT_PUBLIC_API_URL` - Backend API URL

See `.env.example` files for complete list.

## Deployment

### Docker Deployment
```bash
docker-compose up -d
```

### Manual Deployment
1. Set up PostgreSQL and Redis
2. Configure environment variables
3. Run database migrations
4. Start backend server
5. Build and serve frontend

## Maintenance

### Database Migrations
```bash
# Create migration
alembic revision --autogenerate -m "description"

# Apply migration
alembic upgrade head

# Rollback
alembic downgrade -1
```

### Dependencies
- Regular security updates
- Version pinning
- Compatibility testing

## Support

For issues and questions:
- GitHub Issues
- Documentation
- Contributing guide
