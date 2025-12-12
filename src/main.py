import sys
from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Tree import TerminalNodeImpl, ErrorNodeImpl

from .IndentLexer import IndentLexer
from .MyListener import MyListener

from generated.minipythonParser import minipythonParser


# ==========================================================================================
# SAFE, NULL-PROOF LISP TREE PRINTER
# ==========================================================================================
def to_lisp(node, parser):
    """Convert a parse tree to LISP-style text safely."""
    if node is None:
        return "(None)"

    if isinstance(node, TerminalNodeImpl):
        text = node.getText()
        if text is None:
            return "(NoneTerminal)"
        return text

    if isinstance(node, ErrorNodeImpl):
        return f"(ErrorNode {node.getText()})"

    rule_index = node.getRuleIndex()
    rule_name = parser.ruleNames[rule_index]

    child_count = node.getChildCount()
    if child_count == 0:
        return f"({rule_name})"

    children_strs = []
    for i in range(child_count):
        child = node.getChild(i)
        children_strs.append(to_lisp(child, parser))

    return f"({rule_name} {' '.join(children_strs)})"


# ==========================================================================================
# OPTIONAL TREE INTEGRITY CHECK
# ==========================================================================================
def check_tree(node, errors):
    """Verify that the parse tree contains no None children."""
    if node is None:
        errors.append("Encountered None node in parse tree.")
        return

    if isinstance(node, (TerminalNodeImpl, ErrorNodeImpl)):
        return

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        if child is None:
            errors.append("A parser rule contains a None child.")
        else:
            check_tree(child, errors)


# ==========================================================================================
# CUSTOM ERROR LISTENER (optional but useful)
# ==========================================================================================
class ThrowingErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Syntax error at line {line}:{column}: {msg}")


# ==========================================================================================
# MAIN EXECUTION
# ==========================================================================================
def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"Parsing file: {input_file}")

    # -------------
    # SETUP LEXER
    # -------------
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = IndentLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # -------------
    # SETUP PARSER
    # -------------
    parser = minipythonParser(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(ThrowingErrorListener())  # optional

    # -------------
    # PARSE
    # -------------
    try:
        tree = parser.prog()
    except Exception as e:
        print("❌ Parsing failed:")
        print(e)
        return

    print("-------------------------------------------------------------------------")
    print("Checking parse tree integrity...")

    errors = []
    check_tree(tree, errors)

    if errors:
        print("❌ Tree integrity issues detected:")
        for e in errors:
            print("   -", e)
    else:
        print("✔ Parse tree looks valid.")

    print("\n[TREE] (LISP Style)\n")

    try:
        tree_str = to_lisp(tree, parser)
        print(tree_str)
    except Exception as e:
        print("❌ Could not print tree in LISP format.")
        print("Reason:", e)

    print("------------------------------------------------------------------------")

    # -------------
    # WALK THE PARSE TREE WITH LISTENER
    # -------------
    listener = MyListener()
    walker = ParseTreeWalker()

    try:
        walker.walk(listener, tree)
    except Exception as e:
        print("❌ Listener execution failed:")
        print(e)
        return


# ==========================================================================================
# ENTRY POINT
# ==========================================================================================
if __name__ == '__main__':
    main()
