# AI Film Studio - Getting Started Guide

## 🎯 What is AI Film Studio?

AI Film Studio is an end-to-end video production platform that uses AI to automate:
- ✍️ Scriptwriting
- 🎨 Storyboarding
- 🎬 Scene generation
- 🎤 Voiceovers
- ✂️ Video editing

## 🚀 Quick Start (5 minutes)

### Option 1: Using Docker (Recommended)

1. **Install Docker Desktop**
   - Download from [docker.com](https://www.docker.com/products/docker-desktop/)

2. **Clone and setup**
   ```bash
   git clone https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio.git
   cd AI-Film-Studio
   
   # Copy environment files
   cp backend/.env.example backend/.env
   cp frontend/.env.local.example frontend/.env.local
   ```

3. **Add your AI API keys**
   Edit `backend/.env` and add your API keys:
   ```bash
   OPENAI_API_KEY=sk-your-key-here
   # Add other keys as needed
   ```

4. **Start the application**
   ```bash
   docker-compose up -d
   ```

5. **Open your browser**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000/docs

### Option 2: Local Development

#### Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your API keys

# Start PostgreSQL and Redis (or use Docker)
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=changeme postgres:16
docker run -d -p 6379:6379 redis:7

# Run the backend
uvicorn main:app --reload
```

#### Frontend Setup
```bash
cd frontend

# Install dependencies
npm install

# Setup environment
cp .env.local.example .env.local

# Start development server
npm run dev
```

## 🔑 Getting API Keys

You'll need API keys for AI services:

### OpenAI (Required)
1. Go to [platform.openai.com](https://platform.openai.com)
2. Create an account
3. Navigate to API Keys
4. Create a new key
5. Add to `backend/.env`: `OPENAI_API_KEY=sk-...`

### ElevenLabs (Optional - for voiceovers)
1. Go to [elevenlabs.io](https://elevenlabs.io)
2. Sign up
3. Get API key from profile
4. Add to `backend/.env`: `ELEVENLABS_API_KEY=...`

### Stability AI (Optional - for images)
1. Go to [stability.ai](https://stability.ai)
2. Create account
3. Get API key
4. Add to `backend/.env`: `STABILITY_API_KEY=...`

## 📖 Creating Your First Video

1. **Access the app** at http://localhost:3000

2. **Create a new project**
   - Click "Start Your First Project"
   - Enter project details

3. **Generate a script**
   - Provide a prompt: "Create a 60-second video about space exploration"
   - AI will generate a script

4. **Create storyboard**
   - AI generates visual frames from script

5. **Generate scenes**
   - AI creates video clips for each scene

6. **Add voiceover**
   - AI synthesizes narration

7. **Compile video**
   - System assembles final video

8. **Download**
   - Export your finished video

## 🛠️ Development Commands

### Backend
```bash
# Run tests
pytest

# Format code
black .

# Lint
flake8

# Database migrations (when ready)
alembic upgrade head
```

### Frontend
```bash
# Run tests
npm test

# Build for production
npm run build

# Start production server
npm start

# Lint
npm run lint
```

### Docker
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild containers
docker-compose up -d --build

# Clean everything
docker-compose down -v
```

## 🐛 Troubleshooting

### Port already in use
```bash
# Find process using port
lsof -i :8000  # Backend
lsof -i :3000  # Frontend

# Kill process
kill -9 <PID>
```

### Database connection issues
```bash
# Restart PostgreSQL
docker-compose restart postgres

# Check logs
docker-compose logs postgres
```

### Frontend won't start
```bash
# Clear cache and reinstall
cd frontend
rm -rf node_modules .next
npm install
npm run dev
```

## 📚 Next Steps

- Read [ARCHITECTURE.md](ARCHITECTURE.md) for technical details
- Check [API Documentation](http://localhost:8000/docs)
- Explore the codebase
- Start building features!

## 💬 Need Help?

- Create an issue on GitHub
- Check existing documentation
- Review API docs at `/docs`

## ⚡ Tips

1. **Start small**: Test with short videos first
2. **Use good prompts**: Clear, detailed prompts = better results
3. **Monitor costs**: AI APIs can be expensive
4. **Save API keys**: Never commit them to git
5. **Check logs**: Use `docker-compose logs -f` to debug
