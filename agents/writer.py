"""
Writer Agent
Responsible for drafting content for each chapter using research data.
"""

import requests
from shared.context import context, update_context

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def run_writer():
    """
    Write full drafts for each chapter using the research data.
    """
    print("[WRITER] Starting writing phase...")
    
    chapters = context.get("chapters", [])
    research = context.get("research", {})
    drafts = []
    
    if not chapters:
        print("[WRITER] No chapters found in context. Skipping writing.")
        return
    
    for i, chapter in enumerate(chapters, 1):
        print(f"[WRITER] Writing chapter {i}/{len(chapters)}: {chapter}")
        
        research_content = research.get(chapter, "No research available.")
        
        prompt = f"""Write a comprehensive and engaging chapter for a book with the following details:

Chapter Title: {chapter}

Background Research:
{research_content}

Please write a well-structured chapter (500-800 words) that incorporates the research, 
flows well, and maintains a professional tone suitable for a book on AI and technology."""
        
        try:
            response = requests.post(OLLAMA_API_URL, json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            })
            
            if response.status_code == 200:
                draft_content = response.json()["response"].strip()
                chapter_draft = f"# {chapter}\n\n{draft_content}\n\n"
                drafts.append(chapter_draft)
                print(f"[WRITER] Draft completed for: {chapter}")
            else:
                print(f"[WRITER] Error for chapter '{chapter}': {response.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("[WRITER] Error: Could not connect to Ollama. Make sure it's running on http://localhost:11434")
            break
        except Exception as e:
            print(f"[WRITER] Error writing '{chapter}': {str(e)}")
    
    update_context("drafts", drafts)
    print(f"[WRITER] Writing phase complete. Created {len(drafts)} chapter drafts.")
