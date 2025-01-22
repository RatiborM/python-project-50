install:
	uv sync

gendiff:
	uv run gendiff files/file1.json files/file2.json

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

selfcheck:
	uv check

check:
	test lint

reinstall:
	pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build