#!/usr/bin/env bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p $SCRIPT_DIR/tmp
uv run openapi-python-client generate \
--config $SCRIPT_DIR/config.yaml \
--path $SCRIPT_DIR/openapi.json \
--output-path $SCRIPT_DIR/tmp \
--overwrite
rm -rf $SCRIPT_DIR/../../src/better_postgrid
mv $SCRIPT_DIR/tmp/better_postgrid $SCRIPT_DIR/../../src/better_postgrid
rm -rf tmp
