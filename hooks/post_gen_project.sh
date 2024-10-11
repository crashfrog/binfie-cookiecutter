#!/bin/bash

set -e

git init --initial-branch=main
git add *
git add .gitignore
git add .github
git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
echo "Do this: cd {{cookiecutter.project_slug}} && git commit -m 'initial commit' && git tag -a '{{cookiecutter.version}}' -m '{{cookiecutter.version}}' && make help"