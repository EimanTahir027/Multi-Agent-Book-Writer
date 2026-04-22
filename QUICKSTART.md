# Multi-Agent Book Writer - Quick Start Guide

## Overview
This is a multi-agent AI system that collaboratively writes books using local LLMs via Ollama.

## Quick Setup (5 minutes)

### 1. Install Ollama
Download from https://ollama.ai

### 2. Pull a Model
```bash
ollama pull mistral
```

### 3. Start Ollama Server
```bash
ollama serve
```
Keep this terminal open!

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Project
```bash
python main.py
```

## Command Examples

- **Generate 5 chapters** (default): `python main.py`
- **Generate 3 chapters**: `python main.py 3`
- **View output**: `type output\draft.txt` (Windows) or `cat output/draft.txt` (Mac/Linux)

## Project Structure

```
agents/          → Individual agent implementations
shared/          → Shared context and utilities
output/          → Generated book files
config.yaml      → Configuration settings
main.py          → Main pipeline entry point
requirements.txt → Dependencies
```

## Agents

1. **Planner** - Creates chapter structure
2. **Researcher** - Gathers background information
3. **Writer** - Writes chapter content
4. **Editor** - Polishes and edits drafts

## Troubleshooting

**Error: Connection refused**
- Make sure `ollama serve` is running in another terminal

**Slow generation**
- Use a faster model: `ollama pull orca-mini`
- Reduce chapter count: `python main.py 2`

**Out of memory**
- Try a smaller model
- Close other applications
- Reduce chapter count

## Output

Your finished book is saved in `output/draft.txt` with:
- ✓ Complete chapters
- ✓ Proper formatting
- ✓ Edited and polished content
- ✓ Professional formatting

---

For detailed documentation, see README.md
