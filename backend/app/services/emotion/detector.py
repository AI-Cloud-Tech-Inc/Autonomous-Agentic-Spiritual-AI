"""Emotion detection from user messages for context-aware responses."""


class EmotionDetector:
    """Detects emotional state from user text to adapt agent responses.

    Uses a combination of keyword analysis and LLM-based inference
    to understand the user's emotional context without making assumptions.
    """

    EMOTION_CATEGORIES = [
        "calm", "anxious", "grateful", "sad", "curious",
        "frustrated", "hopeful", "confused", "joyful", "reflective",
    ]

    async def detect(self, text: str) -> dict:
        """Analyze text and return detected emotional signals.

        Args:
            text: The user's message text.

        Returns:
            A dict with primary_emotion, confidence, and signals.
        """
        # TODO: Implement emotion detection (LLM-based + heuristic)
        return {
            "primary_emotion": "reflective",
            "confidence": 0.0,
            "signals": [],
        }
