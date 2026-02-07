"""SpiritualAgent main class - orchestrates all subsystems."""
from typing import Dict, Any, List, Optional
from pathlib import Path

from src.core.constants import SYSTEM_PROMPT
from src.memory.memory_manager import MemoryManager
from src.reasoning.context_analyzer import ContextAnalyzer
from src.dialogue.conversation_handler import ConversationHandler


class SpiritualAgent:
    """Autonomous agent that provides spiritual guidance.
    
    Responsibilities:
    - Orchestrates all subsystems
    - Manages session state
    - Routes requests to handlers
    - Coordinates responses
    """
    
    def __init__(self):
        """Initialize the spiritual agent."""
        self.memory = MemoryManager()
        self.context_analyzer = ContextAnalyzer()
        self.conversation = ConversationHandler()
        self.session_id = None
        
        # Load configuration
        self._load_config()
    
    def _load_config(self):
        """Load agent configuration."""
        config_path = Path(__file__).parent.parent.parent / "config" / "config.yaml"
        # TODO: Load from config file
        self.config = {
            "response_length": "balanced",
            "tone": "empathetic",
            "use_wisdom_quotes": True,
            "use_meditation_guidance": True,
        }
    
    def interact(self, user_message: str) -> str:
        """Main interaction method.
        
        Args:
            user_message: The user's input message
            
        Returns:
            The agent's response
        """
        # 1. Analyze context (emotion, intent, crisis indicators)
        context = self.context_analyzer.analyze(user_message)
        
        # 2. Get relevant memories
        relevant_memories = self.memory.recall(user_message)
        
        # 3. Generate response
        response = self.conversation.generate_response(
            user_message=user_message,
            context=context,
            memories=relevant_memories,
        )
        
        # 4. Store the interaction
        self.memory.store(user_message, response, context)
        
        return response
    
    def get_daily_meditation(self) -> str:
        """Get daily meditation guidance.
        
        Returns:
            Meditation text
        """
        return self.conversation.get_meditation()
    
    def get_insights(self) -> Dict[str, Any]:
        """Get user insights based on conversation history.
        
        Returns:
            Dictionary with insights
        """
        return self.memory.get_insights()
    
    def check_in(self) -> str:
        """Perform a wellness check-in.
        
        Returns:
            Check-in response
        """
        return "How are you feeling today? Take a moment to check in with yourself."
    
    def farewell(self) -> str:
        """Generate farewell message."""
        return (
            "May peace fill your heart and guide your steps. "
            "Remember: The journey inward is the most sacred adventure. "
            "I'll be here whenever you wish to continue our conversation."
        )
