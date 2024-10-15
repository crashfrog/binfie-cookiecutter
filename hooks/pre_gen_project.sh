#!/bin/bash

PROJECT_NAME='{{cookiecutter.project_name}}'
PKG_NAME='{{cookiecutter.pkg_name}}'

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

# Query Galaxy Toolshed to check if the tool exists

response=$(curl -s -o /dev/null -w "%{http_code}" https://toolshed.g2.bx.psu.edu/view/$PKG_NAME/)

if [ "$response" -eq 200 ]; then
    echo "Tool '$PKG_NAME' exists on Galaxy Toolshed."
    exit 1
else
    echo "Good news! Tool '$PKG_NAME' does not exist on Galaxy Toolshed."
fi