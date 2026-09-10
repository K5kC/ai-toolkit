# /// script
# requires-python = ">=3.9"
# dependencies = ["tiktoken"]
# ///
"""Count tokens for OpenAI models with tiktoken.

OpenAI open-sources its tokenizer, so this runs locally — no API call, no
key. Newer models (gpt-4o, gpt-4.1, o-series) use the o200k_base encoding.

Note: a real chat request also adds a few tokens of per-message overhead
(role markers, etc.). This counts the raw text, which is what you want for
a quick size/cost check.

    uv run tools/count-tokens/openai.py
"""

import tiktoken

TEXT = "Large language models don't read words. They read tokens."

encoding = tiktoken.encoding_for_model("gpt-4o")
tokens = encoding.encode(TEXT)

print(f"Naive word count: {len(TEXT.split())}")
print(f"OpenAI tokens:    {len(tokens)}")
