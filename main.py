#!/usr/bin/env python3
from antlr4 import *
from minipythonLexer import minipythonLexer
from minipythonParser import minipythonParser
from minipythonListener import minipythonListener
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_parser.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    # Read input
    input_stream = FileStream(input_file)
    
    # Create lexer
    lexer = minipythonLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    # Create parser
    parser = minipythonParser(token_stream)
    
    # Parse the input
    tree = parser.prog()
    
    # Print the parse tree
    print("Parse tree:")
    print(tree.toStringTree(recog=parser))
    
    # Check for syntax errors
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\n{parser.getNumberOfSyntaxErrors()} syntax error(s) found.")
    else:
        print("\nParsing completed successfully!")

if __name__ == '__main__':
    main()