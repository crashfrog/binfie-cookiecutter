{%- if cookiecutter.project_shell_cmd -%}
import click

@click.command("{{ cookiecutter.project_shell_cmd }}")
def cli():
    pass

if __name__ == '__main__':
    cli()

{% endif %}