# Constants
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python3
ENV_FILE = .env
PACKAGE_DIR = package
ACTIVATE = . $(VENV)/bin/activate &&
DOCS_DIR = docs
DOCS_BUILD_DIR = $(DOCS_DIR)/_build
DOCS_SOURCE_DIR = $(DOCS_DIR)/_source

# Helper Functions
define find_commands
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/## //' | sed -e 's/^/  /'
endef

# Check if virtual environment exists
_is_venv:
	@if [ ! -d "$(VENV)" ]; then \
		echo "There is no $(VENV), please run 'make init'."; \
		exit 1; \
	fi

# Help target to list available commands
help:
	@echo "Please use 'make <target>' where <target> is one of :"
	@$(call find_commands)
	@echo "Check the Makefile to know exactly what each target is doing."

# Initialize development environment
init: ## sets up environment in development mode
init:
	python3 -m venv $(VENV)
	$(ACTIVATE) $(PIP) install .[dev]

# Run the Package
run: ## run the package
run: _is_venv
	$(ACTIVATE) $(PYTHON) -m $(PACKAGE_DIR).app

# Test the package
test: ## test the package
test: _is_venv
	$(ACTIVATE) ($(PYTHON) -m pytest $(PACKAGE_DIR) || true)

# Lint typing and other errors
lint: ## test typing and other errors
lint: _is_venv
	$(ACTIVATE) ($(PYTHON) -m flake8 $(PACKAGE_DIR) || true)
	$(ACTIVATE) ($(PYTHON) -m mypy $(PACKAGE_DIR) --follow-imports=skip --strict || true)

# Build the project
build: ## build the project
build: _is_venv
	$(ACTIVATE) $(PYTHON) -m build

# Clean up unnecessary files
clean: ## removes all unnecessary files
clean:
	@echo "Removing $(VENV) folder..."
	@rm -rf $(VENV)
	@echo "Removing files and directories listed in .gitignore..."
	@grep -v '^#' .gitignore | grep -v '^$$' | while read pattern; do \
		rm -rf $$pattern; \
		if [ "$${pattern%/}" != "$$pattern" ]; then \
			dir_pattern="$${pattern%/}"; \
			echo "Removing directory: $$dir_pattern"; \
			find . -type d -name "$$dir_pattern" -exec rm -rf {} +; \
		else \
			echo "Removing file: $$pattern"; \
			find . -name "$$pattern" -exec rm -f {} +; \
		fi \
	done

# Generate documentation using Sphinx
docs: ## Generate documentation using Sphinx
docs: _is_venv
	$(ACTIVATE) sphinx-build -b html $(DOCS_SOURCE_DIR) $(DOCS_BUILD_DIR)/html

# Mark targets as phony to avoid conflicts with files named 'help', 'init', etc.
.PHONY: help init run test lint build clean docs
