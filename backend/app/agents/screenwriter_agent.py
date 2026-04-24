"""
Screenwriter Agent - Script & Dialogue Generation
"""
import json
from typing import Dict, Any, List
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a professional screenwriter who crafts vivid, emotionally resonant
scripts. You write natural dialogue, evocative narration, and precise visual directions.
Always respond with valid JSON only."""


class ScreenwriterAgent(BaseAgent):
    """Writes detailed scripts with dialogue and narration for each scene."""

    def __init__(self, model: str = "claude-opus-4-6", anthropic_api_key: str = ""):
        super().__init__(name="Screenwriter", model=model, anthropic_api_key=anthropic_api_key)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        vision = input_data.get("vision", "")
        scenes = input_data.get("scenes", [])

        logger.info(f"Screenwriter scripting {len(scenes)} scenes...")

        script_scenes = []
        for scene in scenes:
            script_scenes.append(await self._write_scene(scene, vision))

        result = {"script_scenes": script_scenes, "total_scenes": len(script_scenes), "agent": self.name}
        self.add_to_memory(result)
        return result

    async def _write_scene(self, scene: Dict[str, Any], vision: str) -> Dict[str, Any]:
        user_msg = (
            f"Director's vision: {vision}\n\n"
            f"Scene {scene.get('scene_number')}: {scene.get('description')}\n"
            f"Shot type: {scene.get('shot_type')}, Mood: {scene.get('mood')}, "
            f"Duration: {scene.get('duration')}s\n\n"
            "Return a JSON object with these fields:\n"
            "- scene_number (int)\n"
            "- description (string)\n"
            "- narration (string, voiceover text)\n"
            "- dialogue (array of {character, line} objects, can be empty)\n"
            "- visual_description (string, detailed shot description)\n"
            "- audio_cues (array of strings)\n"
            "- duration (int, seconds)"
        )
        raw = await self._ask_claude(user_msg, SYSTEM_PROMPT, max_tokens=1024)
        try:
            start, end = raw.find("{"), raw.rfind("}") + 1
            return json.loads(raw[start:end])
        except Exception:
            logger.warning(f"Screenwriter: failed to parse scene {scene.get('scene_number')} JSON")
            return {
                "scene_number": scene.get("scene_number", 1),
                "description": scene.get("description", ""),
                "narration": f"A {scene.get('mood', 'neutral')} moment unfolds.",
                "dialogue": [],
                "visual_description": f"{scene.get('shot_type', 'MEDIUM')} SHOT: {scene.get('description', '')}",
                "audio_cues": [f"{scene.get('mood', 'neutral')} background music"],
                "duration": scene.get("duration", 10),
            }
