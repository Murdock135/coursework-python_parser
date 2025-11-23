# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\21")
        buf.write("P\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16?\n\16\r\16")
        buf.write("\16\16@\3\17\6\17D\n\17\r\17\16\17E\3\17\3\17\3\20\6\20")
        buf.write("K\n\20\r\20\16\20L\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21\3\2\5\3\2\62;\4\2\f\f\17\17\3\2\13\13R\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3")
        buf.write("\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t\'")
        buf.write("\3\2\2\2\13)\3\2\2\2\r,\3\2\2\2\17/\3\2\2\2\21\61\3\2")
        buf.write("\2\2\23\64\3\2\2\2\25\66\3\2\2\2\279\3\2\2\2\31;\3\2\2")
        buf.write("\2\33>\3\2\2\2\35C\3\2\2\2\37J\3\2\2\2!\"\7,\2\2\"\4\3")
        buf.write("\2\2\2#$\7\61\2\2$\6\3\2\2\2%&\7-\2\2&\b\3\2\2\2\'(\7")
        buf.write("/\2\2(\n\3\2\2\2)*\7?\2\2*+\7?\2\2+\f\3\2\2\2,-\7#\2\2")
        buf.write("-.\7?\2\2.\16\3\2\2\2/\60\7>\2\2\60\20\3\2\2\2\61\62\7")
        buf.write(">\2\2\62\63\7?\2\2\63\22\3\2\2\2\64\65\7@\2\2\65\24\3")
        buf.write("\2\2\2\66\67\7@\2\2\678\7?\2\28\26\3\2\2\29:\7*\2\2:\30")
        buf.write("\3\2\2\2;<\7+\2\2<\32\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2A\34\3\2\2\2BD\t\3\2\2CB\3\2")
        buf.write("\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FG\3\2\2\2GH\b\17\2")
        buf.write("\2H\36\3\2\2\2IK\t\4\2\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2")
        buf.write("LM\3\2\2\2MN\3\2\2\2NO\b\20\2\2O \3\2\2\2\6\2@EL\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class minipythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    INT = 13
    NEWLINE = 14
    WS = 15

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "NEWLINE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "INT", "NEWLINE", 
                  "WS" ]

    grammarFileName = "minipython.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


