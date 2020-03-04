# python:3.6-alpine3.9
FROM python@sha256:ad2b24eacc9865244d7b1ae198d507f4ce8f506484c35d27158e7f1dd6041a8b

ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    USER="{{cookiecutter.package_name}}" \
    GROUP="{{cookiecutter.package_name}}" \
    UID=1000 \
    GID=1000 \
    PYTHONUNBUFFERED=1

RUN apk add --update --no-cache --virtual build-dependencies \
    python3-dev \
    build-base \
    linux-headers \
    gcc \
    musl-dev
 && addgroup -g ${GID} -S ${GROUP} \
 && adduser -u ${UID} -s /bin/sh -S ${USER} -G ${GROUP} -G wheel -D

WORKDIR <WORKDIR>
COPY pyproject.toml poetry.lock setup.sh setup_poetry.sh ./

RUN chmod +x *.sh && ./setup.sh
COPY . ./

RUN apk del build-dependencies

USER ${USER}

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]
