# Python Project Template

This is a template for Python projects.

## Structure

- `src/`: Source directory.
- `tests/`: Test directory.
- `notebooks/`: Jupyter notebooks directory.
- `.gitignore`: Git ignore file.
- `.pre-commit-config.yaml`: Pre-commit hooks configuration.
- `LICENSE`: License for your project.
- `README.md`: Project description and instructions.
- `render.yaml`: Deployment configuration for Render.
- `requirements.txt`: List of dependencies.
- `setup.py`: Script for installing the package.

## Usage

1. To setup and test the development enviroment:
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
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
