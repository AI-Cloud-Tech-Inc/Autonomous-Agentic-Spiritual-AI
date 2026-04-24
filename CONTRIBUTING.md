# Contributing to AI Film Studio

Thank you for your interest in contributing to AI Film Studio! This document provides guidelines and instructions for contributing.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio.git
   cd AI-Film-Studio
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```

3. **Configure environment variables**
   - Update `backend/.env` with your API keys
   - Update `frontend/.env.local` if needed

## Project Structure

```
AI-Film-Studio/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/         # API endpoints
│   │   ├── models/      # Database models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # Business logic
│   │   ├── middleware/  # Custom middleware
│   │   ├── utils/       # Utility functions
│   │   └── core/        # Configuration
│   ├── alembic/         # Database migrations
│   ├── tests/           # Backend tests
│   └── requirements.txt
├── frontend/            # Next.js frontend
│   ├── app/            # Next.js App Router
│   ├── components/     # React components
│   └── lib/            # Frontend utilities
└── docker-compose.yml
```

## Development Workflow

### Backend Development

1. **Activate virtual environment**
   ```bash
   cd backend
   source venv/bin/activate
   ```

2. **Run development server**
   ```bash
   uvicorn main:app --reload
   ```

3. **Run tests**
   ```bash
   pytest tests/ -v
   ```

4. **Create database migration**
   ```bash
   alembic revision --autogenerate -m "Description"
   ```

5. **Apply migrations**
   ```bash
   alembic upgrade head
   ```

### Frontend Development

1. **Run development server**
   ```bash
   cd frontend
   npm run dev
   ```

2. **Run linter**
   ```bash
   npm run lint
   ```

3. **Build for production**
   ```bash
   npm run build
   ```

## Coding Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for all functions and classes
- Keep functions focused and small
- Use meaningful variable names

### TypeScript/JavaScript (Frontend)

- Follow ESLint configuration
- Use TypeScript for type safety
- Write self-documenting code
- Use functional components with hooks
- Keep components small and reusable

## Testing

- Write tests for new features
- Maintain test coverage above 80%
- Test edge cases and error conditions
- Use descriptive test names

## Pull Request Process

1. Create a feature branch from `develop`
2. Make your changes
3. Write/update tests
4. Ensure all tests pass
5. Update documentation if needed
6. Submit a pull request to `develop`
7. Address review feedback

## Code Review

All submissions require code review. We look for:

- Code quality and style
- Test coverage
- Documentation
- Security considerations
- Performance implications

## Commit Messages

Use clear, descriptive commit messages:

```
feat: Add new video generation endpoint
fix: Resolve database connection issue
docs: Update API documentation
test: Add tests for script generation
```

## Questions?

Open an issue or discussion on GitHub if you have questions!
