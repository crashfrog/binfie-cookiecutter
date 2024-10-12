### {{ cookiecutter.project_name }} ###
## {{ cookiecutter.project_short_description }} ##

Overview
========

This project is a bioinformatic workflow designed to process and analyze biological data. This is a super-boring description of the project. Please update this file with a more detailed description of the project so that users can understand what the project is about.

Key Features
------------

- Tell us what the key features are.

Installation
------------

To install the necessary dependencies, run:

.. code-block:: bash

    pip install .

Usage
-----

To run the tool, execute the main script:

.. code-block:: bash

    {%- if cookiecutter.project_shell_cmd %}
    {{ cookiecutter.project_shell_cmd }} [OPTIONS] ARGUMENTS
    {%- if cookiecutter.wf_lang %}
or
.. code-block:: bash
{%- endif %}
{%- endif %}
    {%- if cookiecutter.wf_lang == 'nextflow' %}
    nextflow run {{cookiecutter.github_username}}/{{cookiecutter.project_name}}
    {%- elif cookiecutter.wf_lang == 'snakemake' %}
    snakemake
    {%- elif cookiecutter.wf_lang == 'CWL' %}
    cwl-runner {{cookiecutter.__project_slug}}.cwl
    {%- elif cookiecutter.wf_lang == 'WDL' %}
    miniwdl run {{cookiecutter.__project_slug}}.wdl
    {%- endif %}



Contributing
------------

We welcome contributions from the community. Please refer to the `CONTRIBUTING.rst` file for guidelines on how to contribute to this project.

License
-------

See the `LICENSE` file for more details.


Cookiecutter
------------

Created from Binfie-cookiecutter, https://github.com/crashfrog/binfie-cookiecutter