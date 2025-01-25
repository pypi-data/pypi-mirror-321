#!/usr/bin/env bash
set -eEux -o pipefail

PYTHON="$(py bin --path "${HOST_TAG}")"
TOX="$PYTHON -m tox -v"

# prepare env vars referenced in tox.ini
export ENVS_PASSING="${TARGET_TAGS_PASSING// /,}"
export ENVS_NOINSTALL="${TARGET_TAGS_NOINSTALL// /,}"
export ENVS_NOTFOUND="${TARGET_TAGS_NOTFOUND// /,}"
export ENVS="${ALL_TAGS// /,}"

PKG="$(find /samplepkg/dist -name '*.whl')"

# test passing tags
$TOX run -m passing --installpkg="$PKG"

# test non-installable tags
if [ -n "$ENVS_NOINSTALL" ]; then
  # passing
  TOX_PACKAGE=skip $TOX run -m noinstall
  # failing
  if TOX_PACKAGE=external $TOX run -m noinstall --installpkg="$PKG"; then false; fi
fi

# test non-discoverable tags
for TAG in $TARGET_TAGS_NOTFOUND; do
  [[ "$($TOX run -e "$TAG")" == *" failed with could not find python "* ]]
done

# status
echo "TEST CASE PASSED: ${HOST_TAG} ${VIRTUALENV_PIN}" >&2
