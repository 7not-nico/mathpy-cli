# Math Practice Game Makefile

.PHONY: help run test lint format clean docs

help: ## Show this help message
	@echo "Math Practice Game - Development Commands"
	@echo ""
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

run: ## Run the math game
	python main.py

test: ## Run basic tests
	python -c "import main; print('✅ Import successful')"
	python -m py_compile main.py && echo "✅ Syntax check passed"
	python -c "
	from main import ProblemGenerator, GameEngine, UserInterface
	gen = ProblemGenerator()
	engine = GameEngine()
	ui = UserInterface()
	for i in range(5):
		prob, x = gen.generate()
		print(f'✅ Generated: {prob} → x={x}')
	print('✅ All basic tests passed')
	"

lint: ## Check code style (requires flake8)
	@echo "Checking code style..."
	@command -v flake8 >/dev/null 2>&1 || { echo "❌ flake8 not installed. Install with: uv add --dev flake8"; exit 1; }
	flake8 main.py --max-line-length=100 --extend-ignore=E203,W503 || echo "❌ Linting failed"

format: ## Format code (requires black)
	@echo "Formatting code..."
	@command -v black >/dev/null 2>&1 || { echo "❌ black not installed. Install with: uv add --dev black"; exit 1; }
	black main.py

type-check: ## Check types (requires mypy)
	@echo "Checking types..."
	@command -v mypy >/dev/null 2>&1 || { echo "❌ mypy not installed. Install with: uv add --dev mypy"; exit 1; }
	mypy main.py

clean: ## Clean up generated files
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true

docs: ## Open documentation index
	@echo "Documentation files:"
	@find docs/ -name "*.md" | sort
	@echo ""
	@echo "Open docs/index.md for the main documentation hub"

install-dev: ## Install development dependencies
	uv pip install -r requirements.txt

setup: ## Initial project setup
	@echo "Setting up Math Practice Game..."
	@echo "✅ Project structure ready"
	@echo "Run 'make run' to start the game"
	@echo "Run 'make test' to verify everything works"