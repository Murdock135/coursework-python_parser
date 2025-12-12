#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."
OUTPUT_DIR="$PROJECT_ROOT/output"

echo "===================================================================================="
echo "[RUN] Starting parser generation"
antlr4 -Dlanguage=Python3 -visitor -o "$PROJECT_ROOT/generated" "$PROJECT_ROOT/grammar/minipython.g4" 2>&1 | tee "$OUTPUT_DIR/parser_generation.log"
echo "[RUN] Parser generated."

echo "===================================================================================="
echo "[RUN] Testing against test_code/project_deliverable_1.py"
uv run -m src.main "$PROJECT_ROOT/test_code/project_deliverable_1.py" 2>&1 | tee "$OUTPUT_DIR/output_pd1.log"
echo "[RUN] Done testing against test_code/project_deliverable_1.py"

echo "===================================================================================="
echo "[RUN] Testing against test_code/project_deliverable_2.py"
uv run -m src.main "$PROJECT_ROOT/test_code/project_deliverable_2.py" 2>&1 | tee "$OUTPUT_DIR/output_pd2.log"
echo "[RUN] Done testing against test_code/project_deliverable_2.py"

echo "===================================================================================="
echo "[RUN] Testing against test_code/project_deliverable_3.py"
uv run -m src.main "$PROJECT_ROOT/test_code/project_deliverable_3.py" 2>&1 | tee "$OUTPUT_DIR/output_pd3.log"
echo "[RUN] Done testing against test_code/project_deliverable_3.py"
echo "===================================================================================="

echo "===================================================================================="
echo "[RUN] Generating ASTs"

mkdir -p "$OUTPUT_DIR/asts"
mkdir -p "$OUTPUT_DIR/asts/ast_pd1"
mkdir -p "$OUTPUT_DIR/asts/ast_pd2"
mkdir -p "$OUTPUT_DIR/asts/ast_pd3"

uv run -m src.ASTVisualizer "$PROJECT_ROOT/test_code/project_deliverable_1.py" -o "$OUTPUT_DIR/asts/ast_pd1" 2>&1 | tee "$OUTPUT_DIR/asts/ast_pd1.log"
uv run -m src.ASTVisualizer "$PROJECT_ROOT/test_code/project_deliverable_2.py" -o "$OUTPUT_DIR/asts/ast_pd2" 2>&1 | tee "$OUTPUT_DIR/asts/ast_pd2.log"
uv run -m src.ASTVisualizer "$PROJECT_ROOT/test_code/project_deliverable_3.py" -o "$OUTPUT_DIR/asts/ast_pd3" 2>&1 | tee "$OUTPUT_DIR/asts/ast_pd3.log"

echo "[RUN] Finished"