install:
	uv sync

build:
	uv build

i:
	uv tool install .

uninstall:
	uv tool uninstall hexlet-code
	uv clean

re: uninstall i

#_______________________________________________________________________________Run

run:
	uv run python -m gendiff.scripts.gendiff

run-h:
	uv run python -m gendiff.scripts.gendiff -h

#_______________________________________________________________________________Test run

simple:
	gendiff tests/test_data/file1.json tests/test_data/file2.json

yml:
	gendiff tests/test_data/file1.yml tests/test_data/file2.yaml

nest:
	gendiff tests/test_data/file3.json tests/test_data/file4.json

nest-yaml:
	gendiff tests/test_data/file3.yaml tests/test_data/file4.json

empty:
	gendiff tests/test_data/empty.json tests/test_data/file4.json

plain:
	gendiff --format plain tests/test_data/file1.json tests/test_data/file2.json

plain2:
	gendiff --format plain tests/test_data/file3.json tests/test_data/file4.json

json:
	gendiff --format json tests/test_data/file3.json tests/test_data/file4.json

#_______________________________________________________________________________Lint

lint:
	uv run ruff check .

fix:
	uv run ruff check --fix

#_______________________________________________________________________________Tests

test:
	uv run pytest

test-vv:
	uv run pytest -vv

coverage:
	uv run pytest --cov=gendiff

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

check: test lint
