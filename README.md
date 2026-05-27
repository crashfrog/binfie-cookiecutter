# Binfie Project Cookiecutter

A stripped-down Python project cookiecutter for the stuff I usually do. Updated for 2026.

1) Installs `click` (optional)
2) Puts in a useful Makefile (`make help`)
3) Dockerfile + Singularity/Apptainer definition for HPC clusters
4) `pixi.toml` for reproducible Bioconda environments
5) Optional workflow stubs for Nextflow, WDL, CWL, and Snakemake
6) GitHub Actions that run tests and build containers
7) README, LICENSE, CONTRIBUTING, CODE-OF-CONDUCT — develop in the open from day one
8) Overthrow the tyranny of the blank page with stubs for documentation

## Usage

    pip install cookiecutter
    cookiecutter gh:crashfrog/binfie-cookiecutter

Now you have a bioinformatics project. Shell into the directory and run `make help`.

1. Install cookiecutter: `pip install cookiecutter`
2. Run the cookiecutter: `cookiecutter gh:crashfrog/binfie-cookiecutter`
3. `cd` to the new project directory, make your first git commit, tag the commit (a prompt suggests you do this)
4. Run `make dev` to install the project in an editable, testable dev mode — or `make sync` if you use uv
5. Run `make help` to see all the options. Also read the `Makefile` itself!

## Names

Pick a good name! Binfie-cookiecutter checks PyPI, Bioconda, and Galaxy (IUC Toolshed) for name collisions before generating anything. Turn this off with `__name_check=false` if you're working offline or just want to go fast.

## Packaging and Distribution

Binfie-cookiecutter uses `pyproject.toml` (with `setuptools-scm` for version-from-git-tag) and sets your project up for:

1. **PyPI** — `make dist` builds a wheel; `make release` uploads it with twine
2. **Bioconda** — the conda `environment.yml` is your recipe starting point
3. **Docker** — multi-stage Dockerfile produces a `runtime` image and a `galaxy` image (the latter drops you to bash for Galaxy tool integration); `make container` builds both
4. **Apptainer/Singularity** — `Singularity.def` bootstraps from the same Debian base as the Dockerfile; `make sif` builds the `.sif` for HPC clusters where Docker isn't allowed
5. **uv** — `make sync` and `make lock` for users of the [uv](https://docs.astral.sh/uv/) package manager (no config changes required — uv reads `pyproject.toml` as-is)

## Pixi

Every generated project includes a `pixi.toml` wired to the `conda-forge` and `bioconda` channels. [Pixi](https://pixi.sh) gives you reproducible, cross-platform conda environments with a lockfile — think "cargo for conda." If you have non-Python dependencies (samtools, bedtools, blast...), add them to the `[dependencies]` table. If you don't use Pixi, ignore the file.

    pixi install          # set up the environment
    pixi run test         # run pytest inside it
    pixi run lint         # ruff check

## Workflows

Binfie-cookiecutter optionally generates stubs for Nextflow, WDL, CWL, and Snakemake. Pick one at generation time; the appropriate runtime dependency is added to `pyproject.toml` and `pixi.toml` automatically.

## Actions and Tests

Two CI jobs ship with every project:

- **Test** — runs `pytest` on push/PR via a conda environment
- **Docker** — builds and pushes the `runtime` and `galaxy` container images on release
