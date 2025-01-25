# build sample package

FROM python:3.12-slim-bookworm AS build
# hadolint ignore=DL3022
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY tests/samplepkg /samplepkg
WORKDIR /samplepkg
RUN uv build

# base

FROM makukha/multipython:unsafe AS base
SHELL ["/bin/bash", "-o", "errexit", "-o", "errtrace", "-o", "nounset", "-o", "pipefail", "-c"]
COPY dist /proj/dist
COPY tests/test_*.sh tests/tox.*.ini /proj/tests/
COPY --from=build /samplepkg/dist /samplepkg/dist
WORKDIR /proj/tests
# disable virualenv plugin
RUN rm /root/.config/virtualenv/virtualenv.ini
# args
ARG HOST_TAG
ARG TARGET_TAGS_PASSING
ARG TARGET_TAGS_NOINSTALL
ARG TARGET_TAGS_NOTFOUND
ARG VIRTUALENV_PIN
# envs
ENV HOST_TAG="${HOST_TAG}"
ENV TARGET_TAGS_PASSING="${TARGET_TAGS_PASSING}"
ENV TARGET_TAGS_NOINSTALL="${TARGET_TAGS_NOINSTALL}"
ENV TARGET_TAGS_NOTFOUND="${TARGET_TAGS_NOTFOUND}"
ENV ALL_TAGS="${TARGET_TAGS_PASSING} ${TARGET_TAGS_NOINSTALL} ${TARGET_TAGS_NOTFOUND}"
ENV VIRTUALENV_PIN="${VIRTUALENV_PIN}"
# validate tags
RUN <<EOT
    IMAGE_TAGS="$(py ls --tag | sort | xargs)"
    # shellcheck disable=SC2001
    [ "py20 $IMAGE_TAGS" = "$(sed 's/  */\n/g' <<<"$ALL_TAGS" | sort | xargs)" ]
EOT

# test targets

FROM base AS tox3
RUN <<EOT
    PIP="$(py bin --path "$HOST_TAG") -m pip"
    $PIP install --ignore-installed \
      "tox>=3,<4" \
      "virtualenv$VIRTUALENV_PIN" \
      "tox-multipython @ file://$(find /proj/dist -name '*.whl')"
    bash test_tox3.sh
EOT

FROM base AS debug
ENV MULTIPYTHON_DEBUG=true
RUN <<EOT
    PIP="$(py bin --path "$HOST_TAG") -m pip"
    $PIP install --ignore-installed \
      "tox>=3,<4" \
      "virtualenv$VIRTUALENV_PIN" \
      "tox-multipython[debug] @ file://$(find /proj/dist -name '*.whl')"
    # don't run tests at build time
EOT
