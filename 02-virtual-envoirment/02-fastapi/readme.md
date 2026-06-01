# Quick Refrences How to run fastapi
Task            | Command
Create venv     | python -m venv .venv
Activate        | ./.venv/Scripts/active
Install         | pip install "fastapi[standard]"
Dev server      | fastapi dev main.py
Production      | fastapi run main.py
docs            | http://127.0.0.1:8000/docs
Save deps       | pip freeze > requirements.txt
Run tests       | pytest -v