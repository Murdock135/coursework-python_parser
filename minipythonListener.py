# Generated from minipython.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .minipythonParser import minipythonParser
else:
    from minipythonParser import minipythonParser

# This class defines a complete listener for a parse tree produced by minipythonParser.
class minipythonListener(ParseTreeListener):

    # Enter a parse tree produced by minipythonParser#prog.
    def enterProg(self, ctx:minipythonParser.ProgContext):
        pass

    # Exit a parse tree produced by minipythonParser#prog.
    def exitProg(self, ctx:minipythonParser.ProgContext):
        pass


    # Enter a parse tree produced by minipythonParser#expr.
    def enterExpr(self, ctx:minipythonParser.ExprContext):
        pass

    # Exit a parse tree produced by minipythonParser#expr.
    def exitExpr(self, ctx:minipythonParser.ExprContext):
        pass



del minipythonParser