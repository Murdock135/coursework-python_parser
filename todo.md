1. create directories grammar generated src src/utils scripts output/{parse_trees}
2. rename python_samples/ -> test_code/
3. create `__init__.py`'s
    3.1 generated/
    3.2 src/
    3.3 src/utils
4. change antlr command to output generated parser to generated/ `antlr4 -Dlanguage=Python3 -o generated grammar/minipython.g4`
5. move main.py and IndentLexer.py into it 
6. Fix imports in IndentLexer.py and main.py
7. Move bash scripts to scripts/
    - build_and_test.sh
    - run.sh
8. Update bash scripts
    - build_and_test.sh
    - run.sh

8. Update .gitignore
    - add generated/
    - add output/
    - add *.log/
    - add *.ps

