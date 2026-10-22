# Aster Assistant — MVP

Aster is a user-controlled assistant scaffold, not a continuously running instance of ChatGPT.

## Architecture
- GitHub: versioned code, prompts, tests, and public-safe continuity.
- Google Drive: human-readable continuity and working documents.
- Local runtime: Python standard library CLI, optionally calling an OpenAI-compatible API when the user configures credentials.
- No autonomous external actions or automatic cross-service synchronization in this MVP.

## Start
1. Clone this repository.
2. Run `python APP/aster.py` for offline continuity inspection.
3. Optionally set `OPENAI_API_KEY` and run `python APP/aster.py --chat` for model-backed chat (API usage may incur charges).
4. Update `CONTINUITY/MASTER_CONTEXT.md` and session records after verified decisions.

Do not commit secrets, private transcripts, or OAuth tokens. The Project-Aster repository is public as last verified.
