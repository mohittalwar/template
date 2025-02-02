from setuptools import find_packages, setup

setup(
    name="template",
    description="A template python package.",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "fastapi[all]",
        "uvicorn",
    ],
    extras_require={
        "dev": [
            "ipykernel",
            "mypy",
            "pre-commit",
            "pytest",
            "ruff",
        ],
    },
)
