#!/bin/bash
set -uo pipefail

# Generate the parser and run the sample program
antlr4 -Dlanguage=Python3 minipython.g4 && uv run main.py python_samples/project_deliverable_1.py

# Generate the parse tree in a separate Docker container
antlr4-parse minipython.g4 prog -gui python_samples/project_deliverable_1.py > parse_tree.ps
