from .{{cookiecutter.package_name}} import *
import pkg_resources

__version__ = pkg_resources.get_distribution("{{cookiecutter.package_name}}").version