# Shared context module for all agents
# This is the central data store that all agents use to communicate

context = {
    "title": "The Rise of Agentic AI",
    "chapters": [],
    "research": {},
    "drafts": [],
}

def reset_context():
    """Reset the context to initial state."""
    global context
    context = {
        "title": "The Rise of Agentic AI",
        "chapters": [],
        "research": {},
        "drafts": [],
    }

def update_context(key, value):
    """Update a specific key in the context."""
    context[key] = value

def get_context(key=None):
    """Get a specific key or the entire context."""
    if key:
        return context.get(key)
    return context
