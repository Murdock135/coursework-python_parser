# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\30")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\7\3\23\n\3\f\3\16\3\26\13\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\5\4\37\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5,\n\5\f\5\16\5/\13\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5?\13\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5L\n\5")
        buf.write("\f\5\16\5O\13\5\5\5Q\n\5\3\5\3\5\3\5\5\5V\n\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5a\n\5\f\5\16\5d\13\5\3")
        buf.write("\6\3\6\3\6\2\3\b\7\2\4\6\b\n\2\3\4\2\f\r\20\21r\2\f\3")
        buf.write("\2\2\2\4\24\3\2\2\2\6\36\3\2\2\2\bU\3\2\2\2\ne\3\2\2\2")
        buf.write("\f\r\5\4\3\2\r\16\7\2\2\3\16\3\3\2\2\2\17\20\5\6\4\2\20")
        buf.write("\21\7\27\2\2\21\23\3\2\2\2\22\17\3\2\2\2\23\26\3\2\2\2")
        buf.write("\24\22\3\2\2\2\24\25\3\2\2\2\25\5\3\2\2\2\26\24\3\2\2")
        buf.write("\2\27\30\7\f\2\2\30\31\7\3\2\2\31\37\5\b\5\2\32\37\5\b")
        buf.write("\5\2\33\34\7\f\2\2\34\35\7\25\2\2\35\37\5\b\5\2\36\27")
        buf.write("\3\2\2\2\36\32\3\2\2\2\36\33\3\2\2\2\37\7\3\2\2\2 V\b")
        buf.write("\5\1\2!\"\7\4\2\2\"#\5\b\5\2#$\7\5\2\2$V\3\2\2\2%&\7\4")
        buf.write("\2\2&\'\5\b\5\2\'(\7\6\2\2(-\5\b\5\2)*\7\6\2\2*,\5\b\5")
        buf.write("\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2")
        buf.write("/-\3\2\2\2\60\61\7\5\2\2\61V\3\2\2\2\62\63\7\4\2\2\63")
        buf.write("\64\5\b\5\2\64\65\7\6\2\2\65\66\7\5\2\2\66V\3\2\2\2\67")
        buf.write("8\7\7\2\28=\5\b\5\29:\7\6\2\2:<\5\b\5\2;9\3\2\2\2<?\3")
        buf.write("\2\2\2=;\3\2\2\2=>\3\2\2\2>@\3\2\2\2?=\3\2\2\2@A\7\b\2")
        buf.write("\2AV\3\2\2\2BC\7\t\2\2CD\5\b\5\2DP\7\n\2\2EM\5\b\5\2F")
        buf.write("G\7\6\2\2GH\5\b\5\2HI\7\n\2\2IJ\5\b\5\2JL\3\2\2\2KF\3")
        buf.write("\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NQ\3\2\2\2OM\3\2\2")
        buf.write("\2PE\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\13\2\2SV\3\2\2\2")
        buf.write("TV\5\n\6\2U \3\2\2\2U!\3\2\2\2U%\3\2\2\2U\62\3\2\2\2U")
        buf.write("\67\3\2\2\2UB\3\2\2\2UT\3\2\2\2Vb\3\2\2\2WX\f\13\2\2X")
        buf.write("Y\7\22\2\2Ya\5\b\5\fZ[\f\n\2\2[\\\7\23\2\2\\a\5\b\5\13")
        buf.write("]^\f\t\2\2^_\7\24\2\2_a\5\b\5\n`W\3\2\2\2`Z\3\2\2\2`]")
        buf.write("\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2c\t\3\2\2\2db\3")
        buf.write("\2\2\2ef\t\2\2\2f\13\3\2\2\2\13\24\36-=MPU`b")
        return buf.getvalue()


