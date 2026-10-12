#!/bin/bash

# Create a virtual environment using uv
uv venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install all dependencies using uv
uv pip install -e .
uv pip install pytest

# Install pre-commit hooks
pre-commit install
