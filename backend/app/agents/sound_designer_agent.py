"""
Sound Designer Agent - Audio Landscape Planning
"""
import json
from typing import Dict, Any
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are an acclaimed sound designer who creates immersive audio landscapes.
You specify music genres, sound effects, voiceover tone, and mixing instructions.
Your audio descriptions drive the voiceover and sound generation pipeline.
Always respond with valid JSON only."""


class SoundDesignerAgent(BaseAgent):
    """Plans the complete audio landscape: music, SFX, and voiceover guidance."""

    def __init__(self, model: str = "claude-opus-4-6", anthropic_api_key: str = ""):
        super().__init__(name="SoundDesigner", model=model, anthropic_api_key=anthropic_api_key)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        script_scenes = input_data.get("script_scenes", [])
        style = input_data.get("style", "cinematic")
        vision = input_data.get("vision", "")

        logger.info(f"Sound Designer planning audio for {len(script_scenes)} scenes...")

        audio_plans = []
        for scene in script_scenes:
            audio_plans.append(await self._plan_audio(scene, style, vision))

        result = {"audio_plans": audio_plans, "agent": self.name}
        self.add_to_memory(result)
        return result

    async def _plan_audio(self, scene: Dict[str, Any], style: str, vision: str) -> Dict[str, Any]:
        user_msg = (
            f"Film style: {style}\n"
            f"Director's vision: {vision}\n\n"
            f"Scene {scene.get('scene_number')}: {scene.get('description', '')}\n"
            f"Mood: {scene.get('mood', 'neutral')}\n"
            f"Narration text: {scene.get('narration', '')}\n"
            f"Audio cues hint: {scene.get('audio_cues', [])}\n\n"
            "Return a JSON object with:\n"
            "- scene_number (int)\n"
            "- music_genre (string)\n"
            "- music_tempo (string: slow/medium/fast/dynamic)\n"
            "- music_instruments (array of strings)\n"
            "- sound_effects (array of strings)\n"
            "- voiceover_tone (string: calm/dramatic/excited/mysterious/warm)\n"
            "- voiceover_pace (string: slow/normal/fast)\n"
            "- mixing_notes (string: brief audio mixing guidance)\n"
            "- elevenlabs_voice_id (string: suggested voice type e.g. 'deep-male' / 'warm-female' / 'neutral')"
        )
        raw = await self._ask_claude(user_msg, SYSTEM_PROMPT, max_tokens=768)
        try:
            start, end = raw.find("{"), raw.rfind("}") + 1
            return json.loads(raw[start:end])
        except Exception:
            logger.warning(f"SoundDesigner: failed to parse scene {scene.get('scene_number')} JSON")
            return {
                "scene_number": scene.get("scene_number", 1),
                "music_genre": "cinematic orchestral",
                "music_tempo": "medium",
                "music_instruments": ["strings", "piano"],
                "sound_effects": ["ambient"],
                "voiceover_tone": "calm",
                "voiceover_pace": "normal",
                "mixing_notes": "Music at 30%, SFX at 20%, voiceover at 100%",
                "elevenlabs_voice_id": "neutral",
            }
