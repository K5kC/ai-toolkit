# ai-toolkit — Claude Context

## Repo Purpose
Public GitHub repo of ready-to-use AI prompts, agents, and tools.
Companion resource for the @k5kc YouTube/TikTok/Instagram channel.
Viewers land here from video descriptions to grab copy-paste prompts.

## Structure
- `system-prompts/` — prompts by use case (productivity, coding, writing, etc.)
- `tools/` — short runnable code examples, one folder per topic
  (e.g. `tools/count-tokens/`), with per-provider files where it makes sense
  (`claude.py`, `openai.py`, `gemini.py`)
- Future: `agents/`, `workflows/`

## Prompt File Format
Each prompt file:
- H1 title
- ## Works With (ChatGPT / Claude / Gemini)
- ## Prompt (fenced code block)
- ## Best For (2-3 bullet use cases)
- ## Credit (if adapted from another source)

## Tool Folder Format
Each `tools/<topic>/` folder:
- `README.md` — H1 title, one-line hook, ## Works With, ## Run, ## Best For
  (mirrors the prompt format)
- one script per provider, kept short and copy-pasteable, with a docstring
  that lists the run steps
- run with `uv` — each script carries a PEP 723 inline `# /// script` block
  listing its deps, so `uv run <file>` needs no venv or pip
- API keys via `python-dotenv` + a committed `.env.example` (real `.env` is
  git-ignored)
- For Claude token counting use `messages.count_tokens` (never `tiktoken`);
  `tiktoken` is fine for OpenAI only.

## Git Workflow
- Commit and push directly to `main`. Do not create a branch or open a PR
  unless explicitly asked.
- Commit as the `k5kc-team` git identity (set in this repo's local git config),
  not a personal account.

## Audience
Non-technical users (copy-paste into ChatGPT Custom Instructions)
and developers (drop into API system role). Write for both.

## License
MIT

## Channel Links
YouTube/TikTok/Instagram/X: @k5kc_
