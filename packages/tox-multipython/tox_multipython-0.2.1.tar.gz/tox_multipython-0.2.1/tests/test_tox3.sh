#!/usr/bin/env bash
set -eEux -o pipefail


PYTHON="$(py bin --path "${HOST_TAG}")"
TOX="$PYTHON -m tox -v"
PKG="$(find /samplepkg/dist -name '*.whl')"

commasep () {
  sed 's/^ *//; s/ *$//; s/  */,/g' <<<"$1"
}

# prepare tox.ini
sed 's/{ALL}/'"$(commasep "$ALL_TAGS")"'/; '\
's/{PASSING}/'"$(commasep "$TARGET_TAGS_PASSING")"'/; '\
's/{NOINSTALL}/'"$(commasep "$TARGET_TAGS_NOINSTALL")"'/; '\
's/{NOTFOUND}/'"$(commasep "$TARGET_TAGS_NOTFOUND")"'/' \
tox.template.ini > tox.ini

# test passing tags
for TAG in $TARGET_TAGS_PASSING; do
  $TOX run -e "$TAG" --installpkg="$PKG"
done

# test non-installable tags
for TAG in $TARGET_TAGS_NOINSTALL; do
  if $TOX run -e "$TAG" --skip-pkg-install; then false; fi
  [[ "$($TOX run -e "$TAG" --skip-pkg-install)" != *" InterpreterNotFound: "* ]]
done

# test non-discoverable tags
for TAG in $TARGET_TAGS_NOTFOUND; do
  if $TOX run -e "$TAG"; then false; fi
  [[ "$($TOX run -e "$TAG")" == *" InterpreterNotFound: "* ]]
done

# status
echo "TEST CASE PASSED: ${HOST_TAG} ${VIRTUALENV_PIN}" >&2
