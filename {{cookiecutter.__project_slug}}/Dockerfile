ARG VERSION={{ cookiecutter.version}}

# The build-stage image:
FROM continuumio/miniconda3 AS build

# Install the package as normal:
COPY environment.yml .
RUN conda env create -f environment.yml

# Install conda-pack:
RUN conda install -c conda-forge conda-pack

# Use conda-pack to create a standalone enviornment
# in /venv:
RUN conda-pack -n {{cookiecutter.__project_slug}} -o /tmp/env.tar && \
  mkdir /venv && cd /venv && tar xf /tmp/env.tar && \
  rm /tmp/env.tar

# We've put venv in same path it'll be in final image,
# so now fix up paths:
RUN /venv/bin/conda-unpack


# The runtime-stage image; we can use Debian as the
# base image since the Conda env also includes Python
# for us.
FROM debian:bookworm AS runtime
LABEL maintainer="{{cookiecutter.email}}"

# Copy /venv from the previous stage:
COPY --from=build /venv /venv
{%- if cookiecutter.project_shell_cmd %}

# When image is run, run the code with the environment
# activated:
SHELL ["/bin/bash", "-c"]
ENTRYPOINT source /venv/bin/activate && \
           {{cookiecutter.project_shell_cmd}})"
{%- endif %}

FROM runtime AS galaxy

# For use in Galaxy we need an entrypoint that drops us
# into Bash
ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/bin/bash"]