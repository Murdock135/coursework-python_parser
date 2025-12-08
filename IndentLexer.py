from typing import TextIO, Any
import sys

from minipythonLexer import minipythonLexer

# ================================================================================================================
# IndentLexer extends the ANTLR-generated minipythonLexer to add support for Python-style indentation.
# It tracks indentation levels and emits INDENT and DEDENT tokens when the indentation changes,
# allowing the parser to recognize block structure based on leading whitespace, similar to Python's syntax.

class IndentLexer(minipythonLexer):
    '''
    A lexer that handles indentation-based block structure similar to Python.
    '''
    def __init__(self, input=None, output: TextIO | Any = sys.stdout):
        super().__init__(input, output)

        self.indent_stack = [0]  # Stack to hold current indentation level
        self.pending_tokens = []  # Queue to hold pending tokens after indentation changes

    def _count_indent(self) -> int:
        '''Count the number of spaces after matching a NEWLINE token (\n)'''
        count = 0
        offset = 1 # Current token is \n so start checking from next token

        while True:
            char = self._input.LA(offset) # _input is an instance of InputStream. Grandparent class Lexer has self._input
            if char == ord(' '):
                count += 1
            elif char == ord('\t'):
                count += 4  # Assuming a tab is equivalent to 4 spaces
            else:
                break
            offset += 1
        
        return count

    # TODO
    def nextToken(self):
        pass