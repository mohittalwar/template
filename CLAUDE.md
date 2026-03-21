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

- `src/main.py` — FastAPI app entry point; imports utilities from `src/utils.py`
- `src/utils.py` — Shared helper functions
- `tests/` — pytest tests; modules import from `src/` directly (e.g., `import utils`)
- `notebooks/` — Jupyter notebooks
- Source packages are configured via `setup.py` with `src/` as the package root
