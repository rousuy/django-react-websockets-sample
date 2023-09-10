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



# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1



# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp