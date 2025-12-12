#!/bin/bash

SCRIPTS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPTS_DIR/.."

mkdir -p "$PROJECT_ROOT/output"
bash "$PROJECT_ROOT/scripts/build_and_test.sh" | tee "$PROJECT_ROOT/output/run.log"