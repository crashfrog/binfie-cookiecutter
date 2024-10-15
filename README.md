# Binfie Project Cookiecutter

A stripped-down Python project cookiecutter for the stuff I usually do. Updated for 2024.


2) Installs `click`
3) Puts in a useful Makefile (`make help`)
4) Dockerfile
4) Optional "get started" stubs for WDL, CWL, Nextflow, and Snakemake
5) Github actions that run tests
6) README, LICENSE, CONTRIBUTING, CODE-OF-CONDUCT - develop in the open from day one
7) Overthrow the tyrrany of the blank page with stubs for documentation

## Names

Pick a good name! Binfie-cookiecutter checks PyPI, Bioconda, and Galaxy (IUC Toolshed) for name collisions. (You can turn this off with `__name_check=false`.)

## Packaging

Binfie-cookiecutter uses pyproject.toml and sets your project up for:

1) Building wheels
2) Publishing to pypi.org
3) Building a conda package and providing a bioconda recipe
4) Building a Docker container

## Workflows

Binfie-cookiecutter optionally sets you up with stubs for Nextflow, WDL, CWL, and Snakemake.

## Actions and Tests

Binfie-cookiecutter sets up GitHub actions to automatically run your tests when you push commits, and to build your Docker container.

## Usage

    pip install cookiecutter
    cookiecutter gh:crashfrog/binfie-cookiecutter


Now you have a bioinformatics project. Shell into the directory and run `make help`.

Usage:

0) Install cookiecutter: `pip install cookiecutter`

1) Run the cookiecutter: `cookiecutter gh:crashfrog/binfie-cookiecutter`

2) cd to the new project directory, make your first git commit, tag the commit (a prompt suggests you do this)

3) Optionally, create a virtualenv

4) Run `make dev` to install the project in an editable, testable dev mode

5) Run `make help` to see some other options. Also read the `Makefile` itself!