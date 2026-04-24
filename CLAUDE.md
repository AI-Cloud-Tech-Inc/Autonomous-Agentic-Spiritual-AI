# AI-Spiritual-Agent-1

> An autonomous AI spiritual assistant providing personalized meditation guidance, emotional support, and spiritual companionship through empathetic, non-controversial teachings.

## 🎯 Project Overview

AI-Spiritual-Agent-1 is an intelligent agent combining memory systems, autonomous reasoning, and spiritual content delivery to support users on their spiritual journey.

---

## 📁 Complete File Tree

```
ai-spiritual-agent-1/
│
├── README.md                          # Main project documentation
├── CLAUDE.md                          # This file - complete developer guide
├── LICENSE                            # MIT License
├── CONTRIBUTING.md                    # Contribution guidelines
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
├── .env.example                      # Environment variables template
├── setup.py                          # Package installation config
│
├── config/                           # Configuration files
│   ├── config.yaml                   # Main configuration (gitignored)
│   ├── config.example.yaml          # Configuration template
│   └── logging.yaml                 # Logging configuration
│
├── src/                             # Source code
│   ├── __init__.py
│   ├── main.py                      # Main entry point
│   │
│   ├── core/                        # Core agent logic
│   │   ├── __init__.py
│   │   ├── agent.py                 # SpiritualAgent main class
│   │   └── constants.py             # Application constants
│   │
│   ├── memory/                      # Memory management
│   │   ├── __init__.py
│   │   ├── memory_manager.py        # Memory systems (short/long/episodic)
│   │   ├── storage.py               # Data persistence layer
│   │   └── models.py                # Memory data models
│   │
│   ├── dialogue/                    # Conversation handling
│   │   ├── __init__.py
│   │   ├── conversation_handler.py  # Response generation
│   │   ├── templates.py             # Content templates
│   │   └── content_loader.py        # Load spiritual content
│   │
│   ├── reasoning/                   # Context analysis
│   │   ├── __init__.py
│   │   ├── context_analyzer.py      # Intent & emotion detection
│   │   ├── intent_classifier.py     # Intent classification
│   │   └── emotion_detector.py      # Emotion detection
│   │
│   ├── api/                         # External integrations
│   │   ├── __init__.py
│   │   ├── anthropic_client.py      # Anthropic API integration
│   │   └── webhooks.py              # Webhook handlers
│   │
│   └── utils/                       # Utility functions
│       ├── __init__.py
│       ├── logger.py                # Logging utilities
│       ├── validators.py            # Input validation
│       └── helpers.py               # Helper functions
│
├── data/                            # Data files
│   ├── prompts/                     # Meditation prompts
│   │   ├── meditation_prompts.md    # Daily meditation library
│   │   ├── gratitude.json          # Gratitude practices
│   │   ├── peace.json              # Peace meditations
│   │   └── compassion.json         # Compassion practices
│   │
│   ├── teachings/                   # Spiritual wisdom
│   │   ├── quotes.json             # Wisdom quotes database
│   │   └── themes.json             # Spiritual themes
│   │
│   └── user_data/                   # User-specific data (gitignored)
│       └── README.md
│
├── docs/                            # Documentation
│   ├── QUICKSTART.md               # Quick start guide
│   ├── architecture.md             # System architecture
│   ├── content_guidelines.md       # Spiritual content standards
│   ├── api_reference.md            # API documentation
│   ├── deployment.md               # Deployment guide
│   └── contributing_guide.md       # Detailed contribution guide
│
├── tests/                           # Test suite
│   ├── __init__.py
│   ├── conftest.py                 # Pytest configuration
│   ├── test_agent.py               # Agent tests
│   ├── test_memory.py              # Memory tests
│   ├── test_dialogue.py            # Dialogue tests
│   ├── test_reasoning.py           # Reasoning tests
│   └── integration/                # Integration tests
│       ├── __init__.py
│       └── test_full_flow.py
│
├── scripts/                         # Utility scripts
│   ├── setup_dev.sh                # Development setup
│   ├── run_tests.sh                # Test runner
│   ├── deploy.sh                   # Deployment script
│   └── migrate_data.py             # Data migration
│
├── docker/                          # Docker configuration
│   ├── Dockerfile                  # Main Dockerfile
│   ├── docker-compose.yml          # Docker Compose config
│   └── .dockerignore              # Docker ignore rules
│
└── logs/                            # Log files (gitignored)
    └── .gitkeep

```

