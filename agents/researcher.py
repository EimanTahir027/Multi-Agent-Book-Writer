"""
Researcher Agent
Responsible for gathering background information and research for each chapter.
"""

import requests
from shared.context import context, update_context

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def run_researcher():
    """
    Research background facts and details for each chapter.
    """
    print("[RESEARCHER] Starting research phase...")
    
    research_data = {}
    chapters = context.get("chapters", [])
    
    if not chapters:
        print("[RESEARCHER] No chapters found in context. Skipping research.")
        return
    
    for i, chapter in enumerate(chapters, 1):
        print(f"[RESEARCHER] Researching chapter {i}/{len(chapters)}: {chapter}")
        
        prompt = f"""Provide background facts, historical context, key statistics, relevant quotes, 
and important details for a book chapter titled '{chapter}'. 
Make it informative and substantive (2-3 paragraphs)."""
        
        try:
            response = requests.post(OLLAMA_API_URL, json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            })
            
            if response.status_code == 200:
                research_content = response.json()["response"].strip()
                research_data[chapter] = research_content
                print(f"[RESEARCHER] Research completed for: {chapter}")
            else:
                print(f"[RESEARCHER] Error for chapter '{chapter}': {response.status_code}")
                research_data[chapter] = ""
                
        except requests.exceptions.ConnectionError:
            print("[RESEARCHER] Error: Could not connect to Ollama. Make sure it's running on http://localhost:11434")
            break
        except Exception as e:
            print(f"[RESEARCHER] Error researching '{chapter}': {str(e)}")
            research_data[chapter] = ""
    
    update_context("research", research_data)
    print(f"[RESEARCHER] Research phase complete. Gathered information for {len(research_data)} chapters.")
