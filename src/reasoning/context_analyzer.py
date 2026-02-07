"""Context analyzer - intent & emotion detection, crisis indicators."""
from typing import Dict, Any, List, Tuple
from src.core.constants import EMOTION_KEYWORDS


class ContextAnalyzer:
    """Analyzes user input to detect context (emotion, intent, crisis)."""
    
    def __init__(self):
        """Initialize context analyzer."""
        self.emotion_keywords = EMOTION_KEYWORDS
        self.crisis_keywords = [
            "suicide", "kill myself", "end my life", "hurt myself",
            "self-harm", "cutting myself", "want to die",
        ]
        self.intent_patterns = {
            "meditation_request": [
                "meditate", "meditation", "breathing", "breathe",
                "mindfulness", "practice", "guided",
            ],
            "spiritual_question": [
                "meaning", "purpose", "life", "death", "soul",
                "spiritual", "enlightenment", "awakening",
            ],
            "emotional_support": [
                "sad", "angry", "lonely", "hurt", "pain", "scared",
                "anxious", "worried", "depressed", "feel",
            ],
            "gratitude": [
                "thankful", "grateful", "appreciate", "blessed",
            ],
            "wisdom_seeking": [
                "advice", "guidance", "wisdom", "teach me",
                "learn", "understand",
            ],
        }
    
    def analyze(self, message: str) -> Dict[str, Any]:
        """Analyze user message for context.
        
        Args:
            message: The user's message
            
        Returns:
            Dictionary with detected context
        """
        message_lower = message.lower()
        
        emotion = self._detect_emotion(message_lower)
        intent = self._detect_intent(message_lower)
        is_crisis = self._detect_crisis(message_lower)
        themes = self._extract_themes(message_lower)
        
        return {
            "emotion": emotion,
            "intent": intent,
            "is_crisis": is_crisis,
            "themes": themes,
            "message_length": len(message),
        }
    
    def _detect_emotion(self, message: str) -> str | None:
        """Detect emotion from message."""
        emotion_scores = {}
        
        for emotion, keywords in self.emotion_keywords.items():
            score = sum(1 for kw in keywords if kw in message)
            if score > 0:
                emotion_scores[emotion] = score
        
        if emotion_scores:
            return max(emotion_scores, key=emotion_scores.get)
        return None
    
    def _detect_intent(self, message: str) -> str:
        """Detect user intent from message."""
        intent_scores = {}
        
        for intent, patterns in self.intent_patterns.items():
            score = sum(1 for p in patterns if p in message)
            if score > 0:
                intent_scores[intent] = score
        
        if intent_scores:
            return max(intent_scores, key=intent_scores.get)
        return "general_conversation"
    
    def _detect_crisis(self, message: str) -> bool:
        """Detect crisis indicators in message."""
        return any(kw in message for kw in self.crisis_keywords)
    
    def _extract_themes(self, message: str) -> List[str]:
        """Extract spiritual themes from message."""
        themes = []
        
        theme_keywords = {
            "mindfulness": ["present", "now", "aware", "attention", "focus"],
            "compassion": ["kindness", "love", "care", "forgiveness"],
            "impermanence": ["change", "change", " impermanent", "transient"],
            "suffering": ["suffer", "struggle", "difficult", "hard"],
            "peace": ["peace", "calm", "serene", "quiet", "still"],
            "connection": ["connect", "together", "unity", "oneness"],
        }
        
        for theme, keywords in theme_keywords.items():
            if any(kw in message for kw in keywords):
                themes.append(theme)
        
        return themes
