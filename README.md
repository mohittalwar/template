# Python Project Template

This is a template for Python projects.

## Structure

- `notebooks/`: Jupyter notebooks directory.
- `src/`: Source directory.
- `tests/`: Test directory.
- `.gitignore`: Git ignore file.
- `.pre-commit-config.yaml`: Pre-commit hooks configuration.
- `LICENSE`: License for the project.
- `README.md`: Project description and instructions.
- `render.yaml`: Deployment configuration for Render.
- `setup.py`: Script for installing the package and its depedencies.

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
