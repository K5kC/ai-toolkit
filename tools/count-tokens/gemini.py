# /// script
# requires-python = ">=3.9"
# dependencies = ["google-genai", "python-dotenv"]
# ///
"""Count tokens for Gemini models via the Google GenAI API.

Like Claude, Gemini's tokenizer isn't local — this makes a count_tokens
call. The call is free (no token charges) but still needs an API key.

    cp .env.example .env        # then paste in your key
    uv run tools/count-tokens/gemini.py
"""

import os

from dotenv import load_dotenv
from google import genai

load_dotenv()  # loads .env from this folder or a parent

if not os.getenv("GEMINI_API_KEY"):
    raise SystemExit(
        "GEMINI_API_KEY is not set.\n"
        "  1. cp .env.example .env\n"
        "  2. put a real key in .env (get one at aistudio.google.com/apikey)\n"
        "  3. run this from the tools/count-tokens folder so .env is found"
    )

TEXT = "Large language models don't read words. They read tokens."

client = genai.Client()  # reads GEMINI_API_KEY from the environment

result = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents=TEXT,
)

print(f"Naive word count: {len(TEXT.split())}")
print(f"Gemini tokens:    {result.total_tokens}")
