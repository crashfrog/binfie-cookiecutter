# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for bioinformatics Python projects. Running `cookiecutter gh:crashfrog/binfie-cookiecutter` generates a new project directory. This repo is the *template*, not a runnable project itself.

## Testing the template

```bash
pip install cookiecutter
# Generate a test project (no interactive prompts):
cookiecutter . --no-input -o /tmp full_name="Test User" email="test@test.com" github_username="testuser" project_name="My Test Project"
# Run its tests:
cd /tmp/my_test_project && make test
# Build its Docker image:
docker build . --file Dockerfile --tag mytestproject:test
```

The CI workflow (`test_the_template.yml`) tests all license variants and all workflow languages in a matrix.

## Template structure

- `cookiecutter.json` — all template variables. Private vars (prefixed `__`) are computed from user input via Jinja filters and never prompted.
- `{{cookiecutter.__project_slug}}/` — the output project directory; everything inside is rendered by Jinja2.
- `hooks/pre_gen_project.sh` — runs before generation; checks PyPI, Bioconda, and Galaxy Toolshed for name collisions (skipped if `__name_check=false`).
- `hooks/post_gen_project.sh` — runs after generation; creates optional workflow stubs (Nextflow/Snakemake/WDL/CWL), runs `git init`, and prints first-steps instructions.

## Key template variables

| Variable | Source | Purpose |
|---|---|---|
| `project_name` | user input | Human-readable name |
| `__project_slug` | `project_name` lowercased, spaces/hyphens→`_` | Directory name and import path |
| `pkg_name` | `__project_slug` with vowels stripped | PyPI package name (shorter) |
| `project_shell_cmd` | `__project_slug` consonants only | CLI entry point name; set to `""` to skip Click/CLI entirely |
| `wf_lang` | choice: null/Nextflow/Snakemake/WDL/CWL | Controls which workflow stub is generated and which deps are added |

## Generated project layout

- `pyproject.toml` — build config using `setuptools` + `setuptools_scm` (version from git tags). Click is a dependency only when `project_shell_cmd` is non-empty.
- `Dockerfile` — multi-stage: `build` (miniconda3 + conda-pack), `runtime` (debian:bookworm + packed venv), `galaxy` (runtime + bash entrypoint for Galaxy tool integration).
- `Makefile` — primary dev interface. Key targets: `make dev`, `make test`, `make lint`, `make dist`, `make release`, `make container`.
- `.github/workflows/test_*.yml` — runs pytest via conda env on push/PR.
- `.github/workflows/build_*_docker.yml` — builds and pushes both `runtime` and `galaxy` Docker targets on GitHub release.
- `environment.yml` — conda env definition (bioconda + conda-forge channels); dependencies are a TODO stub for the generated project.

## Jinja2 in GitHub Actions workflows

GitHub Actions syntax (`${{ }}`) conflicts with Jinja2. The template uses `$\{\{ \}\}` escapes or `{% raw %}...{% endraw %}` blocks around Actions expressions. When editing workflow templates, preserve these escapes carefully.

## Name collision check logic

`pre_gen_project.sh` queries:
1. `https://pypi.org/pypi/<pkg_name>/json` — 200 = collision
2. `https://bioconda.github.io/recipes/<pkg_name>/README.html` — 200 = collision
3. `https://toolshed.g2.bx.psu.edu/view/<pkg_name>` — absence of "contains no repositories" = collision
