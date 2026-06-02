# Install UV using powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"


# Create a project (makes pyproject.toml + .venv)
uv init fastapi-app
cd fastapi-app
# Add dependencies (writes to pyproject.toml + lockfile)
uv add "fastapi[standard]" # FastAPI + uvicorn + CLI + extras
uv add sqlalchemy alembic asyncpg # DB stack (later modules)
uv add "passlib[bcrypt]" pyjwt # auth (later)
# Dev-only dependencies
uv add --dev ruff mypy pytest httpx
# Run any command inside the venv
uv run python -V
uv run fastapi dev main.py
