.PHONY: build install-dev test clean

build:
	python -m build

install-dev:
	pip install -e .[dev]

test: install-dev
	pytest tests/

clean:
	powershell -Command "Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue; Get-ChildItem -Recurse -Directory __pycache__ | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue; exit 0"