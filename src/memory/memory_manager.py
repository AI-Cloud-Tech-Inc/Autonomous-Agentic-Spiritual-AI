"""Memory systems (short-term, long-term, episodic)."""
from collections import deque
from typing import List, Dict, Any, Optional
from pathlib import Path
import json
from datetime import datetime


class MemoryManager:
    """Manages different memory systems for the spiritual agent."""
    
    def __init__(self, max_short_term: int = 20, max_episodic: int = 50):
        """Initialize memory manager.
        
        Args:
            max_short_term: Maximum short-term memories to keep
            max_episodic: Maximum episodic memories to keep
        """
        self.short_term = deque(maxlen=max_short_term)  # Recent conversation
        self.long_term = {}  # User profile, preferences
        self.episodic = []  # Significant interactions
        self.max_episodic = max_episodic
        
        # Load from storage if exists
        self._load_memories()
    
    def store(self, user_message: str, agent_response: str, context: Dict[str, Any]) -> None:
        """Store a new interaction.
        
        Args:
            user_message: The user's message
            agent_response: The agent's response
            context: Detected context (emotion, intent)
        """
        # Add to short-term memory
        self.short_term.append({
            "user": user_message,
            "agent": agent_response,
            "timestamp": datetime.now().isoformat(),
            "context": context,
        })
        
        # Check if this is significant (for episodic memory)
        is_significant = self._is_significant(context)
        if is_significant:
            self.episodic.append({
                "user": user_message,
                "agent": agent_response,
                "timestamp": datetime.now().isoformat(),
                "context": context,
            })
            # Trim episodic memory
            if len(self.episodic) > self.max_episodic:
                self.episodic = self.episodic[-self.max_episodic:]
        
        # Update long-term memory with patterns
        self._update_long_term(context)
        
        # Persist memories
        self._save_memories()
    
    def recall(self, query: str) -> List[Dict[str, Any]]:
        """Recall relevant memories based on query.
        
        Args:
            query: The user's message to match against
            
        Returns:
            List of relevant memories
        """
        # Return recent conversation history
        return list(self.short_term)
    
    def get_insights(self) -> Dict[str, Any]:
        """Get insights based on conversation history.
        
        Returns:
            Dictionary with emotional trends, topics discussed, etc.
        """
        emotions = [m.get("context", {}).get("emotion") for m in self.short_term if m.get("context")]
        topics = [m.get("context", {}).get("intent") for m in self.short_term if m.get("context")]
        
        return {
            "total_interactions": len(self.short_term),
            "emotions_expressed": list(set([e for e in emotions if e])),
            "topics_discussed": list(set([t for t in topics if t])),
            "emotional_trend": self._get_emotional_trend(),
        }
    
    def _is_significant(self, context: Dict[str, Any]) -> bool:
        """Check if an interaction is significant enough for episodic memory."""
        # Crisis events are always significant
        if context.get("is_crisis"):
            return True
        
        # Emotional peaks are significant
        emotion = context.get("emotion")
        if emotion in ["joy", "sadness", "fear"]:
            return True
        
        # Deep spiritual discussions
        intent = context.get("intent")
        if intent in ["spiritual_question", "meditation_request", "crisis_support"]:
            return True
        
        return False
    
    def _update_long_term(self, context: Dict[str, Any]) -> None:
        """Update long-term memory with patterns."""
        emotion = context.get("emotion")
        if emotion:
            if "emotions" not in self.long_term:
                self.long_term["emotions"] = {}
            self.long_term["emotions"][emotion] = self.long_term["emotions"].get(emotion, 0) + 1
    
    def _get_emotional_trend(self) -> str:
        """Get the emotional trend over recent interactions."""
        if not self.short_term:
            return "neutral"
        
        emotions = [m.get("context", {}).get("emotion") for m in self.short_term if m.get("context")]
        if not emotions:
            return "neutral"
        
        # Simple trend detection
        recent = emotions[-5:]
        if len(recent) >= 3:
            if recent[-1] == recent[-2] == recent[-3]:
                return recent[-1]
        
        return "varied"
    
    def _load_memories(self) -> None:
        """Load memories from disk."""
        data_dir = Path(__file__).parent.parent.parent / "data" / "user_data"
        data_dir.mkdir(parents=True, exist_ok=True)
        
        memory_file = data_dir / "memories.json"
        if memory_file.exists():
            try:
                with open(memory_file, "r") as f:
                    data = json.load(f)
                    self.episodic = data.get("episodic", [])
                    self.long_term = data.get("long_term", {})
            except Exception:
                pass
    
    def _save_memories(self) -> None:
        """Save memories to disk."""
        data_dir = Path(__file__).parent.parent.parent / "data" / "user_data"
        data_dir.mkdir(parents=True, exist_ok=True)
        
        memory_file = data_dir / "memories.json"
        with open(memory_file, "w") as f:
            json.dump({
                "episodic": self.episodic,
                "long_term": self.long_term,
            }, f, indent=2)
