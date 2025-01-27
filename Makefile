install:
	uv sync

upgrade:
	uv sync --upgrade

package-remove:
	python3 -m pip uninstall hexlet_code

build:
	uv build

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*whl

gendiff:
	uv run gendiff

lint:
	uv run flake8 gendiff

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

tests:
	uv run pytest -vv
