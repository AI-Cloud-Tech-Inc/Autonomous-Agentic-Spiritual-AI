#!/bin/bash

# AI Film Studio - Setup Script
# This script sets up the development environment
# 
# Note: Windows users should use setup.ps1 or manually follow QUICKSTART.md
# On Windows with Git Bash, you may need to adjust the venv activation path

set -e

echo "🎬 Setting up AI Film Studio..."

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18 or higher."
    exit 1
fi

echo -e "${BLUE}📦 Installing backend dependencies...${NC}"
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Created Python virtual environment"
fi

# Activate virtual environment (Linux/Mac)
# Windows users: use venv\Scripts\activate instead
source venv/bin/activate

# Install Python dependencies
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}✅ Backend dependencies installed${NC}"

# Setup environment file
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "✅ Created .env file from template"
    echo "⚠️  Please update .env with your API keys"
fi

cd ..

echo -e "${BLUE}📦 Installing frontend dependencies...${NC}"
cd frontend

# Install Node dependencies
npm install
echo -e "${GREEN}✅ Frontend dependencies installed${NC}"

# Setup environment file
if [ ! -f ".env.local" ]; then
    cp .env.local.example .env.local
    echo "✅ Created .env.local file from template"
fi

cd ..

echo -e "${BLUE}📦 Installing root dependencies...${NC}"
npm install
echo -e "${GREEN}✅ Root dependencies installed${NC}"

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo "Next steps:"
echo "1. Update backend/.env with your API keys (OPENAI_API_KEY, etc.)"
echo "2. Start the development servers:"
echo "   - Using Docker: docker-compose up"
echo "   - Manual: npm run dev"
echo ""
echo "Access the application:"
echo "   - Frontend: http://localhost:3000"
echo "   - Backend API: http://localhost:8000/docs"
