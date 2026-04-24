# AI Film Studio - Architecture Documentation

## 🎬 Project Overview

AI Film Studio is a cloud-based AI platform that automates end-to-end video production, from scriptwriting and storyboarding to scene generation, voiceovers, and editing.

## 🏗️ System Architecture

### Architecture Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                             │
│                      (Next.js + React)                       │
│                    Port: 3000                                │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/REST API
┌──────────────────────▼──────────────────────────────────────┐
│                    Backend API                               │
│                  (FastAPI + Python)                          │
│                    Port: 8000                                │
├─────────────────────────────────────────────────────────────┤
│  Endpoints:                                                  │
│  • /api/v1/projects    - Project management                 │
│  • /api/v1/scripts     - AI script generation               │
│  • /api/v1/storyboards - Storyboard creation                │
│  • /api/v1/scenes      - Video scene generation             │
│  • /api/v1/voiceovers  - AI voice synthesis                 │
│  • /api/v1/videos      - Video compilation                  │
└──────────────┬────────────────────┬─────────────────────────┘
               │                    │
    ┌──────────▼────────┐  ┌───────▼────────┐
    │   PostgreSQL      │  │     Redis      │
    │   Database        │  │  Cache/Queue   │
    │   Port: 5432      │  │  Port: 6379    │
    └───────────────────┘  └────────────────┘
               │                    │
    ┌──────────▼────────────────────▼────────┐
    │         Celery Workers                  │
    │    (Background Task Processing)         │
    └─────────────────────────────────────────┘
               │
    ┌──────────▼────────────────────────────┐
    │      AI Service Integrations          │
    ├───────────────────────────────────────┤
    │ • OpenAI (GPT-4) - Scripts            │
    │ • Stability AI - Image Generation     │
    │ • Replicate - Video Generation        │
    │ • ElevenLabs - Voice Synthesis        │
    └───────────────────────────────────────┘
```

## 📁 Project Structure

```
AI-Film-Studio/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   │   └── v1/
│   │   │       ├── endpoints/ # Individual endpoint modules
│   │   │       │   ├── projects.py
│   │   │       │   ├── scripts.py
│   │   │       │   ├── storyboards.py
│   │   │       │   ├── scenes.py
│   │   │       │   ├── voiceovers.py
│   │   │       │   └── videos.py
│   │   │       └── router.py  # Main API router
│   │   ├── core/              # Core configurations
│   │   │   └── config.py      # Settings and configs
│   │   ├── models/            # Database models (TODO)
│   │   ├── schemas/           # Pydantic schemas (TODO)
│   │   ├── services/          # Business logic (TODO)
│   │   └── tasks/             # Celery tasks
│   │       └── celery.py      # Task definitions
│   ├── main.py                # Application entry point
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Backend container
│   └── .env.example          # Environment variables template
│
├── frontend/                  # Next.js Frontend
│   ├── app/
│   │   ├── layout.tsx        # Root layout
│   │   ├── page.tsx          # Homepage
│   │   ├── providers.tsx     # React Query provider
│   │   └── globals.css       # Global styles
│   ├── components/           # React components (TODO)
│   ├── lib/                  # Utilities (TODO)
│   ├── package.json          # Node dependencies
│   ├── tsconfig.json         # TypeScript config
│   ├── tailwind.config.js    # Tailwind CSS config
│   ├── next.config.js        # Next.js config
│   └── Dockerfile           # Frontend container
│
├── docker-compose.yml        # Docker orchestration
├── .gitignore               # Git ignore rules
├── README.md                # Project documentation
└── LICENSE                  # License file
```

## 🔧 Technology Stack

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database**: PostgreSQL 16
- **Cache/Queue**: Redis 7
- **Task Queue**: Celery
- **API Documentation**: Auto-generated OpenAPI/Swagger

### Frontend
- **Framework**: Next.js 14 (React 18)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Data Fetching**: React Query (@tanstack/react-query)
- **Forms**: React Hook Form + Zod
- **Animations**: Framer Motion

### AI Services
- **OpenAI GPT-4**: Script generation
- **Anthropic Claude**: Alternative text generation
- **Stability AI**: Image generation for storyboards
- **Replicate**: Video generation
- **ElevenLabs**: Voice synthesis

### DevOps
- **Containerization**: Docker + Docker Compose
- **Development**: Hot reload enabled
- **Production**: Ready for cloud deployment (AWS/Azure/GCP)

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Compose
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio.git
   cd AI-Film-Studio
   ```

2. **Set up environment variables**
   ```bash
   # Backend
   cp backend/.env.example backend/.env
   # Edit backend/.env and add your API keys
   
   # Frontend
   cp frontend/.env.local.example frontend/.env.local
   ```

3. **Start all services**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Development Without Docker

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

## 📊 Workflow

1. **Create Project** → User creates a new video project
2. **Generate Script** → AI generates script based on prompt
3. **Create Storyboard** → AI creates visual storyboard from script
4. **Generate Scenes** → AI generates video scenes from storyboard
5. **Add Voiceover** → AI synthesizes voiceover from script
6. **Compile Video** → System compiles all assets into final video
7. **Export** → User downloads the finished video

## 🔐 Security Considerations

- API keys stored in environment variables
- Database credentials in .env files
- CORS configured for specific origins
- Input validation using Pydantic
- File upload size limits

## 📈 Scalability

- Horizontal scaling with container orchestration (Kubernetes ready)
- Background processing with Celery workers
- Redis caching for improved performance
- CDN integration for media files
- Database connection pooling

## 🛠️ Next Steps

1. Implement database models (SQLAlchemy)
2. Create Pydantic schemas
3. Build AI service integrations
4. Develop frontend components
5. Add authentication & authorization
6. Implement file storage (S3/Azure Blob)
7. Set up CI/CD pipeline
8. Add monitoring & logging
9. Write tests
10. Deploy to cloud

## 📝 API Endpoints

See [API Documentation](http://localhost:8000/docs) after starting the backend.

## 🤝 Contributing

Contributions are welcome! Please read our contributing guidelines before submitting PRs.

## 📄 License

See LICENSE file for details.
