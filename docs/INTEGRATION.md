# AI Film Studio - Integration Guide

## 🎬 Complete AI Film Production System

AI Film Studio integrates multiple cutting-edge AI services to autonomously create films from text prompts.

## 🤖 Integrated AI Services

### 1. **Text Generation** (Director & Screenwriter Agents)
- **OpenAI GPT-4**: Creative vision, scene breakdown, dialogue
- **Anthropic Claude**: Alternative LLM for script generation
- **Usage**: Generates scripts, narration, and creative direction

### 2. **Video Generation** (Visual Content)
- **Stable Diffusion 2.1**: Image generation for keyframes
- **RunwayML Gen-2**: Text-to-video generation via Replicate
- **Stable Video Diffusion**: Alternative video generation
- **Usage**: Creates video clips for each scene

### 3. **Audio Generation** (Sound & Music)
- **ElevenLabs**: High-quality voiceover and narration
- **MusicGen (Meta)**: Background music generation via Replicate
- **Usage**: Generates voiceover and soundtrack

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure API Keys

Create a `.env` file in the `backend` directory:

```env
# AI Services - Text Generation
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...

# AI Services - Video Generation
REPLICATE_API_KEY=r8_...
STABILITY_API_KEY=sk-...

# AI Services - Audio Generation
ELEVENLABS_API_KEY=...

# Model Configuration
DEFAULT_TEXT_MODEL=gpt-4
DEFAULT_VIDEO_MODEL=runway-gen2
DEFAULT_VOICE_ID=21m00Tcm4TlvDq8ikWAM

# Database
DATABASE_URL=postgresql://localhost:5432/ai_film_studio

# Redis
REDIS_URL=redis://localhost:6379/0
```

### 3. Get API Keys

#### OpenAI
1. Visit https://platform.openai.com/api-keys
2. Create new API key
3. Copy to `.env` as `OPENAI_API_KEY`

#### Anthropic
1. Visit https://console.anthropic.com/
2. Create API key
3. Copy to `.env` as `ANTHROPIC_API_KEY`

#### Replicate (RunwayML + MusicGen)
1. Visit https://replicate.com/account/api-tokens
2. Create new token
3. Copy to `.env` as `REPLICATE_API_KEY`

#### ElevenLabs
1. Visit https://elevenlabs.io/
2. Go to Profile → API Keys
3. Copy to `.env` as `ELEVENLABS_API_KEY`

### 4. Start the Services

```bash
# Start backend
cd backend
uvicorn main:app --reload

# Start frontend (in another terminal)
cd frontend
npm run dev
```

## 🎯 API Endpoints

### Create Autonomous Film

```bash
POST /api/v1/autonomous/create-film
```

**Request Body:**
```json
{
  "prompt": "A futuristic city at sunset with flying cars",
  "style": "cinematic",
  "duration": 30,
  "voice_id": "21m00Tcm4TlvDq8ikWAM",
  "music_style": "epic orchestral",
  "model": "gpt-4"
}
```

**Response:**
```json
{
  "status": "success",
  "film_id": "uuid-here",
  "message": "Film created successfully with 3 scenes",
  "data": {
    "scenes": 3,
    "total_duration": 30,
    "director_vision": {...},
    "script": {...},
    "video_assets": [...],
    "audio_assets": [...],
    "timeline": [...]
  }
}
```

### Generate Single Scene

```bash
POST /api/v1/autonomous/generate-scene
```

**Parameters:**
- `prompt`: Scene description
- `style`: Visual style (default: "cinematic")
- `duration`: Scene duration in seconds
- `include_audio`: Generate audio (default: true)
- `voice_id`: ElevenLabs voice ID (optional)

### Get Agent Status

```bash
GET /api/v1/autonomous/agent-status
```

Returns status of all AI agents and services.

### List Available Voices

```bash
GET /api/v1/autonomous/voices
```

Returns list of available ElevenLabs voices.

## 🎭 Agent Workflow

