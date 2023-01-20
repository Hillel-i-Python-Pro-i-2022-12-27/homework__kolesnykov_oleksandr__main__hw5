.PHONY: init-dev

init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: homework-i-run

homework-i-run:
	@python main.py

.PHONY: homework-i-purge

homework-i-purge:
	@echo Goodbye!

.PHONY: pre-commit-run

pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all

pre-commit-run-all:
	@pre-commit run --all-files