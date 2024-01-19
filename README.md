# Binfie Project Cookiecutter

A stripped-down Python project cookiecutter for the stuff I usually do. Updated for 2024.


2) Installs `click`
3) Puts in a useful Makefile (`make help`)
4) Dockerfile
5) Github actions that run tests

## Usage

    pip install cookiecutter
    cookiecutter gh:crashfrog/binfie-cookiecutter

Now you have a bioinformatics project. Shell into the directory and run `make help`.

Future:

1) Checks PyPI, Bioconda, and Galaxy for project name collision

Usage:

1) Run the cookiecutter: `cookiecutter gh:crashfrog/binfie-cookiecutter`

2) cd to the new project directory, make your first git commit, tag the commit (a prompt suggests you do this)

3) Optionally, create a virtualenv

4) Run `make dev` to install the project in an editable, testable dev mode

5) Run `make help` to see some other options. Also read the `Makefile` itself!