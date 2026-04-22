"""
Editor Agent
Responsible for reviewing and polishing the drafts for grammar and coherence.
"""

import requests
from shared.context import context

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

def run_editor():
    """
    Edit and polish the draft chapters for grammar, coherence, and flow.
    """
    print("[EDITOR] Starting editing phase...")
    
    drafts = context.get("drafts", [])
    
    if not drafts:
        print("[EDITOR] No drafts found in context. Skipping editing.")
        return
    
    final_output = ""
    
    for i, draft in enumerate(drafts, 1):
        print(f"[EDITOR] Editing chapter {i}/{len(drafts)}...")
        
        prompt = f"""You are a professional editor. Review and improve the following chapter for:
1. Grammar and spelling
2. Clarity and coherence
3. Flow and readability
4. Consistency in tone
5. Proper formatting

Chapter to edit:
{draft}

Provide the edited version that maintains all the original content but with improved writing quality."""
        
        try:
            response = requests.post(OLLAMA_API_URL, json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            })
            
            if response.status_code == 200:
                edited_content = response.json()["response"].strip()
                final_output += edited_content + "\n\n"
                print(f"[EDITOR] Chapter {i} editing completed.")
            else:
                print(f"[EDITOR] Error editing chapter {i}: {response.status_code}")
                final_output += draft + "\n\n"
                
        except requests.exceptions.ConnectionError:
            print("[EDITOR] Error: Could not connect to Ollama. Make sure it's running on http://localhost:11434")
            final_output += draft + "\n\n"
        except Exception as e:
            print(f"[EDITOR] Error editing chapter {i}: {str(e)}")
            final_output += draft + "\n\n"
    
    # Write final output to file
    try:
        output_path = "output/draft.txt"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_output)
        print(f"[EDITOR] Final book saved to {output_path}")
        print("[EDITOR] Editing phase complete!")
        return final_output
    except Exception as e:
        print(f"[EDITOR] Error saving output: {str(e)}")
        return final_output
