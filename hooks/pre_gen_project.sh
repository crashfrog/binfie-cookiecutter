#!/bin/bash

PROJECT_NAME='{{cookiecutter.project_name}}'
PKG_NAME='{{cookiecutter.pkg_name}}'

{% if cookiecutter.__name_check %}
# Query PyPI to check if the project exists
response=$(curl -s -o /dev/null -w "%{http_code}" https://pypi.org/project/$PKG_NAME/)

if [ "$response" -eq 200 ]; then
    echo "Project '$PKG_NAME' exists on PyPI."
    exit 1
else
    echo "Good news! Project '$PKG_NAME' does not exist on PyPI."
fi

# Query Bioconda to check if the package exists

response=$(curl -s -o /dev/null -w "%{http_code}" https://bioconda.github.io/recipes/$PKG_NAME/README.html)

if [ "$response" -eq 200 ]; then
    echo "Package '$PKG_NAME' exists on Bioconda."
    exit 1
else
    echo "Good news! Package '$PKG_NAME' does not exist on Bioconda."
fi

# Query Galaxy Toolshed to see if the response contains the phrase "contains no repositories"

response=$(curl -s https://toolshed.g2.bx.psu.edu/view/$PKG_NAME)

if [[ $response == *"contains no repositories"* ]]; then
    echo "Package '$PKG_NAME' does not exist on Galaxy Toolshed."
else
    echo "Package '$PKG_NAME' exists on Galaxy Toolshed."
    exit 1
fi
{% endif %}