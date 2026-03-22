# Python Project Template

A batteries-included template for Python web service projects.

## What's Included

**Web framework**
- [FastAPI](https://fastapi.tiangolo.com/) with [uvicorn](https://www.uvicorn.org/) — async API routes with automatic OpenAPI docs
- [pydantic-settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) — typed config via environment variables

**Testing**
- [pytest](https://pytest.org/) with [pytest-cov](https://pytest-cov.readthedocs.io/) — 100% coverage enforced on every run
- [httpx](https://www.python-httpx.org/) — async-compatible test client for FastAPI endpoints

**Linting & formatting** (run automatically on commit via [pre-commit](https://pre-commit.com/))
- [ruff](https://docs.astral.sh/ruff/) — fast linter (replaces flake8, isort, and more)
- [ruff-format](https://docs.astral.sh/ruff/formatter/) — opinionated formatter (replaces Black)
- [mypy](https://mypy.readthedocs.io/) — strict static type checking
- Standard hooks: trailing whitespace, end-of-file newline, YAML/JSON validation, merge conflict detection, private key detection

**Package management**
- [uv](https://docs.astral.sh/uv/) — fast dependency installation

**Deployment**
- [Render](https://render.com/) — `render.yaml` preconfigured for a free-tier Python web service

## Structure

- `src/main.py`: FastAPI app entry point with API routes.
- `src/utils.py`: Shared helper functions.
- `src/config.py`: App settings via pydantic-settings (reads env vars).
- `tests/`: pytest tests for utilities and API endpoints.
- `notebooks/`: Jupyter notebooks.
- `.pre-commit-config.yaml`: Pre-commit hooks (ruff, ruff-format, mypy).
- `pyproject.toml`: Package and dependency configuration.
- `render.yaml`: Deployment configuration for Render.
- `.env.example`: Documented environment variables.

## Usage

1. To setup and test the development enviroment:
```sh
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"  # on VPN, add: --index-url https://pypi.apple.com/simple
pre-commit install
pytest
```

2. To run the main script:
```sh
python3 src/main.py
```

3. To deploy the web app locally:
```sh
fastapi dev src/main.py
```

4. To deploy the web app on Render, see https://render.com/docs/deploy-fastapi
