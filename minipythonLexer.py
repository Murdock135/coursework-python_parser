# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\f")
        buf.write("E\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\63\n\b\3\t")
        buf.write("\6\t\66\n\t\r\t\16\t\67\3\n\6\n;\n\n\r\n\16\n<\3\13\6")
        buf.write("\13@\n\13\r\13\16\13A\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\3\2\t\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\'\',,\61\61\4\2--//\4\2\f\f\17\17\3\2\62")
        buf.write(";\4\2\13\13\"\"M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\31\3")
        buf.write("\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13$\3\2\2\2\r&\3\2\2")
        buf.write("\2\17\62\3\2\2\2\21\65\3\2\2\2\23:\3\2\2\2\25?\3\2\2\2")
        buf.write("\27\30\7?\2\2\30\4\3\2\2\2\31\32\7*\2\2\32\6\3\2\2\2\33")
        buf.write("\34\7+\2\2\34\b\3\2\2\2\35!\t\2\2\2\36 \t\3\2\2\37\36")
        buf.write("\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\n\3\2\2\2")
        buf.write("#!\3\2\2\2$%\t\4\2\2%\f\3\2\2\2&\'\t\5\2\2\'\16\3\2\2")
        buf.write("\2()\7?\2\2)\63\7?\2\2*+\7#\2\2+\63\7?\2\2,\63\7>\2\2")
        buf.write("-.\7>\2\2.\63\7?\2\2/\63\7@\2\2\60\61\7@\2\2\61\63\7?")
        buf.write("\2\2\62(\3\2\2\2\62*\3\2\2\2\62,\3\2\2\2\62-\3\2\2\2\62")
        buf.write("/\3\2\2\2\62\60\3\2\2\2\63\20\3\2\2\2\64\66\t\6\2\2\65")
        buf.write("\64\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\22")
        buf.write("\3\2\2\29;\t\7\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2")
        buf.write("\2\2=\24\3\2\2\2>@\t\b\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2")
        buf.write("\2AB\3\2\2\2BC\3\2\2\2CD\b\13\2\2D\26\3\2\2\2\b\2!\62")
        buf.write("\67<A\3\b\2\2")
        return buf.getvalue()


class minipythonLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    OP_1 = 5
    OP_2 = 6
    OP_3 = 7
    NEWLINE = 8
    INT = 9
    WS = 10

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "OP_1", "OP_2", "OP_3", "NEWLINE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "ID", "OP_1", "OP_2", "OP_3", 
                  "NEWLINE", "INT", "WS" ]

    grammarFileName = "minipython.g4"

    def __init__(self, input=None):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


