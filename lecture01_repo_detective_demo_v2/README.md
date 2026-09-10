# Lecture 01 — Repo Detective Demo v2

Учебный репозиторий для первой лекции.

Показывает:
- `pyproject.toml`;
- `src`-layout;
- `python -m pip install -e ".[dev]"`;
- `uv sync`, `uv run`, `uv tree`;
- `__init__.py`, `__main__.py`, `__name__`, `__all__`;
- прямой запуск `.py` файла vs запуск модуля через `python -m`;
- `sys.path`, `find_spec`, `sys.modules`;
- shadowing: локальный `requests.py`;
- чтение dependency conflicts;
- путь `CLI -> service -> classifier -> test`.

## pip

```bash
python -m venv .venv
source .venv/bin/activate  # or Windows: .\.venv\Scripts\activate.ps1
python -m pip install -e ".[dev]"
python -m repo_detective_demo --help
python -m repo_detective_demo classify "I want my money back"
python -m pytest -q
```

## uv

```bash
uv sync
uv run repo-demo classify "I want my money back"
uv run pytest -q
uv tree
```

## import labs

```bash
cd examples/run_file_vs_module
python pkg/tool.py
python -m pkg.tool

cd ../import_shadowing
python app.py

cd ../import_cache
python demo.py
```

## conflict lab

```bash
cd examples/dependency_conflicts
python -m pip install -e ".\packages\pkg_alpha" -e ".\packages\pkg_beta"   
python read_conflict.py sample_pip_resolution_error.txt
```
