# 🛠️ Development Guide - Autonomous Agentic AI Film Studio

## 🎯 Project Vision

We're building the **world's first fully autonomous AI film studio** where intelligent agents collaborate to create complete films from simple text prompts. This isn't just automation—it's autonomous creative intelligence.

## 🏗️ Architecture Overview

### System Layers

```
┌─────────────────────────────────────────────────────────┐
│                    User Interface                        │
│                  (Next.js Frontend)                      │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   API Gateway                            │
│                  (FastAPI Backend)                       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│              Agent Orchestration Layer                   │
│         (Director + Multi-Agent Coordinator)             │
└─────────────────────────────────────────────────────────┘
                            ↓
        ┌───────────────────┴───────────────────┐
        ↓                                       ↓
┌──────────────────┐                 ┌──────────────────┐
│  Creative Agents │                 │  Technical Agents │
│  - Director      │                 │  - VFX           │
│  - Screenwriter  │                 │  - Sound         │
│  - Cinematographer│                │  - Editor        │
└──────────────────┘                 └──────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                  AI Services Layer                       │
│     OpenAI • Stability AI • ElevenLabs • Custom Models   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│               Storage & Processing                       │
│           PostgreSQL • Redis • S3/Local Storage          │
└─────────────────────────────────────────────────────────┘
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.11+** with virtual environment
- **Node.js 18+** and npm
- **Docker & Docker Compose** (recommended)
- **Git** for version control
- **PostgreSQL 15+** (or use Docker)
- **Redis 7+** (or use Docker)

### Initial Setup

```bash
# Clone repository
git clone https://github.com/AI-Cloud-Tech-Inc/AI-Film-Studio.git
cd AI-Film-Studio

# Set up environment
cp backend/.env.example backend/.env
cp frontend/.env.local.example frontend/.env.local

# Edit .env files with your API keys
# Required: OPENAI_API_KEY
# Optional: STABILITY_API_KEY, ELEVENLABS_API_KEY
```

### Development with Docker (Recommended)

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build
```

### Manual Development Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (when database is set up)
alembic upgrade head

# Start development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev

# Build for production
npm run build
```

## 🤖 Implementing Agents

### Agent Base Class

All agents inherit from a base class:

```python
# backend/app/agents/base_agent.py
from abc import ABC, abstractmethod
from typing import Dict, Any, List
import openai
from app.core.config import settings

class BaseAgent(ABC):
    """Base class for all autonomous agents"""
    
    def __init__(self, agent_id: str, role: str):
        self.agent_id = agent_id
        self.role = role
        self.llm = self._init_llm()
        self.memory = []  # Agent's decision history
        
    def _init_llm(self):
        """Initialize LLM connection"""
        return openai.OpenAI(api_key=settings.OPENAI_API_KEY)
        
    @abstractmethod
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Main processing method - must be implemented by each agent"""
        pass
        
    async def think(self, context: str, options: List[str] = None) -> str:
        """Use LLM to make decisions"""
        messages = [
            {"role": "system", "content": self._get_system_prompt()},
            {"role": "user", "content": context}
        ]
        
        if options:
            messages.append({
                "role": "user", 
                "content": f"Choose from: {', '.join(options)}"
            })
        
        response = await self.llm.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.8  # Allow creativity
        )
        
        decision = response.choices[0].message.content
        self._log_decision(context, decision)
        return decision
        
    def _log_decision(self, context: str, decision: str):
        """Log all decisions for learning and debugging"""
        self.memory.append({
            "context": context,
            "decision": decision,
            "timestamp": datetime.now()
        })
        
    @abstractmethod
    def _get_system_prompt(self) -> str:
        """Return agent-specific system prompt"""
        pass
        
    def collaborate(self, other_agent: 'BaseAgent', message: str):
        """Send message to another agent"""
        return MessageBus.send(
            sender=self.agent_id,
            recipient=other_agent.agent_id,
            content=message
        )
```

### Example: Director Agent Implementation

```python
# backend/app/agents/director_agent.py
from app.agents.base_agent import BaseAgent
from typing import Dict, Any

class DirectorAgent(BaseAgent):
    """Director Agent - Creative visionary and production overseer"""
    
    def __init__(self):
        super().__init__(agent_id="director-001", role="director")
        
    def _get_system_prompt(self) -> str:
        return """You are an experienced film director with deep understanding of:
        - Cinematic storytelling and visual language
        - Emotional pacing and audience engagement
        - Creative vision and artistic coherence
        - Collaborative filmmaking processes
        
        Your role is to:
        1. Interpret user concepts into clear creative visions
        2. Guide other agents toward cohesive productions
        3. Make high-level creative decisions
        4. Review and provide constructive feedback
        5. Ensure final output meets quality standards
        
        Be creative, decisive, and collaborative."""
        
    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process user concept into creative vision"""
        user_concept = input_data.get("concept", "")
        
        # Analyze the concept
        vision = await self.create_vision(user_concept)
        
        # Coordinate with other agents
        script = await self.commission_script(vision)
        
        # Review and iterate
        final_script = await self.review_script(script)
        
        return {
            "vision": vision,
            "script": final_script,
            "director_notes": self.memory
        }
        
    async def create_vision(self, concept: str) -> Dict[str, Any]:
        """Create creative vision from user concept"""
        prompt = f"""
        User concept: {concept}
        
        As a film director, create a comprehensive creative vision including:
        1. Genre and sub-genre
        2. Tone and mood
        3. Target audience
        4. Key themes
        5. Visual style
        6. Pacing approach
        7. Emotional arc
        
        Provide a detailed creative brief.
        """
        
        vision_text = await self.think(prompt)
        
        # Parse and structure the vision
        return self._parse_vision(vision_text)
        
    async def commission_script(self, vision: Dict) -> str:
        """Work with Screenwriter to create script"""
        # Coordinate with Screenwriter Agent
        screenwriter = ScreenwriterAgent()
        script = await screenwriter.process({
            "vision": vision,
            "director_notes": "Focus on emotional depth"
        })
        return script
        
    async def review_script(self, script: str) -> str:
        """Review script and request revisions if needed"""
        review_prompt = f"""
        Review this script:
        {script}
        
        Evaluate:
        1. Narrative structure
        2. Character development
        3. Dialogue quality
        4. Pacing
        5. Emotional impact
        
        Should we approve or revise? If revise, what specific changes?
        """
        
        review = await self.think(review_prompt, options=["approve", "revise"])
        
        if "revise" in review.lower():
            # Request revision
            return await self._request_revision(script, review)
        
        return script
        
    def _parse_vision(self, vision_text: str) -> Dict[str, Any]:
        """Parse LLM vision into structured data"""
        # Use LLM to extract structured data
        # Implementation details...
        pass
