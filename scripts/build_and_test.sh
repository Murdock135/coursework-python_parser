#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."
OUTPUT_DIR="$PROJECT_ROOT/output"

echo "===================================================================================="
echo "[RUN] Starting parser generation"
antlr4 -Dlanguage=Python3 -o "$PROJECT_ROOT/generated" "$PROJECT_ROOT/grammar/minipython.g4" 2>&1 | tee "$OUTPUT_DIR/parser_generation.log"
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

echo "[RUN] All tasks completed successfully."