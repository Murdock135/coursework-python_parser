from typing import TextIO, Any
import sys

from minipythonLexer import minipythonLexer
from minipythonParser import minipythonParser
from antlr4.Token import CommonToken

# ================================================================================================================
# IndentLexer extends the ANTLR-generated minipythonLexer to add support for Python-style indentation.
# It tracks indentation levels and emits INDENT and DEDENT tokens when the indentation changes,
# allowing the parser to recognize block structure based on leading whitespace, similar to Python's syntax.

class IndentLexer(minipythonLexer):
    '''
    A lexer that handles indentation-based block structure similar to Python.
    '''
    INDENT = minipythonParser.INDENT
    DEDENT = minipythonParser.DEDENT

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

    # =================================================================================
    # Conceptual:
    # Take the following example:
    # --------------------------------
    # if x:
    #   if y:
    #       a = 1
    # b = 2
    # --------------------------------
    # The lexer processes each line and tracks indentation:
    # - After 'if x:\n', the lexer sees the indent increase from 0 to 4 spaces.
    #   It pushes 4 to the indent stack, queues INDENT, and returns NEWLINE.
    #   Stack: [0, 4]
    # - After 'if y:\n', the indent increases from 4 to 8 spaces.
    #   It pushes 8 to the stack, queues INDENT, and returns NEWLINE.
    #   Stack: [0, 4, 8]
    # - After 'a = 1\n', the indent decreases from 8 to 4 spaces.
    #   It pops 8 from the stack, queues DEDENT, and returns NEWLINE.
    #   Stack: [0, 4]
    # - After 'b = 2\n', the indent decreases from 4 to 0 spaces.
    #   It pops 4 from the stack, queues DEDENT, and returns NEWLINE.
    #   Stack: [0]
    # This mechanism allows the parser to recognize when blocks start and end,
    # mirroring Python's indentation-based syntax.

    def nextToken(self):
        '''
        Returns the next token, handling Python-style indentation.

        Conceptual flow using this example:
        -----------------------------------
        if x:
            if y:
                a = 1
        b = 2

        The lexer processes each line and tracks indentation:
        - After 'if x:\\n', the lexer sees the indent increase from 0 to 4 spaces.
          It pushes 4 to the indent stack, queues INDENT, and returns NEWLINE.
          Stack: [0, 4]
        - After 'if y:\\n', the indent increases from 4 to 8 spaces.
          It pushes 8 to the stack, queues INDENT, and returns NEWLINE.
          Stack: [0, 4, 8]
        - After 'a = 1\\n', the indent decreases from 8 to 4 spaces.
          It pops 8 from the stack, queues DEDENT, and returns NEWLINE.
          Stack: [0, 4]
        - After 'b = 2\\n', the indent decreases from 4 to 0 spaces.
          It pops 4 from the stack, queues DEDENT, and returns NEWLINE.
          Stack: [0]

        This mechanism allows the parser to recognize when blocks start and end,
        mirroring Python's indentation-based syntax.
        '''
        # Return any pending INDENT/DEDENT tokens first
        if self.pending_tokens:
            return self.pending_tokens.pop(0)
        
        token = super().nextToken()

        # If the token is a NEWLINE, check for indentation changes
        if token.type == self.NEWLINE:
            current_indent_level = self.indent_stack[-1]
            next_indent_level = self._count_indent()

            # Indentation detected
            if next_indent_level > current_indent_level:
                self.indent_stack.append(next_indent_level)
                indent_token = CommonToken(type=self.INDENT)
                self.pending_tokens.append(indent_token)
            
            # Dedentation(s) detected
            elif next_indent_level < current_indent_level:
                while next_indent_level != self.indent_stack[-1]:
                    dedent_token = CommonToken(type=self.DEDENT)
                    self.pending_tokens.append(dedent_token)
                    self.indent_stack.pop()
            
        return token


