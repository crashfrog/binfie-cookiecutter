{%- if cookiecutter.project_shell_cmd -%}
import click
{% endif %}

import logging

{% if cookiecutter.project_shell_cmd %}
## https://click.palletsprojects.com/en/8.1.x/

## @click.group()
## @click.argument()
## @click.option('-s', '--string-to-echo', 'string')
## @click.option('--n', default=1, show_default=True)
## @click.option('--shout/--no-shout', default=False)


@click.group()
@click.version_option(
    package_name="{{ cookiecutter.pkg_name }}",
    message="%(prog)s %(version)s")
@click.option("-v", "--verbose", count=True)
def cli(verbose=0):
    """
    {{cookiecutter.project_short_description|wordwrap(70, wrapstring='\n    ')}}.
    """
    log_level = [60, 30, 20, 10][verbose]
    logging.basicConfig(
        level=log_level,
        format='[%(asctime)s][%(name)-12s][%(levelname)-8s] %(message)s',
        datefmt='%m-%d %H:%M')


if __name__ == '__main__':
    cli()
{% else %}
def main(verbose=0):
    """
    {{cookiecutter.project_short_description|wordwrap(70, wrapstring='\n    ')}}.
    """
    log_level = [60, 30, 20, 10][verbose]
    logging.basicConfig(
        level=log_level,
        format='[%(asctime)s][%(name)-12s][%(levelname)-8s] %(message)s',
        datefmt='%m-%d %H:%M')

if __name__ == '__main__':
    main()
{% endif %}