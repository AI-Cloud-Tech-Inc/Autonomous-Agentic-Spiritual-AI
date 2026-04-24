"""Response generation and conversation handling."""
from typing import Dict, Any, List, Optional
from pathlib import Path
import json


class ConversationHandler:
    """Handles conversation flow and response generation."""
    
    def __init__(self):
        """Initialize conversation handler."""
        self.meditation_prompts = self._load_meditation_prompts()
        self.wisdom_quotes = self._load_wisdom_quotes()
    
    def generate_response(
        self,
        user_message: str,
        context: Dict[str, Any],
        memories: List[Dict[str, Any]],
    ) -> str:
        """Generate a contextual response.
        
        Args:
            user_message: The user's message
            context: Detected context (emotion, intent)
            memories: Relevant conversation history
            
        Returns:
            Generated response
        """
        intent = context.get("intent", "general_conversation")
        emotion = context.get("emotion")
        is_crisis = context.get("is_crisis", False)
        
        # Crisis intervention
        if is_crisis:
            return self._handle_crisis()
        
        # Intent-based response
        if intent == "meditation_request":
            return self._generate_meditation_response(emotion)
        elif intent == "emotional_support":
            return self._generate_emotional_support(emotion)
        elif intent == "gratitude":
            return self._generate_gratitude_response()
        elif intent == "wisdom_seeking":
            return self._generate_wisdom_response(context)
        elif intent == "spiritual_question":
            return self._generate_spiritual_response(user_message)
        else:
            return self._generate_general_response(user_message, context)
    
    def get_meditation(self) -> str:
        """Get a meditation prompt."""
        import random
        return random.choice(self.meditation_prompts)
    
    def _generate_meditation_response(self, emotion: Optional[str]) -> str:
        """Generate meditation response based on emotion."""
        meditations = {
            "anxiety": "Take a moment to breathe deeply. Inhale peace, exhale tension...",
            "sadness": "Allow yourself this moment of stillness. Your feelings are valid...",
            "peace": "Continue nurturing this peaceful state. Notice the stillness...",
            None: "Find a comfortable position. Take a deep breath...",
        }
        return meditations.get(emotion, meditations[None])
    
    def _generate_emotional_support(self, emotion: Optional[str]) -> str:
        """Generate emotional support response."""
        responses = {
            "sadness": "I hear you. It's okay to feel sad. Would you like to talk about what's on your heart?",
            "fear": "Fear is natural. You're not alone. Let's take this one breath at a time together.",
            "anger": "I see your frustration. It's valid to feel what you feel.",
            "joy": "I'm glad you're feeling joyful! What has brought this happiness?",
            None: "I'm here to listen. What's on your mind?",
        }
        return responses.get(emotion, responses[None])
    
    def _generate_gratitude_response(self) -> str:
        """Generate gratitude response."""
        return (
            "Gratitude is a powerful practice. "
            "Taking time to appreciate what we have cultivates inner wealth. "
            "What are you most grateful for today?"
        )
    
    def _generate_wisdom_response(self, context: Dict[str, Any]) -> str:
        """Generate wisdom sharing response."""
        import random
        
        wisdom = random.choice(self.wisdom_quotes)
        return f"{wisdom}\n\nWhat are your thoughts on this?"
    
    def _generate_spiritual_response(self, question: str) -> str:
        """Generate response to spiritual question."""
        return (
            "That's a profound question. "
            "Spiritual wisdom often comes from many traditions. "
            "What draws you to this question? Let's explore it together."
        )
    
    def _generate_general_response(self, message: str, context: Dict[str, Any]) -> str:
        """Generate general conversational response."""
        themes = context.get("themes", [])
        
        if "mindfulness" in themes:
            return "I sense you're interested in mindfulness. How has your practice been?"
        elif "compassion" in themes:
            return "Compassion is a beautiful quality. How do you cultivate it in your life?"
        elif "peace" in themes:
            return "Peace is within reach. What helps you find stillness?"
        else:
            return "I'm here to listen and reflect with you. Tell me more."
    
    def _handle_crisis(self) -> str:
        """Handle crisis situation with appropriate response."""
        return (
            "I hear you, and I want you to know that your life matters. "
            "What you're feeling is important, and you don't have to face this alone. "
            "Please consider reaching out to a crisis helpline or trusted person: "
            "National Suicide Prevention Lifeline: 988 (US) "
            "I'm here to support you, but please also connect with professional help."
        )
    
    def _load_meditation_prompts(self) -> List[str]:
        """Load meditation prompts from data."""
        prompts = [
            "Find a comfortable seated position. Close your eyes and take three deep breaths...",
            "Bring your attention to the present moment. What do you hear? What do you feel?",
            "Visualize a warm light filling your heart space, spreading warmth through your body...",
            "Notice your thoughts without judgment. Let them pass like clouds in the sky...",
            "Focus on your breath. Inhale peace, exhale tension. Repeat...",
        ]
        
        # Try to load from file
        prompts_file = Path(__file__).parent.parent.parent / "data" / "prompts" / "meditation_prompts.md"
        if prompts_file.exists():
            try:
                with open(prompts_file, "r") as f:
                    content = f.read()
                    # Parse prompts from markdown
                    prompts = [p.strip() for p in content.split("---") if p.strip()]
            except Exception:
                pass
        
        return prompts
    
    def _load_wisdom_quotes(self) -> List[str]:
        """Load wisdom quotes from data."""
        quotes = [
            "The journey of a thousand miles begins with a single step. — Lao Tzu",
            "Peace comes from within. Do not seek it without. — Buddha",
            "Be the change you wish to see in the world. — Gandhi",
            "In the end, it's not the years in your life that count. It's the life in your years. — Lincoln",
            "The only way to do great work is to love what you do. — Jobs",
        ]
        
        quotes_file = Path(__file__).parent.parent.parent / "data" / "teachings" / "quotes.json"
        if quotes_file.exists():
            try:
                with open(quotes_file, "r") as f:
                    data = json.load(f)
                    quotes = data.get("quotes", quotes)
            except Exception:
                pass
        
        return quotes