1. **DirectorAgent**
   - Uses: OpenAI GPT-4 or Claude
   - Creates: Creative vision, scene breakdown
   - Output: Scene descriptions, shot types, moods

2. **ScreenwriterAgent**
   - Uses: OpenAI GPT-4 or Claude
   - Creates: Detailed scripts, dialogue, narration
   - Output: Script scenes with visual descriptions

3. **Video Generator**
   - Uses: Stable Diffusion, RunwayML
   - Creates: Video clips for each scene
   - Output: MP4 video files or URLs

4. **Audio Generator**
   - Uses: ElevenLabs, MusicGen
   - Creates: Voiceover and background music
   - Output: MP3 audio files

5. **EditorAgent**
   - Creates: Timeline, transitions, effects
   - Output: Final assembly instructions

## 💰 Cost Estimates (per 30-second film)

| Service | Cost per Film | Notes |
|---------|--------------|-------|
| OpenAI GPT-4 | ~$0.10 | Script generation |
| RunwayML Gen-2 | ~$2.00 | 3 scenes × ~$0.70/scene |
| ElevenLabs | ~$0.30 | Voiceover generation |
| MusicGen | Free | Via Replicate (metered) |
| **Total** | **~$2.40** | Per 30-second film |

## 🚀 Advanced Features

### Custom Voices

List available voices:
```python
from app.services.audio_generator import audio_generator

voices = await audio_generator.list_available_voices()
```

### Video Styles

Supported styles:
- `cinematic` - Professional movie style
- `anime` - Animated style
- `realistic` - Photorealistic
- `artistic` - Artistic/painterly
- `sci-fi` - Science fiction aesthetic

### Model Selection

```json
{
  "model": "gpt-4",           // or "claude-3-opus-20240229"
  "style": "cinematic",
  "music_style": "epic orchestral"  // or "ambient", "jazz", etc.
}
```

## 🔍 Monitoring & Debugging

### Check Service Status

```bash
curl http://localhost:8000/api/v1/autonomous/agent-status
```

### View Logs

```bash
# Backend logs
tail -f logs/app.log

# Check for errors
grep ERROR logs/app.log
```

### Clear Agent Memory

```bash
curl -X POST http://localhost:8000/api/v1/autonomous/clear-memory
```

## 🎨 Example Use Cases

### 1. Product Demo Video
```json
{
  "prompt": "A sleek smartphone with holographic display in a modern tech store",
  "style": "commercial",
  "duration": 15
}
```

### 2. Story Narration
```json
{
  "prompt": "An old wizard teaching a young apprentice magic in an ancient library",
  "style": "fantasy",
  "duration": 45,
  "music_style": "mystical orchestral"
}
```

### 3. Educational Content
```json
{
  "prompt": "Explaining how photosynthesis works with animated plant cells",
  "style": "educational",
  "duration": 60
}
```

## 📊 Performance Optimization

### GPU Acceleration

For local Stable Diffusion:
- Requires NVIDIA GPU with CUDA
- Minimum 8GB VRAM
- Significantly faster generation

### Caching

Models are cached after first use:
- Stable Diffusion: `~/.cache/huggingface`
- Video frames: `./storage/cache`

### Parallel Processing

Scenes are generated in parallel when possible:
```python
# Concurrent scene generation
video_tasks = [generate_video(scene) for scene in scenes]
results = await asyncio.gather(*video_tasks)
```

## 🛠️ Troubleshooting

### "Model not available" Error
- Check API keys in `.env`
- Verify API key validity
- Check service quotas

### Slow Generation
- Use GPU for Stable Diffusion
- Reduce video duration
- Use fewer scenes

### Out of Memory
- Reduce video resolution
- Use cloud services (Replicate)
- Process scenes sequentially

## 📚 Additional Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude Docs](https://docs.anthropic.com)
- [Replicate Docs](https://replicate.com/docs)
- [ElevenLabs Docs](https://docs.elevenlabs.io)
- [Stable Diffusion Guide](https://huggingface.co/stabilityai)

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines.

## 📄 License

See [LICENSE](./LICENSE) for details.
