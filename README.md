# Multi-Agent Book Writer

A collaborative AI book writing system using multiple specialized agents. Each agent has a specific role in the writing pipeline to create a complete, polished book draft.


<img src="/images/writer.gif" alt="description" style="width:100%; height:auto;" />
## Project Overview

This project simulates a writing team of AI agents that co-author a book. Each agent has a distinct role:

- **Planner**: Defines the book structure and chapters
- **Researcher**: Gathers background information and supporting content
- **Writer**: Drafts content for each chapter
- **Editor**: Reviews and polishes the output for grammar and coherence

The agents communicate through shared memory, enabling seamless collaboration.

## Tech Stack

| Component | Tool/Library |
|-----------|-------------|
| LLMs | Ollama (mistral, llama3, deepseek) |
| Agent Orchestration | Python classes with sequential pipeline |
| Context Sharing | In-memory Python objects |
| HTTP Client | requests library |
| Configuration | YAML |

## Project Structure

```
multiagent-book-writer/
├── main.py                 # Main pipeline orchestrator
├── agents/                 # Agent implementations
│   ├── planner.py         # Chapter planning agent
│   ├── researcher.py      # Research gathering agent
│   ├── writer.py          # Content writing agent
│   └── editor.py          # Content editing agent
├── shared/
│   └── context.py         # Shared state management
├── output/
│   └── draft.txt          # Final output (generated)
├── config.yaml            # Configuration file
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Installation

### Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running

### Setup Steps

1. **Clone or download the project**
   ```bash
   cd c:\Users\Dell\Downloads\Multi-Agent Book Writer
   ```

2. **Pull an LLM model with Ollama**
   ```bash
   ollama pull mistral
   # Alternative options: ollama pull llama3, ollama pull deepseek
   ```

3. **Start Ollama** (keep it running in a separate terminal)
   ```bash
   ollama serve
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Execution

Run the complete pipeline:
```bash
python main.py
```

Generate a book with a specific number of chapters:
```bash
python main.py 7
```

### Output

The final book draft is saved to `output/draft.txt` with:
- All chapters with proper formatting
- Edited and polished content
- Coherent flow and consistency

## How It Works

### Pipeline Flow

1. **Planning Phase**: Planner agent creates a structured outline with chapter titles and descriptions
2. **Research Phase**: Researcher agent gathers background information, facts, and context for each chapter
3. **Writing Phase**: Writer agent creates full chapter drafts based on research data
4. **Editing Phase**: Editor agent polishes chapters for grammar, clarity, and coherence
5. **Output**: Final draft is saved to `output/draft.txt`

### Agent Communication

All agents share a central `context` dictionary that includes:
- `title`: Book title
- `chapters`: List of chapter titles and descriptions
- `research`: Dictionary of research data per chapter
- `drafts`: List of chapter drafts

## Configuration

Edit `config.yaml` to customize:

- **Book settings**: Title, number of chapters, output format
- **Ollama settings**: API URL, model selection, timeout
- **Agent parameters**: Temperature and behavior for each agent
- **Output settings**: Directory and filename preferences

## Examples

### Run with 3 chapters:
```bash
python main.py 3
```

### Check the output:
```bash
type output\draft.txt
```

## Troubleshooting

### Connection Error to Ollama
- Make sure Ollama is running: `ollama serve`
- Verify it's accessible at `http://localhost:11434`
- Check firewall settings

### Out of Memory
- Try a smaller model: `ollama pull orca-mini`
- Reduce chapter count: `python main.py 2`

### Slow Generation
- Check if Ollama is using GPU: `ollama list --all`
- Consider using a smaller, faster model

## Extensions & Improvements

Potential enhancements to explore:

- [ ] Add LangGraph for advanced orchestration with retries
- [ ] Implement feedback loops for iterative refinement
- [ ] Build Streamlit UI for real-time monitoring
- [ ] Add PDF export functionality
- [ ] Integrate with web search APIs for richer research
- [ ] Add support for multiple LLMs
- [ ] Implement memory persistence (JSON/database)
- [ ] Add custom style guides for writing consistency

## Requirements

See `requirements.txt`:
- `requests`: HTTP library for Ollama API calls
- `ollama`: Ollama Python client library
- `python-dotenv`: Environment variable management (optional)

## License

This project is open source and available for educational and commercial use.

## Notes

- Ollama must be running locally for this project to work
- Generated content quality depends on the selected LLM model
- Generation time depends on model size and hardware capabilities
- All content is generated in-memory before being written to disk

---

**Getting Started**: Install dependencies, start Ollama, and run `python main.py` to generate your first AI-written book!


