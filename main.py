"""
Main Pipeline
Orchestrates the multi-agent book writing workflow.
"""

from agents.planner import run_planner
from agents.researcher import run_researcher
from agents.writer import run_writer
from agents.editor import run_editor
from shared.context import get_context
import time

def run_pipeline(num_chapters=5):
    """
    Execute the complete book writing pipeline.
    
    Args:
        num_chapters: Number of chapters to generate
    """
    print("=" * 60)
    print("MULTI-AGENT BOOK WRITER")
    print("=" * 60)
    print()
    
    start_time = time.time()
    
    try:
        # Step 1: Planning Phase
        print("\n[PIPELINE] Step 1: Planning Phase")
        print("-" * 60)
        chapters = run_planner(num_chapters)
        if not chapters:
            print("[PIPELINE] Planning failed. Exiting.")
            return
        
        # Step 2: Research Phase
        print("\n[PIPELINE] Step 2: Research Phase")
        print("-" * 60)
        run_researcher()
        
        # Step 3: Writing Phase
        print("\n[PIPELINE] Step 3: Writing Phase")
        print("-" * 60)
        run_writer()
        
        # Step 4: Editing Phase
        print("\n[PIPELINE] Step 4: Editing Phase")
        print("-" * 60)
        run_editor()
        
        # Summary
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        context = get_context()
        print("\n" + "=" * 60)
        print("PIPELINE COMPLETE!")
        print("=" * 60)
        print(f"Title: {context['title']}")
        print(f"Chapters: {len(context['chapters'])}")
        print(f"Total time: {elapsed_time:.2f} seconds")
        print(f"Output: output/draft.txt")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n[PIPELINE] Error: {str(e)}")
        raise

if __name__ == "__main__":
    import sys
    
    # Get number of chapters from command line or use default
    num_chapters = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    
    run_pipeline(num_chapters)
    print("\n✓ Book written! Check output/draft.txt")
