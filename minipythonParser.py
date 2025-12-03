# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\27")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4$\n\4\f\4\16\4\'")
        buf.write("\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("\64\n\4\f\4\16\4\67\13\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\7\4D\n\4\f\4\16\4G\13\4\5\4I\n\4\3\4\3")
        buf.write("\4\3\4\5\4N\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4Y\n\4\f\4\16\4\\\13\4\3\5\3\5\3\5\2\3\6\6\2\4\6\b\2")
        buf.write("\3\4\2\f\r\20\21j\2\n\3\2\2\2\4\22\3\2\2\2\6M\3\2\2\2")
        buf.write("\b]\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16")
        buf.write("\5\6\4\2\16\17\7\26\2\2\17\21\3\2\2\2\20\r\3\2\2\2\21")
        buf.write("\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23\5\3\2\2\2\24")
        buf.write("\22\3\2\2\2\25N\b\4\1\2\26\27\7\f\2\2\27\30\7\3\2\2\30")
        buf.write("N\5\6\4\f\31\32\7\4\2\2\32\33\5\6\4\2\33\34\7\5\2\2\34")
        buf.write("N\3\2\2\2\35\36\7\4\2\2\36\37\5\6\4\2\37 \7\6\2\2 %\5")
        buf.write("\6\4\2!\"\7\6\2\2\"$\5\6\4\2#!\3\2\2\2$\'\3\2\2\2%#\3")
        buf.write("\2\2\2%&\3\2\2\2&(\3\2\2\2\'%\3\2\2\2()\7\5\2\2)N\3\2")
        buf.write("\2\2*+\7\4\2\2+,\5\6\4\2,-\7\6\2\2-.\7\5\2\2.N\3\2\2\2")
        buf.write("/\60\7\7\2\2\60\65\5\6\4\2\61\62\7\6\2\2\62\64\5\6\4\2")
        buf.write("\63\61\3\2\2\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2")
        buf.write("\2\668\3\2\2\2\67\65\3\2\2\289\7\b\2\29N\3\2\2\2:;\7\t")
        buf.write("\2\2;<\5\6\4\2<H\7\n\2\2=E\5\6\4\2>?\7\6\2\2?@\5\6\4\2")
        buf.write("@A\7\n\2\2AB\5\6\4\2BD\3\2\2\2C>\3\2\2\2DG\3\2\2\2EC\3")
        buf.write("\2\2\2EF\3\2\2\2FI\3\2\2\2GE\3\2\2\2H=\3\2\2\2HI\3\2\2")
        buf.write("\2IJ\3\2\2\2JK\7\13\2\2KN\3\2\2\2LN\5\b\5\2M\25\3\2\2")
        buf.write("\2M\26\3\2\2\2M\31\3\2\2\2M\35\3\2\2\2M*\3\2\2\2M/\3\2")
        buf.write("\2\2M:\3\2\2\2ML\3\2\2\2NZ\3\2\2\2OP\f\13\2\2PQ\7\22\2")
        buf.write("\2QY\5\6\4\fRS\f\n\2\2ST\7\23\2\2TY\5\6\4\13UV\f\t\2\2")
        buf.write("VW\7\24\2\2WY\5\6\4\nXO\3\2\2\2XR\3\2\2\2XU\3\2\2\2Y\\")
        buf.write("\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\7\3\2\2\2\\Z\3\2\2\2]^\t")
        buf.write("\2\2\2^\t\3\2\2\2\n\22%\65EHMXZ")
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
                      "INT", "BOOL", "STRING", "OP_1", "OP_2", "OP_3", "COMMENT", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "block", "expr", "atom" ]

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
    COMMENT=19
    NEWLINE=20
    WS=21

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
            self.state = 8
            self.block()
            self.state = 9
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(minipythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(minipythonParser.ExprContext,i)


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
            self.state = 16
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 11
                    self.expr(0)
                    self.state = 12
                    self.match(minipythonParser.NEWLINE) 
                self.state = 18
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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

        def ID(self):
            return self.getToken(minipythonParser.ID, 0)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 20
                self.match(minipythonParser.ID)
                self.state = 21
                self.match(minipythonParser.T__0)
                self.state = 22
                self.expr(10)
                pass

            elif la_ == 3:
                self.state = 23
                self.match(minipythonParser.T__1)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 4:
                self.state = 27
                self.match(minipythonParser.T__1)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(minipythonParser.T__3)
                self.state = 30
                self.expr(0)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==minipythonParser.T__3:
                    self.state = 31
                    self.match(minipythonParser.T__3)
                    self.state = 32
                    self.expr(0)
                    self.state = 37
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 38
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 5:
                self.state = 40
                self.match(minipythonParser.T__1)
                self.state = 41
                self.expr(0)
                self.state = 42
                self.match(minipythonParser.T__3)
                self.state = 43
                self.match(minipythonParser.T__2)
                pass

            elif la_ == 6:
                self.state = 45
                self.match(minipythonParser.T__4)
                self.state = 46
                self.expr(0)
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==minipythonParser.T__3:
                    self.state = 47
                    self.match(minipythonParser.T__3)
                    self.state = 48
                    self.expr(0)
                    self.state = 53
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 54
                self.match(minipythonParser.T__5)
                pass

            elif la_ == 7:
                self.state = 56
                self.match(minipythonParser.T__6)
                self.state = 57
                self.expr(0)
                self.state = 58
                self.match(minipythonParser.T__7)
                self.state = 70
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 59
                    self.expr(0)
                    self.state = 67
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==minipythonParser.T__3:
                        self.state = 60
                        self.match(minipythonParser.T__3)
                        self.state = 61
                        self.expr(0)
                        self.state = 62
                        self.match(minipythonParser.T__7)
                        self.state = 63
                        self.expr(0)
                        self.state = 69
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 72
                self.match(minipythonParser.T__8)
                pass

            elif la_ == 8:
                self.state = 74
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 86
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 77
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 78
                        self.match(minipythonParser.OP_1)
                        self.state = 79
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 80
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 81
                        self.match(minipythonParser.OP_2)
                        self.state = 82
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 83
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 84
                        self.match(minipythonParser.OP_3)
                        self.state = 85
                        self.expr(8)
                        pass

             
                self.state = 90
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self.enterRule(localctx, 6, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
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
        self._predicates[2] = self.expr_sempred
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
         




