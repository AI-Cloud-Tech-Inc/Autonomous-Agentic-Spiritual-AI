"""
AI Services Integration Layer
"""
from typing import Optional, List, Dict
import json
from openai import AsyncOpenAI
from app.core.config import settings


class OpenAIService:
    """OpenAI GPT integration for script generation"""
    
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def generate_script(self, prompt: str, duration: int, tone: str = "professional") -> str:
        """Generate video script using GPT-4"""
        system_prompt = f"""You are a professional video scriptwriter. 
        Create a {duration}-second video script with a {tone} tone.
        
        Format the script with:
        - Scene numbers and descriptions
        - Voiceover/narration text
        - Approximate timing for each scene
        - Visual direction notes
        
        Make it engaging, concise, and suitable for AI video generation."""
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",  # Using mini for cost efficiency
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            # Fallback to demo script if API key is not configured
            if "api_key" in str(e).lower() or "authentication" in str(e).lower():
                return self._generate_demo_script(prompt, duration, tone)
            raise Exception(f"Script generation failed: {str(e)}")
    
    async def analyze_script_for_scenes(self, script: str) -> List[Dict]:
        """Break script into scenes for storyboarding"""
        prompt = f"""Analyze this video script and break it into distinct scenes.
        Return a JSON array where each scene has:
        - scene_number: integer
        - description: visual description for image generation
        - narration: the voiceover text
        - duration: duration in seconds
        
        Script:
        {script}
        
        Return ONLY the JSON array, no other text."""
        
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=1000,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            scenes = json.loads(content)
            return scenes.get("scenes", [])
        except Exception as e:
            if "api_key" in str(e).lower() or "authentication" in str(e).lower():
                return self._generate_demo_scenes()
            raise Exception(f"Scene analysis failed: {str(e)}")
    
    def _generate_demo_script(self, prompt: str, duration: int, tone: str) -> str:
        """Generate a demo script when API is not configured"""
        return f"""DEMO VIDEO SCRIPT - {duration} seconds
Theme: {prompt}
Tone: {tone}

SCENE 1 (0-10s)
Visual: Opening shot with dynamic graphics
Narration: "Welcome to the future of video creation with AI Film Studio."

SCENE 2 (10-20s)
Visual: Showcase of AI-powered features
Narration: "Transform your ideas into professional videos in minutes, not hours."

SCENE 3 (20-{duration}s)
Visual: Call to action with branding
Narration: "Start creating your masterpiece today."

Note: This is a demo script. Add your OpenAI API key in backend/.env for AI-generated scripts."""
    
    def _generate_demo_scenes(self) -> List[Dict]:
        """Generate demo scenes when API is not configured"""
        return [
            {
                "scene_number": 1,
                "description": "Dynamic opening with colorful graphics and modern design",
                "narration": "Welcome to AI Film Studio",
                "duration": 5
            },
            {
                "scene_number": 2,
                "description": "Professional workspace with AI technology visualization",
                "narration": "Create amazing videos with AI",
                "duration": 5
            }
        ]


class StabilityAIService:
    """Stability AI integration for image generation"""
    
    def __init__(self):
        self.api_key = settings.STABILITY_API_KEY
    
    async def generate_storyboard_frame(self, description: str) -> str:
        """Generate storyboard image from description"""
        # TODO: Implement Stability AI API integration
        # This is a placeholder
        return "path/to/generated/image.png"


class ReplicateService:
    """Replicate integration for video generation"""
    
    def __init__(self):
        self.api_token = settings.REPLICATE_API_TOKEN
    
    async def generate_video_scene(self, description: str, duration: int, style: str) -> str:
        """Generate video scene using AI models on Replicate"""
        # TODO: Implement Replicate API integration
        # This is a placeholder
        return "path/to/generated/video.mp4"


class ElevenLabsService:
    """ElevenLabs integration for voice synthesis"""
    
    def __init__(self):
        self.api_key = settings.ELEVENLABS_API_KEY
        self.api_url = "https://api.elevenlabs.io/v1"
    
    async def generate_voiceover(self, text: str, voice: str = "male", language: str = "en") -> str:
        """Generate voiceover from text using ElevenLabs"""
        import aiohttp
        import os
        
        # Default voice IDs (these are real ElevenLabs voice IDs)
        voice_map = {
            "male": "21m00Tcm4TlvDq8ikWAM",  # Rachel (can use for professional)
            "female": "21m00Tcm4TlvDq8ikWAM",
            "professional": "21m00Tcm4TlvDq8ikWAM"
        }
        
        voice_id = voice_map.get(voice, voice)
        
        if not self.api_key or self.api_key == "your-elevenlabs-api-key-here":
            # Return demo audio path
            return self._create_demo_audio(text)
        
        try:
            url = f"{self.api_url}/text-to-speech/{voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key
            }
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.5
                }
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=data, headers=headers) as response:
                    if response.status == 200:
                        # Save audio file
                        os.makedirs("media/audio", exist_ok=True)
                        audio_path = f"media/audio/voice_{hash(text)}.mp3"
                        
                        with open(audio_path, 'wb') as f:
                            f.write(await response.read())
                        
                        return audio_path
                    else:
                        raise Exception(f"ElevenLabs API error: {response.status}")
        
        except Exception as e:
            if "api" in str(e).lower():
                return self._create_demo_audio(text)
            raise Exception(f"Voiceover generation failed: {str(e)}")
    
    async def get_available_voices(self) -> List[Dict]:
        """Get list of available voices"""
        import aiohttp
        
        if not self.api_key or self.api_key == "your-elevenlabs-api-key-here":
            return self._get_demo_voices()
        
        try:
            url = f"{self.api_url}/voices"
            headers = {"xi-api-key": self.api_key}
            
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=headers) as response:
                    if response.status == 200:
                        data = await response.json()
                        return [
                            {"id": v["voice_id"], "name": v["name"]} 
                            for v in data.get("voices", [])
                        ]
        except:
            pass
        
        return self._get_demo_voices()
    
    def _create_demo_audio(self, text: str) -> str:
        """Create a placeholder for demo audio"""
        import os
        os.makedirs("media/audio", exist_ok=True)
        demo_path = "media/audio/demo_voice.txt"
        with open(demo_path, 'w') as f:
            f.write(f"Demo voiceover: {text}\n\nAdd your ElevenLabs API key for real voice synthesis.")
        return demo_path
    
    def _get_demo_voices(self) -> List[Dict]:
        """Get demo voice list"""
        return [
            {"id": "male_professional", "name": "Professional Male (Demo)"},
            {"id": "female_professional", "name": "Professional Female (Demo)"},
            {"id": "narrator", "name": "Documentary Narrator (Demo)"}
        ]


# Service instances
openai_service = OpenAIService()
stability_service = StabilityAIService()
replicate_service = ReplicateService()
elevenlabs_service = ElevenLabsService()
