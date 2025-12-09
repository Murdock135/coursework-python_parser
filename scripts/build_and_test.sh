#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."
OUTPUT_DIR="$PROJECT_ROOT/output"

echo "===================================================================================="
echo "[RUN] Starting parser generation"
antlr4 -Dlanguage=Python3 -o "$PROJECT_ROOT/generated" "$PROJECT_ROOT/grammar/minipython.g4"
echo "[RUN] Parser generated."

echo "===================================================================================="
echo "[RUN] Testing against test_code/project_deliverable_1.py"
uv run "$PROJECT_ROOT/src/main.py" "$PROJECT_ROOT/test_code/project_deliverable_1.py" 2>&1 | tee "$OUTPUT_DIR/output_pd1.log"
echo "[RUN] Done testing against test_code/project_deliverable_1.py"

echo "===================================================================================="
echo "[RUN] Testing against test_code/project_deliverable_2.py"
uv run "$PROJECT_ROOT/src/main.py" "$PROJECT_ROOT/test_code/project_deliverable_2.py" 2>&1 | tee "$OUTPUT_DIR/output_pd2.log"
echo "[RUN] Done testing against test_code/project_deliverable_2.py"

# echo "===================================================================================="
# echo "[RUN] Generating parse trees"
# antlr4-parse "$PROJECT_ROOT/grammar/minipython.g4" prog -gui "$PROJECT_ROOT/test_code/project_deliverable_1.py" > "$OUTPUT_DIR/parse_trees/parse_tree_1.ps" 2>> "$PROJECT_ROOT/run.log"
# echo "[RUN] Parse tree for project_deliverable_1.py generated as parse_tree_1.ps"

# echo "===================================================================================="
# echo "[RUN] Generating parse tree for project_deliverable_2.py"
# antlr4-parse "$PROJECT_ROOT/grammar/minipython.g4" prog -gui "$PROJECT_ROOT/test_code/project_deliverable_2.py" > "$OUTPUT_DIR/parse_trees/parse_tree_2.ps" 2>> "$PROJECT_ROOT/run.log"
# echo "[RUN] Parse tree for project_deliverable_2.py generated as parse_tree_2.ps"