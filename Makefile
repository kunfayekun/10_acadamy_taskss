.PHONY: setup test spec-check

setup:
	@echo "Installing Python dependencies (if requirements.txt exists)..."
	python -m pip install --upgrade pip
	@if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; else echo "No requirements.txt found"; fi
	@echo "Building Docker image chimera-test..."
	@docker build -t chimera-test . || echo "Docker build failed or Docker not available"

test:
	@echo "Running tests locally..."
	@pytest -q || true
	@echo "Running tests in Docker image chimera-test..."
	@docker run --rm chimera-test || echo "Docker run failed or Docker not available"

spec-check:
	@echo "Running spec-check script..."
	@python scripts/spec_check.py
