import pytest

LICENSES = [
    "MIT license",
    "GNU General Public License v3",
    "Public domain",
    "US Government Work Product",
    "BSD license",
    "ISC license",
    "Apache Software License 2.0",
    "Not open source",
]

WF_LANGS = [None, "Nextflow", "Snakemake", "WDL", "CWL"]

# __project_slug for "My Cool Project" = my_cool_project
# pkg_name = mycoolproject (underscores stripped)
PKG_NAME = "mycoolproject"
PROJECT_SLUG = "my_cool_project"


@pytest.mark.parametrize("license_", LICENSES)
def test_generation_succeeds_all_licenses(cookies, base_context, license_):
    result = cookies.bake(extra_context={**base_context, "open_source_license": license_})
    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_path.is_dir()


@pytest.mark.parametrize("wf_lang", WF_LANGS)
def test_generation_succeeds_all_wf_langs(cookies, base_context, wf_lang):
    ctx = {**base_context}
    if wf_lang:
        ctx["wf_lang"] = wf_lang
    result = cookies.bake(extra_context=ctx)
    assert result.exit_code == 0, result.exception
    assert result.exception is None
    assert result.project_path.is_dir()


@pytest.mark.parametrize("wf_lang,expected_files", [
    ("Nextflow", ["main.nf", "nextflow.config", "modules/accessory.nf"]),
    ("Snakemake", ["workflow/Snakefile"]),
    ("WDL", [f"{PROJECT_SLUG}.wdl"]),
    ("CWL", [f"{PROJECT_SLUG}.cwl"]),
])
def test_wf_lang_generates_expected_files(cookies, base_context, wf_lang, expected_files):
    result = cookies.bake(extra_context={**base_context, "wf_lang": wf_lang})
    assert result.exit_code == 0, result.exception
    for f in expected_files:
        assert (result.project_path / f).exists(), f"Expected {f} not found for wf_lang={wf_lang}"


def test_cli_on_has_entrypoint(cookies, base_context):
    result = cookies.bake(extra_context=base_context)
    assert result.exit_code == 0, result.exception
    assert (result.project_path / PKG_NAME / "cli.py").exists()
    pyproject = (result.project_path / "pyproject.toml").read_text()
    assert "[project.scripts]" in pyproject


def test_always_present_files(cookies, base_context):
    result = cookies.bake(extra_context=base_context)
    assert result.exit_code == 0, result.exception
    assert (result.project_path / "pixi.toml").exists()
    assert (result.project_path / "Singularity.def").exists()


def test_cli_off_no_entrypoint(cookies, base_context):
    result = cookies.bake(extra_context={**base_context, "project_shell_cmd": ""})
    assert result.exit_code == 0, result.exception
    pyproject = (result.project_path / "pyproject.toml").read_text()
    assert "[project.scripts]" not in pyproject
