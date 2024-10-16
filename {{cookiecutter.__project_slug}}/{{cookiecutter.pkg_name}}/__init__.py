from .{{cookiecutter.pkg_name}} import *
import pkg_resources

__version__ = pkg_resources.get_distribution("{{cookiecutter.__project_slug}}").version
