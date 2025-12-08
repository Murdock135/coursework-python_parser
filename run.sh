#!/bin/bash
set -uo pipefail

# Generate the parser and run the sample program
antlr4 -Dlanguage=Python3 minipython.g4
uv run main.py python_samples/project_deliverable_1.py 
uv run main.py python_samples/project_deliverable_2.py

# Generate the parse tree
antlr4-parse minipython.g4 prog -gui python_samples/project_deliverable_1.py > parse_tree_1.ps
antlr4-parse minipython.g4 prog -gui python_samples/project_deliverable_2.py > parse_tree_2.ps
