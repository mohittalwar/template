# Python Project Template

This is a template for Python projects.

## Structure

- `src/main.py`: FastAPI app entry point with API routes.
- `src/utils.py`: Shared helper functions.
- `src/config.py`: App settings via pydantic-settings (reads env vars).
- `tests/`: pytest tests for utilities and API endpoints.
- `notebooks/`: Jupyter notebooks.
- `.pre-commit-config.yaml`: Pre-commit hooks (ruff, mypy).
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
