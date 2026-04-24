"""
Director Agent - Creative Vision & Planning
"""
import json
from typing import Dict, Any
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

# Used for the creative vision statement — plain prose, no JSON required.
VISION_SYSTEM_PROMPT = """You are an award-winning film director with decades of experience.
You craft compelling visual narratives and give each project a distinctive aesthetic identity."""

# Used for scene breakdown — must return a JSON array.
SCENE_SYSTEM_PROMPT = """You are an award-winning film director with decades of experience.
You break stories into dynamic scenes. Always respond with valid JSON only."""


class DirectorAgent(BaseAgent):
    """Creates the creative vision and scene breakdown for a film."""

    def __init__(self, model: str = "claude-opus-4-6", anthropic_api_key: str = ""):
        super().__init__(name="Director", model=model, anthropic_api_key=anthropic_api_key)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        prompt = input_data.get("prompt", "")
        style = input_data.get("style", "cinematic")
        duration = input_data.get("duration", 30)

        logger.info(f"Director processing: {prompt[:60]}...")

        vision = await self._create_vision(prompt, style, duration)
        scenes = await self._break_down_scenes(vision, prompt, duration)

        result = {"vision": vision, "scenes": scenes, "style": style, "agent": self.name}
        self.add_to_memory(result)
        return result

    async def _create_vision(self, prompt: str, style: str, duration: int) -> str:
        user_msg = (
            f"Film concept: {prompt}\n"
            f"Visual style: {style}\n"
            f"Duration: {duration} seconds\n\n"
            "Write a concise creative vision statement (3-4 sentences) covering tone, "
            "visual aesthetic, pacing, and emotional arc. Return plain text, no JSON."
        )
        return await self._ask_claude(user_msg, VISION_SYSTEM_PROMPT, max_tokens=512)

    async def _break_down_scenes(self, vision: str, prompt: str, duration: int) -> list[Dict[str, Any]]:
        scene_count = max(3, duration // 10)
        user_msg = (
            f"Film concept: {prompt}\n"
            f"Director's vision: {vision}\n"
            f"Total duration: {duration} seconds\n"
            f"Number of scenes: {scene_count}\n\n"
            f"Return a JSON array of exactly {scene_count} scene objects. "
            "Each object must have: scene_number (int), description (string), "
            "duration (int, seconds), shot_type (wide/medium/close-up/extreme-close-up), "
            "mood (string), visual_prompt (detailed image generation prompt as string)."
        )
        raw = await self._ask_claude(user_msg, SCENE_SYSTEM_PROMPT, max_tokens=2048)
        try:
            start, end = raw.find("["), raw.rfind("]") + 1
            return json.loads(raw[start:end])
        except Exception:
            logger.warning("Director: failed to parse scene JSON, using fallback")
            return [
                {"scene_number": i + 1, "description": f"Scene {i + 1}", "duration": duration // scene_count,
                 "shot_type": "medium", "mood": "neutral", "visual_prompt": prompt}
                for i in range(scene_count)
            ]
