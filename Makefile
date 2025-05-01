.PHONY: init up down

init:
	@uv venv .venv
	@uv sync --frozen

up:
	@docker compose up -d

down:
	@docker compose down