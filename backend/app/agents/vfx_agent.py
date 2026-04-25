"""
VFX Agent - Visual Effects & Color Grading
"""
import json
from typing import Dict, Any
import logging
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a world-class VFX supervisor and colorist with expertise in visual effects,
color grading, CGI integration, and quality assurance for film and video productions.
Always respond with valid JSON only."""


class VFXAgent(BaseAgent):
    """Identifies VFX opportunities, applies color grading, and ensures visual quality."""

    def __init__(self, model: str = "claude-opus-4-6", anthropic_api_key: str = ""):
        super().__init__(name="VFX", model=model, anthropic_api_key=anthropic_api_key)

    async def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        scenes = input_data.get("scenes", [])
        shot_plans = input_data.get("shot_plans", [])
        style = input_data.get("style", "cinematic")
        vision = input_data.get("vision", "")

        logger.info(f"VFX processing {len(scenes)} scenes...")

        vfx_plans = []
        for i, scene in enumerate(scenes):
            shot = shot_plans[i] if i < len(shot_plans) else {}
            vfx_plans.append(await self._plan_vfx(scene, shot, style, vision))

        result = {"vfx_plans": vfx_plans, "style": style, "agent": self.name}
        self.add_to_memory(result)
        return result

    async def _plan_vfx(self, scene: Dict[str, Any], shot: Dict[str, Any],
                        style: str, vision: str) -> Dict[str, Any]:
        user_msg = (
            f"Visual style: {style}\n"
            f"Director's vision: {vision}\n\n"
            f"Scene {scene.get('scene_number')}: {scene.get('description')}\n"
            f"Mood: {scene.get('mood')}\n"
            f"Lighting: {shot.get('lighting', 'natural')}\n"
            f"Color palette: {shot.get('color_palette', [])}\n\n"
            "Return a JSON object with:\n"
            "- scene_number (int)\n"
            "- color_grading (object: lut, contrast, saturation, temperature, mood)\n"
            "- vfx_elements (array of objects: type, description, compositing_mode)\n"
            "- enhancements (array of strings: suggested post-processing effects)\n"
            "- quality_notes (string: technical quality considerations)"
        )
        raw = await self._ask_claude(user_msg, SYSTEM_PROMPT, max_tokens=768)
        try:
            start, end = raw.find("{"), raw.rfind("}") + 1
            return json.loads(raw[start:end])
        except Exception:
            logger.warning(f"VFX: failed to parse scene {scene.get('scene_number')} JSON")
            return {
                "scene_number": scene.get("scene_number", 1),
                "color_grading": {
                    "lut": "cinematic",
                    "contrast": 1.1,
                    "saturation": 1.0,
                    "temperature": 0,
                    "mood": "warm",
                },
                "vfx_elements": [],
                "enhancements": ["subtle film grain", "lens flare"],
                "quality_notes": "Standard post-processing pipeline",
            }