```

## 📁 Project Structure

```
AI-Film-Studio/
├── backend/
│   ├── app/
│   │   ├── agents/              # 🤖 All AI agents
│   │   │   ├── __init__.py
│   │   │   ├── base_agent.py    # Base agent class
│   │   │   ├── director_agent.py
│   │   │   ├── screenwriter_agent.py
│   │   │   ├── cinematographer_agent.py
│   │   │   ├── editor_agent.py
│   │   │   ├── sound_designer_agent.py
│   │   │   └── vfx_agent.py
│   │   ├── api/                 # API routes
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── projects.py
│   │   │       │   ├── scripts.py
│   │   │       │   ├── scenes.py
│   │   │       │   └── videos.py
│   │   │       └── router.py
│   │   ├── core/                # Configuration
│   │   │   ├── config.py
│   │   │   └── message_bus.py   # Agent communication
│   │   ├── services/            # Business logic
│   │   │   ├── ai_services.py
│   │   │   ├── video_service.py
│   │   │   └── storage_service.py
│   │   ├── tasks/               # Background tasks
│   │   │   └── celery.py
│   │   └── models/              # Database models
│   │       ├── project.py
│   │       ├── script.py
│   │       └── scene.py
│   ├── tests/                   # Test suite
│   │   ├── test_agents/
│   │   ├── test_integration/
│   │   └── test_autonomous/
│   ├── main.py                  # FastAPI app
│   └── requirements.txt
│
├── frontend/
│   ├── app/                     # Next.js app directory
│   │   ├── page.tsx            # Home page
│   │   ├── layout.tsx          # Root layout
│   │   ├── projects/           # Projects section
│   │   └── create/             # Film creation wizard
│   ├── components/              # React components
│   │   ├── AgentStatus.tsx     # Show agent activity
│   │   ├── FilmStudio.tsx      # Main studio interface
│   │   └── CreativeVision.tsx  # Vision editor
│   ├── lib/                     # Utilities
│   │   ├── api.ts              # API client
│   │   └── types.ts            # TypeScript types
│   └── package.json
│
├── docs/                        # Documentation
│   ├── ARCHITECTURE.md
│   └── GETTING_STARTED.md
│
├── AGENT_ARCHITECTURE.md        # Agent system design
├── TEST_AUTONOMOUS.md           # Testing guide
├── DEVELOPMENT.md               # This file
└── docker-compose.yml
```

## 🔧 Key Development Tasks

### Task 1: Implement Agent Communication

```python
# backend/app/core/message_bus.py
from typing import Dict, Any
import asyncio
from enum import Enum