---

## 🚀 Quick Start Commands

### Installation & Setup
```bash
# Clone repository
git clone https://github.com/yourusername/ai-spiritual-agent-1.git
cd ai-spiritual-agent-1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup configuration
cp config/config.example.yaml config/config.yaml
cp .env.example .env

# Create required directories
mkdir -p data/user_data logs
```

### Running the Agent
```bash
# Run in development mode
python src/main.py

# Run with custom config
python src/main.py --config config/custom.yaml

# Run with logging level
python src/main.py --log-level DEBUG

# Interactive mode
python -i src/main.py
```

### Testing
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_agent.py -v

# Run integration tests only
pytest tests/integration/ -v

# Watch mode (requires pytest-watch)
ptw tests/
```

### Development Tools
```bash
# Format code
black src/ tests/

# Lint code
flake8 src/ tests/

# Type checking
mypy src/

# Sort imports
isort src/ tests/

# Run all quality checks
./scripts/run_tests.sh
```

### Docker
```bash
# Build image
docker build -t ai-spiritual-agent:latest .

# Run container
docker run -it ai-spiritual-agent:latest

# Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f
```

---

## 🏗️ Architecture Overview

### System Components

#### 1. **Agent Core** (`src/core/agent.py`)
- Orchestrates all subsystems
- Manages session state
- Routes requests to handlers
- Coordinates responses

**Key Methods:**
```python
agent.interact(message: str) -> str
agent.get_daily_meditation() -> str
agent.get_insights() -> Dict[str, Any]
agent.farewell() -> str
```

#### 2. **Memory System** (`src/memory/`)
- **Short-term**: Recent conversation (last 20 interactions)
- **Long-term**: User profile, preferences, journey stage
- **Episodic**: Significant past interactions (last 50)

**Memory Architecture:**
```
MemoryManager
├── ShortTermMemory (deque, maxlen=20)
├── LongTermMemory (dict, persisted)
└── EpisodicMemory (list, last 50 items)
```

#### 3. **Dialogue Handler** (`src/dialogue/`)
- Generates responses based on context
- Manages meditation prompts
- Shares spiritual wisdom
- Provides emotional support

**Content Types:**
- Meditation guidance
- Wisdom quotes
- Emotional support
- General conversation

#### 4. **Context Analyzer** (`src/reasoning/`)
- Intent classification
- Emotion detection
- Crisis indicators
- Theme extraction

**Analysis Flow:**
```
User Input → Intent Detection → Emotion Analysis → Crisis Check → Context Generation
```

### Data Flow

```
┌─────────────┐
│ User Input  │
└──────┬──────┘
       │
       ▼
┌─────────────────┐
│ Context Analyzer│
└──────┬──────────┘
       │ (context)
       ▼
┌─────────────────┐      ┌──────────────┐
│ Memory Manager  │◄────►│ Load History │
└──────┬──────────┘      └──────────────┘
       │
       ▼
┌─────────────────┐
│   Agent Core    │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐
│Dialogue Handler │
└──────┬──────────┘
       │
       ▼
┌─────────────────┐      ┌──────────────┐
│ Memory Manager  │─────►│ Store Update │
└──────┬──────────┘      └──────────────┘
       │
       ▼
