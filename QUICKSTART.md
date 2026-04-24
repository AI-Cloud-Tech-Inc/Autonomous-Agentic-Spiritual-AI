# Quick Setup Guide

This guide will get you up and running with AI Film Studio in minutes.

## Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- Docker and Docker Compose (optional, for containerized setup)
- PostgreSQL (optional, SQLite works for development)
- Redis (optional, for task queue)

## Quick Start

### Option 1: Automated Setup (Recommended)

Run the setup script:

```bash
./setup.sh
```

This will:
- Create Python virtual environment
- Install all backend dependencies
- Install all frontend dependencies
- Create `.env` files from templates

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Update .env with your API keys (at minimum, add OPENAI_API_KEY)
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Copy environment template
cp .env.local.example .env.local
```

## Running the Application

### Development Mode

#### Start Backend
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

Backend will be available at: http://localhost:8000
API docs at: http://localhost:8000/docs

#### Start Frontend
```bash
cd frontend
npm run dev
```

Frontend will be available at: http://localhost:3000

### Docker Mode

```bash
# Build and start all services
docker-compose up --build

# Stop services
docker-compose down
```

## Database Setup

### Using SQLite (Default)

No additional setup needed. The database file will be created automatically.

### Using PostgreSQL

1. Update `backend/.env`:
   ```
   DATABASE_URL=postgresql://user:password@localhost:5432/ai_film_studio
   ```

2. Run migrations:
   ```bash
   cd backend
   source venv/bin/activate
   alembic upgrade head
   ```

## Environment Variables

### Required
- `OPENAI_API_KEY` - Get from [OpenAI](https://platform.openai.com)

### Optional
- `ELEVENLABS_API_KEY` - For voice synthesis
- `STABILITY_API_KEY` - For image generation
- `ANTHROPIC_API_KEY` - For Claude AI
- `REPLICATE_API_TOKEN` - For video generation

## Testing

### Backend Tests
```bash
cd backend
source venv/bin/activate
pytest tests/ -v
```

### Frontend Build
```bash
cd frontend
npm run build
```

## Troubleshooting

### Backend won't start
- Ensure Python 3.11+ is installed
- Check that all dependencies are installed
- Verify `.env` file exists with required keys

### Frontend won't build
- Ensure Node.js 18+ is installed
- Try deleting `node_modules` and running `npm install` again
- Check for TypeScript errors with `npm run lint`

### Database errors
- Ensure DATABASE_URL is correct
- Run migrations: `alembic upgrade head`
- Check PostgreSQL/Redis are running

## Next Steps

1. Read the [Development Guide](DEVELOPMENT.md)
2. Check the [Contributing Guidelines](CONTRIBUTING.md)
3. Review the [API Documentation](http://localhost:8000/docs)

## Support

- GitHub Issues: [Report a bug](https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio/issues)
- Documentation: Check the `docs/` directory
