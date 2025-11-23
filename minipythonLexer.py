# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\t")
        buf.write("\61\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6$\n\6\3\7\6\7\'\n\7\r")
        buf.write("\7\16\7(\3\b\6\b,\n\b\r\b\16\b-\3\b\3\b\2\2\t\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\3\2\6\5\2\'\',,\61\61\4\2--//\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\67\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\3\21\3\2\2\2\5\23\3\2\2\2\7\25\3\2\2\2\t\27\3\2")
        buf.write("\2\2\13#\3\2\2\2\r&\3\2\2\2\17+\3\2\2\2\21\22\7*\2\2\22")
        buf.write("\4\3\2\2\2\23\24\7+\2\2\24\6\3\2\2\2\25\26\t\2\2\2\26")
        buf.write("\b\3\2\2\2\27\30\t\3\2\2\30\n\3\2\2\2\31\32\7?\2\2\32")
        buf.write("$\7?\2\2\33\34\7#\2\2\34$\7?\2\2\35$\7>\2\2\36\37\7>\2")
        buf.write("\2\37$\7?\2\2 $\7@\2\2!\"\7@\2\2\"$\7?\2\2#\31\3\2\2\2")
        buf.write("#\33\3\2\2\2#\35\3\2\2\2#\36\3\2\2\2# \3\2\2\2#!\3\2\2")
        buf.write("\2$\f\3\2\2\2%\'\t\4\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2")
        buf.write("\2()\3\2\2\2)\16\3\2\2\2*,\t\5\2\2+*\3\2\2\2,-\3\2\2\2")
        buf.write("-+\3\2\2\2-.\3\2\2\2./\3\2\2\2/\60\b\b\2\2\60\20\3\2\2")
        buf.write("\2\6\2#(-\3\b\2\2")
        return buf.getvalue()


class minipythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    OP_1 = 3
    OP_2 = 4
    OP_3 = 5
    INT = 6
    WS = 7

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "OP_1", "OP_2", "OP_3", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "OP_1", "OP_2", "OP_3", "INT", "WS" ]

    grammarFileName = "minipython.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


