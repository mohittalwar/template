# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Development

```sh
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"  # on VPN, add: --index-url https://pypi.apple.com/simple
pre-commit install
```

Run the app: `python3 src/main.py`
Run FastAPI dev server: `fastapi dev src/main.py`

## Testing

Run all tests: `pytest`
Run a single test: `pytest tests/test_utils.py::test_get_message`

## Linting

Pre-commit hooks run ruff (linting) and mypy (type checking) automatically on commit.
Run manually: `ruff check src/` and `mypy src/`

## Architecture

This is a FastAPI web app with deployment configured for Render (`render.yaml`).

- `src/main.py` — FastAPI app entry point with route handlers; imports from `utils` and `config`
- `src/utils.py` — Shared helper functions
- `src/config.py` — App settings via pydantic-settings `BaseSettings` (reads env vars with defaults)
- `tests/` — pytest tests; `test_utils.py` for unit tests, `test_main.py` for API endpoint tests
- `notebooks/` — Jupyter notebooks
- `pyproject.toml` — Package config, dependencies, and tooling settings
- `.env.example` — Documented environment variables