┌─────────────────┐
│ Agent Response  │
└─────────────────┘
```

---

## 🛠️ Developer Command Reference

### Project Management

| Command | Description |
|---------|-------------|
| `pip install -r requirements.txt` | Install dependencies |
| `pip install -e .` | Install package in editable mode |
| `pip freeze > requirements.txt` | Update requirements |

### Code Quality

| Command | Description |
|---------|-------------|
| `black src/` | Format code |
| `flake8 src/` | Lint code |
| `mypy src/` | Type checking |
| `isort src/` | Sort imports |
| `pylint src/` | Advanced linting |

### Testing

| Command | Description |
|---------|-------------|
| `pytest` | Run all tests |
| `pytest -v` | Verbose test output |
| `pytest -k "test_agent"` | Run specific tests |
| `pytest --cov` | Test with coverage |
| `pytest --pdb` | Debug on failure |
| `pytest -x` | Stop on first failure |
| `pytest -n auto` | Parallel testing |

### Git Workflow

| Command | Description |
|---------|-------------|
| `git checkout -b feature/name` | Create feature branch |
| `git add .` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git push origin branch` | Push to remote |
| `git pull --rebase` | Update with rebase |

### Database (Future)

| Command | Description |
|---------|-------------|
| `python scripts/migrate_data.py` | Run migrations |
| `python scripts/seed_data.py` | Seed database |
| `python scripts/backup_data.py` | Backup user data |

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file from `.env.example`:

```bash
# Application
APP_NAME=ai-spiritual-agent-1
APP_ENV=development  # development, staging, production
DEBUG=true

# Logging
LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
LOG_FILE=logs/agent.log

# Memory
MEMORY_MAX_SHORT_TERM=20
MEMORY_MAX_EPISODIC=50
MEMORY_SAVE_FREQUENCY=10

# API Keys (Optional)
ANTHROPIC_API_KEY=your_api_key_here

# Database (Future)
# DATABASE_URL=postgresql://user:pass@localhost/dbname

# Security
SECRET_KEY=your-secret-key-here
SESSION_TIMEOUT=3600
```

### Config File (`config/config.yaml`)

```yaml
# Memory settings
memory:
  max_short_term_items: 20
  episodic_memory_limit: 50
  save_frequency: 10

# Dialogue settings
dialogue:
  tone: empathetic
  response_length: balanced
  use_emojis: true
  spiritual_traditions:
    - universal
    - mindfulness
    - contemplative

# Reasoning settings
reasoning:
  emotion_detection: enabled
  crisis_detection: enabled
  intent_classification: enabled
  theme_extraction: enabled

# Agent settings
agent:
  greeting_style: warm
  farewell_style: peaceful
  check_in_frequency: 5

# Safety settings
safety:
  crisis_disclaimer: true
  professional_referral: true
  content_boundaries:
    - no_medical_advice
    - no_religious_proselytizing
    - respect_all_traditions

# Features
features:
  daily_meditation: true
  journey_tracking: true
  progress_insights: true
  personalization: true

# Logging
logging:
  level: INFO
  file: logs/agent.log
  console: true
```

---

## 🧪 Testing Strategy

### Test Coverage

- **Unit Tests**: Individual components (memory, dialogue, reasoning)
- **Integration Tests**: Full conversation flows
- **End-to-End Tests**: Complete user journeys

### Test Structure

```python
# tests/test_agent.py
class TestSpiritualAgent:
    def test_initialization(self)
    def test_basic_interaction(self)
    def test_meditation_request(self)
    def test_emotional_support(self)
    def test_memory_persistence(self)
```

### Running Specific Tests

```bash
# Test specific module
pytest tests/test_memory.py

# Test specific class
pytest tests/test_agent.py::TestSpiritualAgent

# Test specific method
pytest tests/test_agent.py::TestSpiritualAgent::test_meditation_request

# With markers
pytest -m "slow"  # Only slow tests
pytest -m "not slow"  # Skip slow tests
```

---

## 📦 Dependencies

### Core Dependencies
- **Python**: 3.9+
- **PyYAML**: Configuration management
- **python-dateutil**: Date/time utilities

### Optional Dependencies
- **NLTK/spaCy**: Advanced NLP
- **SQLAlchemy**: Database ORM
- **Redis**: Caching layer
- **FastAPI**: Web API framework

