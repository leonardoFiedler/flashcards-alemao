.PHONY: init up down alembic_upgrade_head format

init:
	@uv venv .venv
	@uv sync --frozen

up:
	@docker compose up -d

down:
	@docker compose down

alembic_upgrade_head:
	cd backend && alembic upgrade head

format:
	@ruff format
	@ruff check --fix