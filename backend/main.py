"""FastAPI backend for Spiritual AI Companion with Bhakti Features."""
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import uvicorn

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

app = FastAPI(
    title="Spiritual AI Companion API",
    description="A compassionate AI companion for spiritual guidance, bhakti, and mindfulness",
    version="2.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://127.0.0.1:3000", "http://127.0.0.1:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# SPIRITUAL CONTENT DATABASE - Public Domain / Traditional
# ============================================================================

BHakti_CONTENT = {
    "gayatri_mantra": {
        "name": "Gayatri Mantra",
        "soundscape": "ॐ भूर्भुवः स्वः। तत्सवितुर्वरेण्यं। भर्गो देवस्य धीमहि। धियो यो नः प्रचोदयात्॥",
        "telugu": "ఓం భూర్భువః స్వః। తత్సవితుర్వరేణ్యం। భర్గో దేవస్య ధీమహి। ధియో యో నః ప్రచోదయాత్॥",
        "english": "We meditate on the glory of the divine light, who has produced the universe, who is worthy of worship, who removes all sins.",
        "meaning": "The Gayatri is the mother of all mantras, invoking the divine wisdom within each seeker.",
        "deity": "Savitr (Sun God)",
        "benefits": ["Knowledge", "Wisdom", "Spiritual illumination", "Mental clarity"],
        "audio_url": "/audio/gayatri.mp3"
    },
    "om_namah_shivaya": {
        "name": "Om Namah Shivaya",
        "soundscape": "ॐ नमः शिवाय",
        "telugu": "ఓం నమః శివాయ",
        "english": "I bow to Shiva, the auspicious one",
        "meaning": "The five-syllable mantra (Panchakshara) is the most sacred mantra of Shaivism, representing the five elements.",
        "deity": "Shiva",
        "benefits": ["Inner peace", "Transformation", "Removal of obstacles", "Spiritual growth"],
        "audio_url": "/audio/om-namah-shivaya.mp3"
    },
    "hanuman_chalisa": {
        "name": "Hanuman Chalisa",
        "soundscape": "శ్రీ గురు చరణ కరుణా మృతం, జయ హనుమాన్",
        "telugu": "శ్రీగురు చరణ కరుణామృతం, జయ హనుమాన్!",
        "english": "Victory to Hanuman, the devoted servant of Rama",
        "meaning": "40 verses praising Hanuman's strength, devotion, and virtues.",
        "deity": "Hanuman",
        "benefits": ["Courage", "Protection", "Strength", "Devotion"],
        "audio_url": "/audio/hanuman-chalisa.mp3"
    },
    "vishnu_sahasranamam": {
        "name": "Vishnu Sahasranamam",
        "soundscape": "విష్ణువు పరమేశ్వరుడు",
        "telugu": "విష్ణువు పరమేశ్వరుడు, నారాయణుడు, వాసుదేవుడు",
        "english": "The thousand names of Lord Vishnu",
        "meaning": "Reveals the divine qualities and names of the Supreme Being.",
        "deity": "Vishnu",
        "benefits": ["Divine blessings", "Protection", "Prosperity", "Moksha"],
        "audio_url": "/audio/vishnu-sahasranamam.mp3"
    },
    "lalitha_sahasranamam": {
        "name": "Lalitha Sahasranamam",
        "soundscape": "శ్రీమతీ భగవతీ లలిత",
        "telugu": "శ్రీమతి, భగవతి, లలిత, కామేశ్వరి",
        "english": "The thousand names of Goddess Lalitha",
        "meaning": "Describes the divine feminine energy and qualities of the mother goddess.",
        "deity": "Lakshmi/Parvati",
        "benefits": ["Wealth", "Prosperity", "Wisdom", "Feminine power"],
        "audio_url": "/audio/lalitha-sahasranamam.mp3"
    },
    "aditya_hrudayam": {
        "name": "Aditya Hrudayam",
        "soundscape": "ఆదిత్య హృదయమ్",
        "telugu": "సూర్యదేవుని హృదయం, కాంతి మరియు శక్తి",
        "english": "Heart of the Sun God",
        "meaning": "A powerful hymn revealing the glory of Surya, the source of all life and energy.",
        "deity": "Surya (Sun)",
        "benefits": ["Energy", "Vitality", "Success", "Removal of enemies"],
        "audio_url": "/audio/aditya-hrudayam.mp3"
    }
}

MORNING_ROUTINE = {
    "gayatri": BHakti_CONTENT["gayatri_mantra"],
    "surya": {
        "name": "Surya Namaskar",
        "meaning": "Salutations to the Sun God, source of life and energy",
        "duration": "10 minutes",
        "benefits": ["Physical energy", "Mental clarity", "Gratitude"]
    },
    "prayer": {
        "name": "Morning Prayer",
        "soundscape": "ఓం సరస్వతి నమస్తుభ్యం వరదే కామరూపిణీ",
        "english": "Salutations to Goddess Saraswati, remover of obstacles"
    }
}

EVENING_ROUTINE = {
    "bhajan": {
        "name": "Bhajan Singing",
        "meaning": "Devotional singing to connect with the divine",
        "duration": "15 minutes"
    },
    "meditation": {
        "name": "Meditation",
        "meaning": "Silent contemplation for inner peace",
        "duration": "10 minutes"
    },
    "gratitude": {
        "name": "Gratitude Journaling",
        "meaning": "Reflecting on blessings received",
        "duration": "5 minutes"
    }
}

# ============================================================================
# INTENT DETECTION
# ============================================================================

def detect_intent(message: str) -> Dict[str, Any]:
    """Detect spiritual intent from user message."""
    msg_lower = message.lower()
    
    # Bhakti/Song intents
    if any(word in msg_lower for word in ['bhajan', 'devotional song', 'spiritual song', 'kirtan']):
        return {"intent": "PLAY_BHAKTI_SONG", "deity": detect_deity(msg_lower)}
    
    # Mantra intents
    if any(word in msg_lower for word in ['mantra', 'chant', 'recite', 'chanting']):
        return {"intent": "CHANT_MANRA", "mantra": detect_mantra(msg_lower)}
    
    # Gayatri specific
    if 'gayatri' in msg_lower:
        return {"intent": "PLAY_GAYATRI", "content": BHakti_CONTENT["gayatri_mantra"]}
    
    # Shiva specific
    if any(word in msg_lower for word in ['shiva', 'shivaya', 'rudra']):
        return {"intent": "PLAY_SHIVA", "content": BHakti_CONTENT["om_namah_shivaya"]}
    
    # Hanuman specific
    if any(word in msg_lower for word in ['hanuman', 'anjaneya', 'maruti']):
        return {"intent": "PLAY_HANUMAN", "content": BHakti_CONTENT["hanuman_chalisa"]}
    
    # Vishnu specific
    if any(word in msg_lower for word in ['vishnu', 'narayana', 'krishna', 'rama']):
        return {"intent": "PLAY_VISHNU", "deity": "Vishnu"}
    
    # Meaning/Explanation intents
    if any(word in msg_lower for word in ['meaning', 'explain', 'what is', 'understand']):
        return {"intent": "EXPLAIN_MANTRAM", "item": detect_mantra(msg_lower)}
    
    # Morning prayer
    if any(word in msg_lower for word in ['morning', 'sunrise', 'prayer']):
        return {"intent": "MORNING_PRAYER", "routine": MORNING_ROUTINE}
    
    # Evening practice
    if any(word in msg_lower for word in ['evening', 'night', 'bedtime']):
        return {"intent": "EVENING_PRACTICE", "routine": EVENING_ROUTINE}
    
    # Meditation
    if any(word in msg_lower for word in ['meditate', 'meditation', 'dhyana']):
        return {"intent": "MEDITATION", "type": "general"}
    
    return {"intent": "GENERAL_CHAT", "message": message}

def detect_deity(msg: str) -> str:
    """Detect deity name from message."""
    if 'krishna' in msg: return "Krishna"
    if 'rama' in msg: return "Rama"
    if 'hanuman' in msg: return "Hanuman"
    if 'shiva' in msg: return "Shiva"
    if 'vishnu' in msg: return "Vishnu"
    if 'lakshmi' in msg: return "Lakshmi"
    if 'saraswati' in msg: return "Saraswati"
    return "General"

def detect_mantra(msg: str) -> str:
    """Detect specific mantra from message."""
    if 'gayatri' in msg: return "gayatri_mantra"
    if 'namah shivaya' in msg: return "om_namah_shivaya"
    if 'hanuman' in msg: return "hanuman_chalisa"
    if 'vishnu' in msg: return "vishnu_sahasranamam"
    return "general"

# ============================================================================
# SPIRITUAL AGENT RESPONSE GENERATOR
# ============================================================================

def generate_bhakti_response(intent_data: Dict) -> Dict[str, Any]:
    """Generate response for bhakti-related intents."""
    intent = intent_data.get("intent")
    
    responses = {
        "PLAY_BHAKTI_SONG": {
            "response": "🙏 Let us together sing praises to the divine. Playing a devotional song to fill your heart with bhakti (devotion).",
            "audio_type": "bhajan",
            "deity": intent_data.get("deity", "General"),
            "flow": ["intro", "audio", "meaning", "close"]
        },
        "CHANT_MANRA": {
            "response": "🕉️ Let us chant this sacred mantra together. Feel the vibration in your heart as we invoke the divine presence.",
            "audio_type": "mantra",
            "mantra": intent_data.get("mantra", "general"),
            "flow": ["intro", "chant", "pause", "meaning", "close"]
        },
        "PLAY_GAYATRI": {
            "response": "📿 The Gayatri Mantra is the mother of all mantras. Let us meditate on the divine light within. ॐ भूर्भुवः स्वः...",
            "audio_type": "gayatri",
            "content": BHakti_CONTENT["gayatri_mantra"],
            "flow": ["intro", "sanskrit", "telugu", "english", "meaning", "close"]
        },
        "PLAY_SHIVA": {
            "response": "🕉️ Om Namah Shivaya - I bow to the auspicious one. This mantra removes all obstacles and transforms consciousness.",
            "audio_type": "shiva",
            "content": BHakti_CONTENT["om_namah_shivaya"],
            "flow": ["intro", "chant", "meaning", "close"]
        },
        "PLAY_HANUMAN": {
            "response": "🐒 Jai Hanuman! Let us invoke the strength and devotion of Lord Hanuman, the supreme servant of Rama.",
            "audio_type": "hanuman",
            "content": BHakti_CONTENT["hanuman_chalisa"],
            "flow": ["intro", "verse", "meaning", "close"]
        },
        "MEDITATION": {
            "response": "🧘 Let us sit comfortably and turn our attention inward. Close your eyes and follow your breath...",
            "audio_type": "meditation",
            "duration": "10 minutes",
            "flow": ["intro", "guidance", "silence", "close"]
        },
        "MORNING_PRAYER": {
            "response": "🌅 Good morning, dear seeker. Let us begin the day with gratitude and divine connection.",
            "audio_type": "routine",
            "routine": MORNING_ROUTINE,
            "flow": ["intro", "gayatri", "surya", "blessing"]
        },
        "EVENING_PRACTICE": {
            "response": "🌙 As the day ends, let us reflect on the blessings received and prepare for peaceful rest.",
            "audio_type": "routine",
            "routine": EVENING_ROUTINE,
            "flow": ["intro", "bhajan", "gratitude", "blessing"]
        }
    }
    
    return responses.get(intent, {"response": "🙏 May peace be with you. How else may I assist you on your spiritual journey?"})

# ============================================================================
# REQUEST/RESPONSE MODELS
# ============================================================================

class ChatRequest(BaseModel):
    message: str
    context: Optional[Dict[str, Any]] = {}

class ChatResponse(BaseModel):
    response: str
    context: Dict[str, Any]
    audio_type: Optional[str] = None
    audio_content: Optional[Dict] = None

class BhaktiRequest(BaseModel):
    intent: str
    deity: Optional[str] = None
    mantra: Optional[str] = None

class BhaktiResponse(BaseModel):
    response: str
    audio_url: Optional[str] = None
    sanskrit: Optional[str] = None
    telugu: Optional[str] = None
    english_meaning: Optional[str] = None
    benefits: Optional[List[str]] = None

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "name": "Spiritual AI Companion API v2.0",
        "version": "2.0.0",
        "status": "running",
        "features": ["Bhakti", "Mantras", "Meditation", "Daily Routines"]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "spiritual-ai"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Chat endpoint for spiritual guidance."""
    try:
        # Detect intent
        intent_data = detect_intent(request.message)
        
        # Generate response based on intent
        response_data = generate_bhakti_response(intent_data)
        
        context = {
            "intent": intent_data.get("intent"),
            "deity": intent_data.get("deity"),
            "audio_type": response_data.get("audio_type")
        }
        
        return ChatResponse(
            response=response_data["response"],
            context=context,
            audio_type=response_data.get("audio_type"),
            audio_content=response_data.get("content") if response_data.get("audio_type") in ["gayatri", "shiva", "hanuman"] else None
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/bhakti", response_model=BhaktiResponse)
async def bhakti_content(request: BhaktiRequest):
    """Get bhakti content based on intent."""
    try:
        if request.intent == "gayatri":
            content = BHakti_CONTENT["gayatri_mantra"]
        elif request.intent == "shiva":
            content = BHakti_CONTENT["om_namah_shivaya"]
        elif request.intent == "hanuman":
            content = BHakti_CONTENT["hanuman_chalisa"]
        elif request.intent == "vishnu":
            content = BHakti_CONTENT["vishnu_sahasranamam"]
        else:
            content = BHakti_CONTENT["gayatri_mantra"]
        
        return BhaktiResponse(
            response=f"🙏 {content['name']} - {content['english']}",
            audio_url=content["audio_url"],
            sanskrit=content["soundscape"],
            telugu=content["telugu"],
            english_meaning=content["meaning"],
            benefits=content["benefits"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/mantra/{mantra_id}")
async def get_mantra(mantra_id: str):
    """Get specific mantra content."""
    try:
        if mantra_id in BHakti_CONTENT:
            content = BHakti_CONTENT[mantra_id]
            return {
                "name": content["name"],
                "soundscape": content["soundscape"],
                "telugu": content["telugu"],
                "english": content["english"],
                "meaning": content["meaning"],
                "benefits": content["benefits"],
                "audio_url": content["audio_url"]
            }
        else:
            return {"error": "Mantra not found"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/routine/{time_of_day}")
async def get_routine(time_of_day: str):
    """Get morning or evening spiritual routine."""
    try:
        if time_of_day == "morning":
            return {
                "routine": "Morning Spiritual Practice",
                "items": MORNING_ROUTINE,
                "message": "🌅 Begin your day with divine connection"
            }
        elif time_of_day == "evening":
            return {
                "routine": "Evening Spiritual Practice",
                "items": EVENING_ROUTINE,
                "message": "🌙 End your day with gratitude and peace"
            }
        else:
            return {"error": "Invalid time of day. Use 'morning' or 'evening'"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/meditation")
async def get_meditation():
    """Get meditation guidance."""
    return {
        "meditation": {
            "type": "Guided Meditation",
            "steps": [
                "Find a comfortable seated position",
                "Close your eyes gently",
                "Follow your breath without force",
                "Observe thoughts without attachment",
                "Return to the present moment",
                "Feel peace within"
            ],
            "duration": "10-20 minutes"
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
