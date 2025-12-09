#!/bin/bash
set -uo pipefail

# Generate the parser and run the sample program
echo "===================================================================================="
echo "[RUN] Starting parser generation"
antlr4 -Dlanguage=Python3 minipython.g4
echo "[RUN] Parser generated."

echo "===================================================================================="
echo "[RUN] Testing against python_samples/project_deliverable_1.py"
uv run main.py python_samples/project_deliverable_1.py 2>&1 | tee output_pd1.log
echo "[RUN] Done testing against python_samples/project_deliverable_1.py"

echo "===================================================================================="
echo "[RUN] Testing against python_samples/project_deliverable_2.py"
uv run main.py python_samples/project_deliverable_2.py 2>&1 | tee output_pd2.log
echo "[RUN] Done testing against python_samples/project_deliverable_2.py"

# Generate the parse tree
echo "===================================================================================="
echo "[RUN] Generating parse trees"
antlr4-parse minipython.g4 prog -gui python_samples/project_deliverable_1.py > parse_tree_1.ps 2>> run.log
echo "[RUN] Parse tree for project_deliverable_1.py generated as parse_tree_1.ps"

echo "===================================================================================="
echo "[RUN] Generating parse tree for project_deliverable_2.py"
antlr4-parse minipython.g4 prog -gui python_samples/project_deliverable_2.py > parse_tree_2.ps 2>> run.log
echo "[RUN] Parse tree for project_deliverable_2.py generated as parse_tree_2.ps"