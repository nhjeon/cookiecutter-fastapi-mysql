init:
	pip install poetry
	poetry install --no-dev

check:
	poetry run black -S -l 79 --check app
	poetry run pylint app

format:
	poetry run black -S -l 79 app

run:
	PYTHONPATH=./app poetry run uvicorn main:app --reload

pytest:
	PYTHONPATH=./app poetry run python -m pytest

coverage:
	PYTHONPATH=./app poetry run python -m pytest ./test --cov app --cov-report term --cov-report xml

htmlcov:
	PYTHONPATH=./app poetry run python -m pytest --cov app --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html
