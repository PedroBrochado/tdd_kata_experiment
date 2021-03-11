SHELL=/bin/bash

clean:
	rm -rf venv

install:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

test:
	PYTHONPATH=src venv/bin/pytest  tests
