#!/bin/bash
set -euo pipefail

docker-antlr -Dlanguage=Python3 minipython.g4 && uv run test_parser.py python_samples/project_deliverable_1.py