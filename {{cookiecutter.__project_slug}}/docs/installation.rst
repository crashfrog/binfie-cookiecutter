### Installing {{ cookiecutter.project_name }} ###

To install {{ cookiecutter.project_name }}, run the following command:

```bash
pip install {{ cookiecutter.project_name }}
```

### Installing from source ###
To install {{ cookiecutter.project_name }} from source, clone the repository and run the following command:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
pip install .
```

### Installing from source with editable mode ###
To install {{ cookiecutter.project_name }} from source in editable mode, clone the repository and run the following command:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
pip install -e .
```

### Installing from source with editable mode and development dependencies ###
To install {{ cookiecutter.project_name }} from source in editable mode with development dependencies, clone the repository and run the following command:

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.git
cd {{ cookiecutter.project_name }}
pip install -e .[dev]
```
