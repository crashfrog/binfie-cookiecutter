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

init: ## initialize and pull any submodules
	git submodule init
	git submodule update

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

lint: dev ## check style with flake8
	flake8 --extend-ignore=E266,E203,W503,E303,F401,F302 {{ cookiecutter.pkg_name }}

test: install-test ## run tests quickly with the default Python
	pytest

coverage: clean-test install install-test dev ## check code coverage quickly with the default Python
	coverage run --source {{ cookiecutter.pkg_name }} -m pytest
	coverage report -m --include={{ cookiecutter.pkg_name }}/*

docs: dev ## generate Sphinx HTML documentation, including API docs
	rm -f docs/{{ cookiecutter.__project_slug }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.pkg_name }}

servedocs: dev docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

revise: dev ## update version, tag, and history using zest.releaser
	prerelease

release: dev dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

# Not sure if this is the right approach

install: clean ## install the package to the active Python's site-packages
	python -m pip install .

dev: clean ## install the dev dependencies and install in edit mode
	python -m pip install -e .[dev]

container: ## create the latest version of the container image
	docker build -t {{cookiecutter.github_username}}/{{ cookiecutter.__project_slug }}:latest .
