"""
Cinematographer Agent - Visual Composition & Shot Planning
"""
import json
from typing import Dict, Any
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a world-class cinematographer who creates stunning visual compositions.
You specify camera movements, lighting setups, color grading, and lens choices.
Your shot descriptions are used directly as image/video generation prompts.
Always respond with valid JSON only."""


class CinematographerAgent(BaseAgent):
    """Turns scene descriptions into detailed visual/camera specifications."""

    def __init__(self, model: str = "claude-opus-4-6", anthropic_api_key: str = ""):
        super().__init__(name="Cinematographer", model=model, anthropic_api_key=anthropic_api_key)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        scenes = input_data.get("scenes", [])
        style = input_data.get("style", "cinematic")
        vision = input_data.get("vision", "")

        logger.info(f"Cinematographer planning shots for {len(scenes)} scenes...")

        shot_plans = []
        for scene in scenes:
            shot_plans.append(await self._plan_shot(scene, style, vision))

        result = {"shot_plans": shot_plans, "style": style, "agent": self.name}
        self.add_to_memory(result)
        return result

    async def _plan_shot(self, scene: Dict[str, Any], style: str, vision: str) -> Dict[str, Any]:
        user_msg = (
            f"Visual style: {style}\n"
            f"Director's vision: {vision}\n\n"
            f"Scene {scene.get('scene_number')}: {scene.get('description')}\n"
            f"Shot type: {scene.get('shot_type')}, Mood: {scene.get('mood')}\n"
            f"Visual prompt hint: {scene.get('visual_prompt', '')}\n\n"
            "Return a JSON object with:\n"
            "- scene_number (int)\n"
            "- camera_movement (string: static/pan/tilt/dolly/handheld/crane)\n"
            "- lens (string: wide-angle/standard/telephoto/macro)\n"
            "- lighting (string: natural/golden-hour/low-key/high-key/neon/dramatic)\n"
            "- color_palette (array of 3-5 color descriptors)\n"
            "- image_generation_prompt (string, highly detailed prompt for Stable Diffusion or similar)\n"
            "- depth_of_field (string: shallow/deep/rack-focus)"
        )
        raw = await self._ask_claude(user_msg, SYSTEM_PROMPT, max_tokens=768)
        try:
            start, end = raw.find("{"), raw.rfind("}") + 1
            return json.loads(raw[start:end])
        except Exception:
            logger.warning(f"Cinematographer: failed to parse scene {scene.get('scene_number')} JSON")
            return {
                "scene_number": scene.get("scene_number", 1),
                "camera_movement": "static",
                "lens": "standard",
                "lighting": "natural",
                "color_palette": ["neutral", "warm", "cinematic"],
                "image_generation_prompt": scene.get("visual_prompt", scene.get("description", "")),
                "depth_of_field": "shallow",
            }
