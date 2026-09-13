# CI/CD Tutorial — Python + GitHub Actions

A minimal project to learn continuous integration hands-on.

## What's here
```
ci-cd-tutorial/
├── src/calc/          # the code (add, divide)
├── tests/             # pytest tests
├── pyproject.toml     # project + tool config (pytest, ruff)
├── requirements-dev.txt
└── .github/workflows/ci.yml   # the CI pipeline
```

## Run the checks locally (same ones CI runs)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements-dev.txt
ruff check .
pytest --cov=calc
```

If those pass locally, they pass in CI — that's the whole point.

## Push it to GitHub
```bash
git init
git add .
git commit -m "Initial commit: calc + CI pipeline"
git branch -M main
git remote add origin https://github.com/<you>/ci-cd-tutorial.git
git push -u origin main
```
Open the repo's **Actions** tab to watch the pipeline run.
