"""FastAPI backend for Spiritual AI Companion."""
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import uvicorn

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.agent import SpiritualAgent
from src.core.constants import GREETING

app = FastAPI(
    title="Spiritual AI Companion API",
    description="A compassionate AI companion for spiritual guidance and mindfulness",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global agent instance
agent: Optional[SpiritualAgent] = None

def get_agent():
    """Get or create the spiritual agent."""
    global agent
    if agent is None:
        agent = SpiritualAgent()
    return agent

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    context: Optional[Dict[str, Any]] = {}

class ChatResponse(BaseModel):
    response: str
    context: Dict[str, Any]

class MeditationResponse(BaseModel):
    meditation: str

class InsightsResponse(BaseModel):
    insights: Dict[str, Any]

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Spiritual AI Companion API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "spiritual-ai"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint for interacting with the spiritual agent."""
    try:
        agent_instance = get_agent()
        
        # Process the message
        response = agent_instance.interact(request.message)
        
        # Get context for the response
        context = agent_instance.context_analyzer.analyze(request.message)
        
        return ChatResponse(
            response=response,
            context=context
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/meditation", response_model=MeditationResponse)
async def get_meditation():
    """Get a daily meditation."""
    try:
        agent_instance = get_agent()
        meditation = agent_instance.get_daily_meditation()
        return MeditationResponse(meditation=meditation)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/insights", response_model=InsightsResponse)
async def get_insights():
    """Get user insights based on conversation history."""
    try:
        agent_instance = get_agent()
        insights = agent_instance.get_insights()
        return InsightsResponse(insights=insights)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/check-in")
async def check_in():
    """Perform a wellness check-in."""
    try:
        agent_instance = get_agent()
        response = agent_instance.check_in()
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/farewell")
async def farewell():
    """Generate farewell message."""
    try:
        agent_instance = get_agent()
        response = agent_instance.farewell()
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
