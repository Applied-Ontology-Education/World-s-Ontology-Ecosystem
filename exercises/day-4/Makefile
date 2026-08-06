.DEFAULT_GOAL := run

.PHONY: install verify-setup test run

install:
	uv sync --frozen --dev

verify-setup:
	uv run --frozen python scripts/verify_ontology_files.py

test:
	uv run --frozen pytest \
		src/day4/workflows/StudentExerciseWorkflow_test.py -q

.env:
	touch .env

run: install verify-setup .env
	uv run --frozen python main.py
