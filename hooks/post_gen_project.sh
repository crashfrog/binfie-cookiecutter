#!/bin/sh

set -e

git init
git add *
git commit -m "{{ cookiecutter.project_name }}"