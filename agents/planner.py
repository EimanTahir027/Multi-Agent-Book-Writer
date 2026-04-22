"""
Planner Agent
Responsible for defining the book structure and chapters.
"""

import requests
from shared.context import context, update_context

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def run_planner(num_chapters=5):
    """
    Generate a chapter plan for the book.
    
    Args:
        num_chapters: Number of chapters to plan for
    """
    print("[PLANNER] Starting chapter planning...")
    
    prompt = f"""Plan {num_chapters} detailed chapters for a book titled '{context['title']}'. 
For each chapter, provide a clear title and brief description.
Format: 
Chapter 1: Title - Description
Chapter 2: Title - Description
etc."""
    
    try:
        response = requests.post(OLLAMA_API_URL, json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        })
        
        if response.status_code == 200:
            chapters_text = response.json()["response"].strip()
            chapters = [ch.strip() for ch in chapters_text.split("\n") if ch.strip()]
            
            update_context("chapters", chapters)
            print(f"[PLANNER] Planned {len(chapters)} chapters:")
            for ch in chapters:
                print(f"  - {ch}")
            return chapters
        else:
            print(f"[PLANNER] Error: {response.status_code}")
            return []
    except requests.exceptions.ConnectionError:
        print("[PLANNER] Error: Could not connect to Ollama. Make sure it's running on http://localhost:11434")
        return []
    except Exception as e:
        print(f"[PLANNER] Error: {str(e)}")
        return []
