# Count Tokens

Count how many tokens a piece of text really uses — for Claude, ChatGPT, and Gemini.

Same sentence, three tokenizers, three different numbers. Models bill you and
cut off context by **tokens, not words**, so this is how you check real cost
and how close you are to a context limit.

## Works With

| File | Provider | How it counts | Needs a key? |
|---|---|---|---|
| `openai.py` | ChatGPT / OpenAI | `tiktoken`, runs on your machine | No |
| `claude.py` | Claude | `messages.count_tokens` API call | Yes* |
| `gemini.py` | Gemini | `models.count_tokens` API call | Yes* |

\* The call is **free** (no token charges), but Claude and Gemini don't ship a
local tokenizer, so the request still needs an API key to authenticate. Only
`openai.py` is fully offline.

Don't use `tiktoken` to estimate Claude or Gemini — it's OpenAI's tokenizer and
undercounts the others, more so on code and non-English text.

## Run

Uses [uv](https://docs.astral.sh/uv/) — each script declares its own
dependencies inline, so `uv run` installs them on the fly. No venv, no `pip`.

```bash
cd tools/count-tokens

uv run openai.py                    # works immediately, no key

cp .env.example .env                # paste your keys into .env
uv run claude.py
uv run gemini.py
```

Keys are read from `.env` via `python-dotenv`. `.env` is git-ignored.

## Best For

- Estimating API cost before you send a big prompt
- Checking whether a document fits a model's context window
- Showing why "word count" is the wrong unit for LLMs
