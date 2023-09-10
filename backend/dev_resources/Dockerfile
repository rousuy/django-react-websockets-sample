FROM python:3.11-bullseye

ARG USER_ID
ARG GROUP_ID

WORKDIR /workspace

COPY ./dev_resources/dev-requirements.txt /tmp/dev-requirements.txt

RUN set -x \
    && apt update && apt install gettext -y \
    && python -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install -U pip wheel pip-tools \
    && /opt/venv/bin/pip-sync /tmp/dev-requirements.txt --pip-args "--no-cache-dir --no-deps"

RUN addgroup --gid $GROUP_ID user

RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

RUN chown -R $USER_ID:$GROUP_ID /workspace && chown -R $USER_ID:$GROUP_ID /opt/venv

USER user

ENV PATH="/opt/venv/bin:${PATH}"

ENV PYTHONUNBUFFERED 1

ENV PYTHONPATH /workspace