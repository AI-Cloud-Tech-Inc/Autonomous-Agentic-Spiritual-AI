"""
Audio Generation Service
Integrates with ElevenLabs for voice, MusicGen for music
"""
from typing import Dict, Any, Optional, List
import logging
import asyncio
from elevenlabs.client import AsyncElevenLabs
from elevenlabs import VoiceSettings
import replicate
from app.core.config import settings

logger = logging.getLogger(__name__)


class AudioGenerator:
    """Audio generation using ElevenLabs and MusicGen"""
    
    def __init__(self):
        """Initialize audio generation services"""
        self.elevenlabs_client = None
        self.replicate_client = None
        
        if settings.ELEVENLABS_API_KEY:
            self.elevenlabs_client = AsyncElevenLabs(api_key=settings.ELEVENLABS_API_KEY)
            logger.info("ElevenLabs client initialized")
        
        if settings.REPLICATE_API_KEY:
            self.replicate_client = replicate.Client(api_token=settings.REPLICATE_API_KEY)
            logger.info("Replicate client for MusicGen initialized")
    
    async def generate_voiceover(
        self,
        text: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Default: Rachel
        model_id: str = "eleven_multilingual_v2",
        stability: float = 0.5,
        similarity_boost: float = 0.75,
        style: float = 0.0,
        use_speaker_boost: bool = True
    ) -> bytes:
        """
        Generate voiceover using ElevenLabs
        
        Args:
            text: Script text to convert to speech
            voice_id: ElevenLabs voice ID
            model_id: Model to use
            stability: Voice stability (0-1)
            similarity_boost: Voice similarity (0-1)
            style: Style exaggeration (0-1)
            use_speaker_boost: Enable speaker boost
            
        Returns:
            Audio data in bytes
        """
        if not self.elevenlabs_client:
            logger.warning("ElevenLabs not configured, returning silence")
            return b""
        
        try:
            audio_generator = await self.elevenlabs_client.text_to_speech.convert(
                text=text,
                voice_id=voice_id,
                model_id=model_id,
                voice_settings=VoiceSettings(
                    stability=stability,
                    similarity_boost=similarity_boost,
                    style=style,
                    use_speaker_boost=use_speaker_boost
                )
            )
            
            # Collect audio chunks
            audio_data = b""
            async for chunk in audio_generator:
                audio_data += chunk
            
            logger.info(f"Generated voiceover: {len(text)} chars -> {len(audio_data)} bytes")
            return audio_data
            
        except Exception as e:
            logger.error(f"Error generating voiceover: {str(e)}")
            return b""
    
    async def generate_music(
        self,
        prompt: str,
        duration: int = 30,
        temperature: float = 1.0,
        top_k: int = 250,
        top_p: float = 0.0
    ) -> str:
        """
        Generate background music using MusicGen
        
        Args:
            prompt: Music description
            duration: Duration in seconds
            temperature: Randomness (0-1.5)
            top_k: Top-k sampling
            top_p: Top-p sampling
            
        Returns:
            Audio file URL
        """
        if not self.replicate_client:
            logger.warning("MusicGen not configured")
            return ""
        
        try:
            output = await self.replicate_client.run(
                "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
                input={
                    "top_k": top_k,
                    "top_p": top_p,
                    "prompt": prompt,
                    "duration": duration,
                    "temperature": temperature,
                    "continuation": False,
                    "model_version": "stereo-large",
                    "output_format": "mp3",
                    "continuation_start": 0,
                    "multi_band_diffusion": False,
                    "normalization_strategy": "peak",
                    "classifier_free_guidance": 3
                }
            )
            
            logger.info(f"Generated music for prompt: {prompt}")
            return output
            
        except Exception as e:
            logger.error(f"Error generating music: {str(e)}")
            return ""
    
    async def generate_sound_effects(
        self,
        description: str,
        duration: int = 5
    ) -> str:
        """
        Generate sound effects
        
        Args:
            description: Sound effect description
            duration: Duration in seconds
            
        Returns:
            Audio file URL
        """
        # Use MusicGen for sound effects as well
        prompt = f"sound effect: {description}"
        return await self.generate_music(prompt, duration, temperature=1.2)
    
    async def generate_scene_audio(
        self,
        narration_text: str,
        music_prompt: str,
        duration: int,
        voice_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Generate complete audio for a scene (voiceover + music)
        
        Args:
            narration_text: Narration script
            music_prompt: Music description
            duration: Scene duration
            voice_id: Voice ID for narration
            
        Returns:
            Dictionary with voiceover and music URLs
        """
        # Generate in parallel
        voice_task = self.generate_voiceover(
            narration_text,
            voice_id or "21m00Tcm4TlvDq8ikWAM"
        )
        music_task = self.generate_music(music_prompt, duration)
        
        voiceover, music = await asyncio.gather(voice_task, music_task)
        
        return {
            "voiceover": voiceover,
            "music_url": music,
            "duration": duration,
            "narration_text": narration_text,
            "music_prompt": music_prompt
        }
    
    async def list_available_voices(self) -> List[Dict[str, Any]]:
        """Get list of available ElevenLabs voices"""
        if not self.elevenlabs_client:
            return []
        
        try:
            voices = await self.elevenlabs_client.voices.get_all()
            return [
                {
                    "voice_id": voice.voice_id,
                    "name": voice.name,
                    "category": voice.category,
                    "description": voice.description
                }
                for voice in voices.voices
            ]
        except Exception as e:
            logger.error(f"Error fetching voices: {str(e)}")
            return []


# Global instance
audio_generator = AudioGenerator()
