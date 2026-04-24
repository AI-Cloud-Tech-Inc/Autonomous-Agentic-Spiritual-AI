"""Main entry point for Autonomous Agentic Spiritual AI."""
import sys
import io

# Enable UTF-8 encoding for stdout/stderr
if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr.encoding.lower() != 'utf-8':
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.core.agent import SpiritualAgent
from src.core.constants import GREETING, FAREWELL


def main():
    """Main entry point."""
    print(GREETING)
    
    agent = SpiritualAgent()
    
    try:
        while True:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ["quit", "exit", "bye"]:
                print(f"\nAgent: {FAREWELL}")
                break
            
            response = agent.interact(user_input)
            print(f"\nAgent: {response}")
            
    except KeyboardInterrupt:
        print("\n\nAgent: Take care on your spiritual journey. 🙏")


if __name__ == "__main__":
    main()
