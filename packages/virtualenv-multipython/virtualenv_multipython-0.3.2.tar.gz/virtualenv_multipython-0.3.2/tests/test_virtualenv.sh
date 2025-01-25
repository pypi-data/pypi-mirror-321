#!/usr/bin/env bash
set -eEux -o pipefail

PYTHON="$(py bin --path "${HOST_TAG}")"

# test passing tags
for TAG in $TARGET_TAGS_PASSING $TARGET_TAGS_NOINSTALL; do
  $PYTHON -m virtualenv -p "$TAG" --no-seed --with-traceback "/tmp/$TAG"
  [ "$(py tag "/tmp/$TAG/bin/python")" = "$TAG" ]
done

# test failing tags
for TAG in $TARGET_TAGS_NOTFOUND; do
  [[ "$($PYTHON -m virtualenv -p "$TAG" "/tmp/$TAG" 2>&1)" == *"RuntimeError: failed to find interpreter "* ]]
  [ ! -d "/tmp/$TAG" ]
done

# status
echo "TEST CASE PASSED: ${HOST_TAG} ${VIRTUALENV_PIN}" >&2
