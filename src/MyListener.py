from antlr4 import *
from generated.minipythonParser import minipythonParser
from generated.minipythonListener import minipythonListener

class MyListener(minipythonListener):
    
    def enterIf_stmt(self, ctx:minipythonParser.If_stmtContext):
        print(f"[IF_STMT] if_stmt detected at line {ctx.start.line}")
    
    def enterExpr(self, ctx:minipythonParser.ExprContext):
        print(f"[EXPR] expr detected at line {ctx.start.line}")
    
    def enterAssignment(self, ctx:minipythonParser.AssignmentContext):
        print(f"[ASSIGNMENT] assignment detected at line {ctx.start.line}")
    
    def enterCompound_assignment(self, ctx:minipythonParser.Compound_assignmentContext):
        print(f"[COMPOUND_ASSIGNMENT] compound_assignment detected at line {ctx.start.line}")

    # def enterWhile_stmt(self, ctx:minipythonParser.While_stmtContext):
    #     print(f"[STRUCTURE] while_stmt detected at line {ctx.start.line}")
    
    # Add more enterXXX methods for other structures you want to detect