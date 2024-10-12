#!/usr/bin/env python

"""Tests for `{{ cookiecutter.pkg_name }}` package."""

import pytest
# https://docs.pytest.org/en/stable/index.html

import hypothesis
# https://hypothesis.readthedocs.io/en/latest/index.html

import {{ cookiecutter.pkg_name }}


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_{{cookiecutter.pkg_name}}(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
    pass
