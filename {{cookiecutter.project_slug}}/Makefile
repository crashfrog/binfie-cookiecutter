.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

install-test: clean ## install the package to the active Python's site-packages
	python -m pip install .[test]

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: install-test ## check style with flake8
	flake8 {{ cookiecutter.project_slug }} tests

test: install-test ## run tests quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	pytest
{%- else %}
	python setup.py test
{%- endif %}

test-all: install-test ## run tests on every Python version with tox
	tox

coverage: install-test ## check code coverage quickly with the default Python
{%- if cookiecutter.use_pytest == 'y' %}
	coverage run --source {{ cookiecutter.project_slug }} -m pytest
{%- else %}
	coverage run --source {{ cookiecutter.project_slug }} setup.py test
{%- endif %}
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

docs: dev ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.project_slug }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: dev docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

revise: dev ## update version, tag, and history using zest.releaser
	prerelease

release: dist ## package and upload a release
	twine upload dist/*

dist: dev clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

# Not sure if this is the right approach

install: clean ## install the package to the active Python's site-packages
	python -m pip install .

dev: clean ## install the dev dependencies and install in edit mode
	python -m pip install -e .[dev]

container: ## create the latest version of the container image
	docker build -t {{cookiecutter.github_username}}/{{ cookiecutter.project_slug }}:latest .
