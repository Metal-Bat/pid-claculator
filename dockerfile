FROM python:3.11.1-slim

ARG APP_HOME=/app

WORKDIR ${APP_HOME}

# Create Docker user
RUN addgroup --system control \
    && adduser --system --ingroup control control

# copy application code to WORKDIR
COPY --chown=control:control . ${APP_HOME}

# make control owner of the WORKDIR directory as well.
RUN chown control:control ${APP_HOME}

# control
USER control

# Create Python Dependency and Sub-Dependency Wheels.
RUN python -m pip install wheel setuptools

# use wheels to install python dependencies
RUN python -m pip install -r requirements.txt