### Development Dependencies
- **pytest**: Testing framework
- **black**: Code formatter
- **flake8**: Linter
- **mypy**: Type checker
- **pytest-cov**: Coverage reporting

---

## 🔐 Security & Privacy

### Data Protection
- User data encrypted at rest
- Memory files in `.gitignore`
- No logging of sensitive information
- Session timeouts implemented

### Crisis Detection
- Keyword-based detection
- Automatic resource provision
- Professional referral prompts
- No attempt to "fix" crises

### Content Safety
- Universal spiritual principles only
- No medical/psychological diagnoses
- Age-appropriate content
- Cultural sensitivity checks

---

## 🚢 Deployment

### Production Checklist

- [ ] Set `APP_ENV=production`
- [ ] Configure proper logging
- [ ] Set up data backups
- [ ] Enable SSL/TLS
- [ ] Configure firewalls
- [ ] Set up monitoring
- [ ] Review security settings
- [ ] Test crisis workflows

### Docker Deployment

```bash
# Build
docker build -t ai-spiritual-agent:v1.0 .

# Run
docker run -d \
  --name spiritual-agent \
  -v ./data:/app/data \
  -v ./logs:/app/logs \
  -e APP_ENV=production \
  ai-spiritual-agent:v1.0
```

### Docker Compose

```yaml
version: '3.8'
services:
  agent:
    build: .
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    environment:
      - APP_ENV=production
    restart: unless-stopped
```

---

## 🤝 Contributing

### Development Workflow

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes
4. Run tests: `pytest tests/`
5. Format code: `black src/`
6. Commit: `git commit -m 'Add amazing feature'`
7. Push: `git push origin feature/amazing-feature`
8. Create Pull Request

### Code Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions focused
- Maximum line length: 88 (Black default)

### Commit Conventions

```
feat: Add new meditation type
fix: Resolve memory persistence issue
docs: Update architecture guide
test: Add integration tests
refactor: Simplify context analyzer
style: Format with Black
chore: Update dependencies
```

---

## 📚 Documentation

### Available Docs

| Document | Purpose |
|----------|---------|
| `README.md` | Project overview |
| `CLAUDE.md` | Complete developer guide (this file) |
| `docs/QUICKSTART.md` | Getting started |
| `docs/architecture.md` | System design |
| `docs/content_guidelines.md` | Spiritual content standards |
| `docs/api_reference.md` | API documentation |
| `CONTRIBUTING.md` | Contribution guidelines |

### Generating API Docs

```bash
# Install sphinx
pip install sphinx sphinx-rtd-theme

# Generate docs
cd docs
sphinx-quickstart
make html
```

---

## 🗺️ Roadmap

### v1.0 (Current)
- [x] Core agent architecture
- [x] Memory systems
- [x] Basic dialogue
- [x] Context analysis
- [x] Test suite

### v1.1
- [ ] Web interface (Flask/FastAPI)
- [ ] Database integration (PostgreSQL)
- [ ] Advanced NLP (transformers)
- [ ] Voice interaction (TTS/STT)

### v2.0
- [ ] Mobile app (React Native)
- [ ] Multi-language support
- [ ] Community features
- [ ] Analytics dashboard
- [ ] API for third-party integrations

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError
```bash
# Solution
source venv/bin/activate
pip install -r requirements.txt
```

**Issue**: Config file not found
```bash
# Solution
cp config/config.example.yaml config/config.yaml
```

**Issue**: Memory not persisting
```bash
# Solution
mkdir -p data/user_data
chmod 755 data/user_data
```

**Issue**: Tests failing
```bash
# Solution
pytest tests/ -v --tb=short
# Check error output and fix issues
```

---

## 📞 Support & Contact

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: your-email@example.com
- **Documentation**: https://docs.yourproject.com

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

Built with respect for spiritual traditions worldwide and commitment to ethical AI development.

---

**Last Updated**: 2024
**Version**: 1.0.0
**Status**: Active Development
