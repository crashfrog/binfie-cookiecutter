#!/bin/bash

set -e

# Create optional workflow files, depending on the language

{%- if cookiecutter.wf_lang == "Nextflow" %}
echo "Creating Nextflow project"
cat <<- EOF > main.nf
#!/usr/bin/env nextflow

/*
Author: {{cookiecutter.full_name}}
Email: {{cookiecutter.email}}

{{cookiecutter.project_short_description}}

*/

//use DSL 2
nextflow.enable.dsl=2

//import subworkflows
include { accessory } from './modules/accessory.nf'


//Simple usage message
def helpMessage() {
    log.info"""
Usage:

nextflow run {{cookiecutter.github_username}}/cookiecutter.__project_slug}} <ARGUMENTS>

Required Arguments:

    # Put some arguments here

Optional Arguments:

    # Put some arguments here

    """.stripIndent()
}

//main script

workflow {

    // Show help message if the user specifies the --help flag at runtime
    // or if any required params are not provided
    if ( params.help || !params.input ) {
        // Invoke the function above which prints the help message
        helpMessage()
        // Exit out and do not run anything else
        exit 1
    }

    //Define the input parameters
    params.input = "input"

    //Define the output parameters
    output:
    file("output") into output_ch

    //Define the process
    process myProcess {
        input:
        file input from params.input

        output:
        file("output") into output_ch

        script:
        """
        # Put your script here
        """
    }

    //Define the output channel
    output_ch.view { it }

}
EOF

cat <<- EOF > nextflow.config
profiles {
    docker {
        docker {
            enabled = true
            temp = 'auto'
        }
    }
}
/*
Set default parameters

Any parameters provided by the user with a -params-file or
with -- command-line arguments will override the values
defined below.
*/
params {
    help = false
    input = false
}
EOF
mkdir modules
cat <<- EOF > modules/accessory.nf
#!/usr/bin/env nextflow

// Using DSL-2
nextflow.enable.dsl=2

// Define an accessory subworkflow here
process accessory {
    input:
    file input

    output:
    file("output") into accessory_ch

    script:
    """
    # Put your script here
    """
}
EOF

{%- elif cookiecutter.wf_lang == "Snakemake" %}
echo "Creating Snakemake project"
mkdir workflow
cat <<- EOF > workflow/Snakefile
###
# Author: {{cookiecutter.full_name}}
# Email: {{cookiecutter.email}}
#
# {{cookiecutter.project_short_description}}
###
rule all:
    shell: "echo \"Nothing to do. Modify ./Snakefile to define your pipeline...\""
EOF


{%- elif cookiecutter.wf_lang == "CWL" %}
echo "Creating CWL project"
cat <<- EOF > {{cookiecutter.__project_slug}}.cwl
#!/usr/bin/env cwl-runner

class: {{cookiecutter.__project_slug}}
id: "{{cookiecutter.project_name}}.cwl"
label: "{{cookiecutter.project_name}}"
cwlVersion: v1.1
doc: |
    {{cookiecutter.project_short_description}}

dct:creator:
  foaf:name: {{cookiecutter.full_name}}
  foaf:mbox: "{{cookiecutter.email}}"

inputs:
  # Define your inputs here

outputs:
    # Define your outputs here

$namespaces:
    dct: https://purl.org/dc/terms/
    foaf: https://xmlns.com/foaf/0.1/

EOF

{%- elif cookiecutter.wf_lang == "WDL" %}
echo "Creating WDL project"
cat <<- EOF > {{cookiecutter.__project_slug}}.wdl
# {{cookiecutter.project_name}}
# {{cookiecutter.project_short_description}}
# Author: {{cookiecutter.full_name}} <{{cookiecuttter.email}}>

version 1.2

workflow {{cookiecutter.__project_slug}} {
    # Define your workflow here
}

task {{cookiecutter.__project_slug}} {
    # Define your task here
}



EOF
{%- endif %}

git init --initial-branch=main
git add *
git add .gitignore
git add .github/
git remote add origin https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.__project_slug}}.git
echo "Do this: cd {{cookiecutter.__project_slug}} && git commit -m 'initial commit' && git tag -a '{{cookiecutter.version}}' -m '{{cookiecutter.version}}' && make help"
