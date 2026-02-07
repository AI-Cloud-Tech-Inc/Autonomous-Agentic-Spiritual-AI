#!/usr/bin/env bash
set -euo pipefail

# Start backend and frontend in development mode (requires tmux or two terminals)
echo "=== Autonomous Agentic Spiritual AI — Dev Server ==="
echo ""
echo "Start each service in a separate terminal:"
echo ""
echo "  Backend:   cd backend && pip install -e '.[dev]' && uvicorn app.main:app --reload"
echo "  Frontend:  cd frontend && npm install && npm run dev"
echo ""
echo "Or use Docker Compose:"
echo "  docker compose up --build"