class minipythonParser ( Parser ):

    grammarFileName = "minipython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','", "'['", "']'", 
                     "'{'", "':'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "FLOAT", 
                      "INT", "BOOL", "STRING", "OP_1", "OP_2", "OP_3", "COMPOUND_OP", 
                      "COMMENT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_atom = 4

    ruleNames =  [ "prog", "block", "statement", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUMBER=11
    FLOAT=12
    INT=13
    BOOL=14
    STRING=15
    OP_1=16
    OP_2=17
    OP_3=18
    COMPOUND_OP=19
    COMMENT=20
    NEWLINE=21
    WS=22

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(minipythonParser.BlockContext,0)


        def EOF(self):
            return self.getToken(minipythonParser.EOF, 0)

        def getRuleIndex(self):
            return minipythonParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = minipythonParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.block()
            self.state = 11
            self.match(minipythonParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(minipythonParser.StatementContext)
            else:
                return self.getTypedRuleContext(minipythonParser.StatementContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(minipythonParser.NEWLINE)
            else:
                return self.getToken(minipythonParser.NEWLINE, i)

        def getRuleIndex(self):
            return minipythonParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = minipythonParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 13
                    self.statement()
                    self.state = 14
                    self.match(minipythonParser.NEWLINE) 
                self.state = 20
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(minipythonParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(minipythonParser.ExprContext,0)


        def COMPOUND_OP(self):
            return self.getToken(minipythonParser.COMPOUND_OP, 0)

        def getRuleIndex(self):
            return minipythonParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = minipythonParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(minipythonParser.ID)
                self.state = 22
                self.match(minipythonParser.T__0)
                self.state = 23
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.expr(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.match(minipythonParser.ID)
                self.state = 26
                self.match(minipythonParser.COMPOUND_OP)
                self.state = 27
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(minipythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(minipythonParser.ExprContext,i)


        def atom(self):
            return self.getTypedRuleContext(minipythonParser.AtomContext,0)


        def OP_1(self):
            return self.getToken(minipythonParser.OP_1, 0)

        def OP_2(self):
            return self.getToken(minipythonParser.OP_2, 0)

        def OP_3(self):
            return self.getToken(minipythonParser.OP_3, 0)

        def getRuleIndex(self):
            return minipythonParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = minipythonParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 31
                self.match(minipythonParser.T__1)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 3:
                self.state = 35
                self.match(minipythonParser.T__1)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(minipythonParser.T__3)
                self.state = 38
                self.expr(0)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==minipythonParser.T__3:
                    self.state = 39
                    self.match(minipythonParser.T__3)
                    self.state = 40
                    self.expr(0)
                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 46
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 4:
                self.state = 48
                self.match(minipythonParser.T__1)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(minipythonParser.T__3)
                self.state = 51
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 5:
                self.state = 53
                self.match(minipythonParser.T__4)
                self.state = 54
                self.expr(0)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==minipythonParser.T__3:
                    self.state = 55
                    self.match(minipythonParser.T__3)
                    self.state = 56
                    self.expr(0)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 62
                self.match(minipythonParser.T__5)
                pass

            elif la_ == 6:
                self.state = 64
                self.match(minipythonParser.T__6)
                self.state = 65
                self.expr(0)
                self.state = 66
                self.match(minipythonParser.T__7)
                self.state = 78
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 67
                    self.expr(0)
                    self.state = 75
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==minipythonParser.T__3:
                        self.state = 68
                        self.match(minipythonParser.T__3)
                        self.state = 69
                        self.expr(0)
                        self.state = 70
                        self.match(minipythonParser.T__7)
                        self.state = 71
                        self.expr(0)
                        self.state = 77
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 80
                self.match(minipythonParser.T__8)
                pass

            elif la_ == 7:
                self.state = 82
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 96
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 94
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 85
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 86
                        self.match(minipythonParser.OP_1)
                        self.state = 87
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 88
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 89
                        self.match(minipythonParser.OP_2)
                        self.state = 90
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 91
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 92
                        self.match(minipythonParser.OP_3)
                        self.state = 93
                        self.expr(8)
                        pass

             
                self.state = 98
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(minipythonParser.NUMBER, 0)

        def ID(self):
            return self.getToken(minipythonParser.ID, 0)

        def STRING(self):
            return self.getToken(minipythonParser.STRING, 0)

        def BOOL(self):
            return self.getToken(minipythonParser.BOOL, 0)

        def getRuleIndex(self):
            return minipythonParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = minipythonParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << minipythonParser.ID) | (1 << minipythonParser.NUMBER) | (1 << minipythonParser.BOOL) | (1 << minipythonParser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




