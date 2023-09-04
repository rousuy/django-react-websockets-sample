FROM python:3.11

ARG USER_ID
ARG GROUP_ID

COPY dev-requirements.txt /tmp/dev-requirements.txt

RUN set -x \
    && python -m venv /opt/djmeet \
    && /opt/djmeet/bin/python -m pip install -U pip wheel pip-tools \
    && /opt/djmeet/bin/pip-sync /tmp/dev-requirements.txt --pip-args "--no-cache-dir --no-deps" \
    && mkdir -p /workspace && chown -R $USER_ID:$GROUP_ID /workspace && chown -R $USER_ID:$GROUP_ID /opt/djmeet

RUN addgroup --gid $GROUP_ID user

RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user

USER user

WORKDIR /workspace

ENV PATH="/opt/djmeet/bin:${PATH}"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /workspace/base