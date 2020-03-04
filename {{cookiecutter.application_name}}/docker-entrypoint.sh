#!/usr/bin/env sh
set -exuo pipefail

command="test"

set -- poetry run invoke "${command}"

exec "$@"
