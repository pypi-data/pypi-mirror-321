#!/usr/bin/env bash
set -eEux -o pipefail


PYTHON="$(py bin --path "${HOST_TAG}")"
TOX="$PYTHON -m tox -v"
PKG="$(find /samplepkg/dist -name '*.whl')"

commasep () {
  sed 's/^ *//; s/ *$//; s/  */,/g' <<<"$1"
}

# prepare env vars referenced in tox.ini
ENVS_PASSING="$(commasep "$TARGET_TAGS_PASSING")"
ENVS_NOINSTALL="$(commasep "$TARGET_TAGS_NOINSTALL")"
ENVS_NOTFOUND="$(commasep "$TARGET_TAGS_NOTFOUND")"
ALL_ENVS="$(commasep "$ALL_TAGS")"
export ENVS_PASSING
export ENVS_NOINSTALL
export ENVS_NOTFOUND
export ALL_ENVS

# test passing tags
for TAG in $TARGET_TAGS_PASSING; do
  $TOX run -e "$TAG" --installpkg="$PKG"
done

# test non-installable tags
for TAG in $TARGET_TAGS_NOINSTALL; do
  # passing
  TOX_PACKAGE=skip $TOX run -e "$TAG"
  # failing
  if TOX_PACKAGE=external $TOX run -e "$TAG" --installpkg="$PKG"; then false; fi
done

# test non-discoverable tags
for TAG in $TARGET_TAGS_NOTFOUND; do
  [[ "$($TOX run -e "$TAG")" == *" failed with could not find python "* ]]
done

# status
echo "TEST CASE PASSED: tox4 ${HOST_TAG} ${VIRTUALENV_PIN}" >&2
