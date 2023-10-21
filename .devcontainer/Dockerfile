ARG PYTHON_VERSION="3.11-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${PYTHON_VERSION}

ARG NODE_VERSION="18"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c \
"umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

COPY ./backend/dev_resources/dev-requirements.txt /tmp/pip/

RUN set -x \
    && python -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install -U pip wheel pip-tools \
    && /opt/venv/bin/pip-sync /tmp/pip/dev-requirements.txt --pip-args "--no-cache-dir --no-deps" \
    && rm -rf /tmp/pip

RUN mkdir -p /workspace /opt/venv \
    && chown -R vscode:vscode /workspace /opt/venv

USER vscode

ENV PATH="/opt/venv/bin:${PATH}"

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /workspace
