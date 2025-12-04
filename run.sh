#!/bin/bash
set -uo pipefail

docker-antlr -Dlanguage=Python3 minipython.g4 && uv run main.py python_samples/project_deliverable_1.py