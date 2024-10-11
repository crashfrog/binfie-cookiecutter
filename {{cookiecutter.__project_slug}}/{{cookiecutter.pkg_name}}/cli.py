{%- if cookiecutter.project_shell_cmd -%}
import click
{% endif %}

import logging

## https://click.palletsprojects.com/en/8.1.x/

## @click.group()
## @click.argument()
## @click.option('-s', '--string-to-echo', 'string')
## @click.option('--n', default=1, show_default=True)
## @click.option("--gr", is_flag=True, show_default=True, default=False, help="Greet the world.")
## @click.option("--br", is_flag=True, show_default=True, default=True, help="Add a thematic break")
## @click.option('--shout/--no-shout', default=False)


{% if cookiecutter.project_shell_cmd %}
@click.group()
@click.version_option(package_name="{{ cookiecutter.pkg_name }}", message="%(prog)s %(version)s")
@click.option("-v", "--verbose", count=True)
def cli(verbose=0):
    "{{cookiecutter.project_short_description}}"
    log_level = {0:60, 1:30, 2:20, 3:10}[verbose]
    logging.basicConfig(level=log_level,
                        format='[%(asctime)s][%(name)-12s][%(levelname)-8s] %(message)s',
                        datefmt='%m-%d %H:%M')


if __name__ == '__main__':
    cli()
{% else %}
def main():
    "do stuff"
    pass

if __name__ == '__main__':
    main()
{% endif %}