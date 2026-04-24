"""
Voiceovers Endpoint - AI voice generation
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai_services import elevenlabs_service

router = APIRouter()


class VoiceoverRequest(BaseModel):
    """Voiceover generation request"""
    script_id: str
    text: str
    voice: str = "male"  # male, female, or specific voice ID
    language: str = "en"


class VoiceoverResponse(BaseModel):
    """Voiceover response"""
    id: str
    audio_url: str
    duration: float
    status: str


# In-memory storage
voiceovers_db = {}


@router.post("/generate", response_model=VoiceoverResponse)
async def generate_voiceover(request: VoiceoverRequest):
    """Generate voiceover using AI"""
    try:
        # Generate audio using ElevenLabs
        audio_path = await elevenlabs_service.generate_voiceover(
            text=request.text,
            voice=request.voice,
            language=request.language
        )
        
        voiceover_id = f"voice_{hash(request.text)}"
        
        voiceover_data = {
            "id": voiceover_id,
            "audio_url": f"/{audio_path}",
            "duration": len(request.text.split()) * 0.5,  # Rough estimate
            "status": "completed"
        }
        
        voiceovers_db[voiceover_id] = voiceover_data
        
        return voiceover_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{voiceover_id}", response_model=VoiceoverResponse)
async def get_voiceover(voiceover_id: str):
    """Get voiceover by ID"""
    if voiceover_id in voiceovers_db:
        return voiceovers_db[voiceover_id]
    
    raise HTTPException(status_code=404, detail="Voiceover not found")


@router.get("/voices/list")
async def list_voices():
    """Get available voices"""
    try:
        voices = await elevenlabs_service.get_available_voices()
        return {"voices": voices}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
