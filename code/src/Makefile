# Define variables
VENV=venv
PYTHON=$(VENV)/bin/python
UVICORN=uvicorn
DOCKER_IMAGE=my-fastapi-app

# Create a virtual environment
venv:
	python3 -m venv $(VENV)

# Install dependencies
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-dev.txt

# Run FastAPI server
run: install
	$(UVICORN) main:app --host 0.0.0.0 --port 8000 --reload

# Run tests
test:
	pytest tests/

# Format code using Black
format:
	black .

# Lint code using flake8
lint:
	flake8 .

# Type checking using mypy
type-check:
	mypy .

# Clean up build, cache, and temporary files
clean:
	@echo "Cleaning up..."
	@rm -rf __pycache__ .pytest_cache .mypy_cache dist build *.egg-info || true

# Build the Python package
build: clean
	python -m build || true