class MessageType(Enum):
    REQUEST = "request"
    RESPONSE = "response"
    FEEDBACK = "feedback"
    BROADCAST = "broadcast"

class MessageBus:
    """Handles inter-agent communication"""
    
    def __init__(self):
        self.queues = {}  # agent_id -> queue
        self.history = []
        
    async def send(
        self, 
        sender: str, 
        recipient: str, 
        content: Any,
        message_type: MessageType = MessageType.REQUEST
    ):
        """Send message from one agent to another"""
        message = {
            "sender": sender,
            "recipient": recipient,
            "content": content,
            "type": message_type,
            "timestamp": datetime.now()
        }
        
        # Log message
        self.history.append(message)
        
        # Deliver to recipient
        if recipient in self.queues:
            await self.queues[recipient].put(message)
            
    async def broadcast(self, sender: str, content: Any):
        """Broadcast message to all agents"""
        for agent_id, queue in self.queues.items():
            if agent_id != sender:
                await queue.put({
                    "sender": sender,
                    "content": content,
                    "type": MessageType.BROADCAST
                })
```

### Task 2: Create Orchestrator

```python
# backend/app/orchestrator.py
from app.agents import *

class FilmOrchestrator:
    """Orchestrates all agents to create a complete film"""
    
    def __init__(self):
        self.director = DirectorAgent()
        self.screenwriter = ScreenwriterAgent()
        self.cinematographer = CinematographerAgent()
        self.editor = EditorAgent()
        self.sound_designer = SoundDesignerAgent()
        self.vfx = VFXAgent()
        
    async def create_film(self, user_concept: str) -> Dict[str, Any]:
        """Autonomous film creation pipeline"""
        
        # Stage 1: Creative Vision
        vision = await self.director.create_vision(user_concept)
        
        # Stage 2: Script Development
        script = await self.screenwriter.write_script(vision)
        approved_script = await self.director.review_script(script)
        
        # Stage 3: Shot Planning
        shot_list = await self.cinematographer.plan_shots(approved_script)
        
        # Stage 4: Scene Generation
        scenes = await self._generate_scenes(shot_list)
        
        # Stage 5: Post-Production
        edited = await self.editor.assemble(scenes)
        with_audio = await self.sound_designer.add_audio(edited)
        final = await self.vfx.enhance(with_audio)
        
        # Stage 6: Final Review
        approved = await self.director.final_review(final)
        
        return {
            "film": approved,
            "metadata": self._collect_metadata()
        }
```

### Task 3: Frontend Agent Visualization

```typescript
// frontend/components/AgentStatus.tsx
import { useEffect, useState } from 'react';

interface AgentActivity {
  agentId: string;
  role: string;
  status: 'idle' | 'thinking' | 'working' | 'collaborating';
  currentTask: string;
  progress: number;
}

export function AgentStatus() {
  const [agents, setAgents] = useState<AgentActivity[]>([]);
  
  useEffect(() => {
    // Subscribe to agent activity updates
    const ws = new WebSocket('ws://localhost:8000/ws/agents');
    
    ws.onmessage = (event) => {
      const activity = JSON.parse(event.data);
      setAgents(prev => updateAgentActivity(prev, activity));
    };
    
    return () => ws.close();
  }, []);
  
  return (
    <div className="agent-dashboard">
      <h2>🤖 AI Agents at Work</h2>
      {agents.map(agent => (
        <AgentCard key={agent.agentId} agent={agent} />
      ))}
    </div>
  );
}
```

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Test specific agent
pytest tests/test_agents/test_director.py

# Test with coverage
pytest --cov=app tests/

# Test autonomous behavior
pytest tests/test_autonomous/ -v
```

## 📊 Monitoring & Debugging

### Logging

```python
# Configure structured logging
import logging
from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Log agent decisions
logger.info("Agent decision", extra={
    "agent": "director",
    "decision": "approve_script",
    "reasoning": "Strong narrative arc",
    "confidence": 0.87
})
```

### Metrics

Track key metrics:
- Agent decision quality
- Collaboration efficiency
- Film generation time
- User satisfaction scores
- Resource utilization

## 🚢 Deployment

```bash
# Build for production
docker-compose -f docker-compose.prod.yml build

# Deploy to cloud
./deploy.sh production

# Monitor logs
kubectl logs -f deployment/ai-film-studio
```

## 🤝 Contributing

1. Create feature branch: `git checkout -b feature/agent-improvements`
2. Implement changes
3. Add tests
4. Update documentation
5. Submit PR

## 📚 Resources

- [Agent Architecture](./AGENT_ARCHITECTURE.md)
- [Testing Guide](./TEST_AUTONOMOUS.md)
- [API Documentation](http://localhost:8000/docs)

---

**Let's build the future of autonomous creative AI!** 🎬🤖
