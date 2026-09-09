import sys
from pathlib import Path

# Ensure project root is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.langgraphagenticai.main import load_langgraph_agenticai_app

if __name__ == "__main__":
    load_langgraph_agenticai_app()