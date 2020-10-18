FROM python:3.8.5-alpine3.12

LABEL maintainer="Artem Zdor <zdor@adv.ru>"

ENV PYTHONUNBUFFERED 1

COPY ["requirements.txt", "/app/"]

WORKDIR /app

RUN apk add --update --no-cache --virtual .build-deps \
        build-base \
        libffi-dev \
        gcc \
        musl-dev \
        dnscache \
        linux-headers \
        g++ \
        python3-dev \
        make \
    && rm -rf /var/cache/apk/* \
    && pip install --no-cache-dir --upgrade pip==20.2.2 pip-tools==5.3.1 \
    && pip-sync requirements.txt \
    && apk del .build-deps \
    && rm -rf /root/.cache/*

