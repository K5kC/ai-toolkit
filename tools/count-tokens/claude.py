# /// script
# requires-python = ">=3.9"
# dependencies = ["anthropic", "python-dotenv"]
# ///
"""Count tokens for Claude models via the Anthropic API.

Claude's tokenizer isn't published, so this makes a count_tokens API call.
The call is free (no token charges) but still needs an API key to authenticate.

    cp .env.example .env        # then paste in your key
    uv run tools/count-tokens/claude.py
"""

import os

from dotenv import load_dotenv
import anthropic

load_dotenv()  # loads .env from this folder or a parent

if not os.getenv("ANTHROPIC_API_KEY"):
    raise SystemExit(
        "ANTHROPIC_API_KEY is not set.\n"
        "  1. cp .env.example .env\n"
        "  2. put a real key in .env (get one at console.anthropic.com -> API keys)\n"
        "  3. run this from the tools/count-tokens folder so .env is found"
    )

TEXT = "Large language models don't read words. They read tokens."

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

count = client.messages.count_tokens(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": TEXT}],
)

print(f"Naive word count: {len(TEXT.split())}")
print(f"Claude tokens:    {count.input_tokens}")
