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

.PHONY: d-run

d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose up --build

.PHONY: d-purge

d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: d-stop
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 \
		docker-compose down

.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge
