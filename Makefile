.PHONY: install check build test

install:
	python -m pip install -r requirements.lock
	python -m pip install --no-deps -e .

check:
	sztu-connect check --json

build:
	sztu-connect build --json

test:
	python -m unittest discover -s tests
