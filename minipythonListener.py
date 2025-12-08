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


    # Enter a parse tree produced by minipythonParser#block.
    def enterBlock(self, ctx:minipythonParser.BlockContext):
        pass

    # Exit a parse tree produced by minipythonParser#block.
    def exitBlock(self, ctx:minipythonParser.BlockContext):
        pass


    # Enter a parse tree produced by minipythonParser#statement.
    def enterStatement(self, ctx:minipythonParser.StatementContext):
        pass

    # Exit a parse tree produced by minipythonParser#statement.
    def exitStatement(self, ctx:minipythonParser.StatementContext):
        pass


    # Enter a parse tree produced by minipythonParser#assignment.
    def enterAssignment(self, ctx:minipythonParser.AssignmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#assignment.
    def exitAssignment(self, ctx:minipythonParser.AssignmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#compound_assignment.
    def enterCompound_assignment(self, ctx:minipythonParser.Compound_assignmentContext):
        pass

    # Exit a parse tree produced by minipythonParser#compound_assignment.
    def exitCompound_assignment(self, ctx:minipythonParser.Compound_assignmentContext):
        pass


    # Enter a parse tree produced by minipythonParser#if_stmt.
    def enterIf_stmt(self, ctx:minipythonParser.If_stmtContext):
        pass

    # Exit a parse tree produced by minipythonParser#if_stmt.
    def exitIf_stmt(self, ctx:minipythonParser.If_stmtContext):
        pass


    # Enter a parse tree produced by minipythonParser#expr.
    def enterExpr(self, ctx:minipythonParser.ExprContext):
        pass

    # Exit a parse tree produced by minipythonParser#expr.
    def exitExpr(self, ctx:minipythonParser.ExprContext):
        pass


    # Enter a parse tree produced by minipythonParser#atom.
    def enterAtom(self, ctx:minipythonParser.AtomContext):
        pass

    # Exit a parse tree produced by minipythonParser#atom.
    def exitAtom(self, ctx:minipythonParser.AtomContext):
        pass



del minipythonParser