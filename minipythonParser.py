# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\f")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\7\3\21\n\3\f\3\16\3\24\13\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\37\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\3\5\2\3\6\6")
        buf.write("\2\4\6\b\2\3\4\2\6\6\13\13\63\2\n\3\2\2\2\4\22\3\2\2\2")
        buf.write("\6\36\3\2\2\2\b.\3\2\2\2\n\13\5\4\3\2\13\f\7\2\2\3\f\3")
        buf.write("\3\2\2\2\r\16\5\6\4\2\16\17\7\n\2\2\17\21\3\2\2\2\20\r")
        buf.write("\3\2\2\2\21\24\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\5\3\2\2\2\24\22\3\2\2\2\25\37\b\4\1\2\26\27\7\6\2\2\27")
        buf.write("\30\7\3\2\2\30\37\5\6\4\b\31\37\5\b\5\2\32\33\7\4\2\2")
        buf.write("\33\34\5\6\4\2\34\35\7\5\2\2\35\37\3\2\2\2\36\25\3\2\2")
        buf.write("\2\36\26\3\2\2\2\36\31\3\2\2\2\36\32\3\2\2\2\37+\3\2\2")
        buf.write("\2 !\f\7\2\2!\"\7\7\2\2\"*\5\6\4\b#$\f\6\2\2$%\7\b\2\2")
        buf.write("%*\5\6\4\7&\'\f\5\2\2\'(\7\t\2\2(*\5\6\4\6) \3\2\2\2)")
        buf.write("#\3\2\2\2)&\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\7\3")
        buf.write("\2\2\2-+\3\2\2\2./\t\2\2\2/\t\3\2\2\2\6\22\36)+")
        return buf.getvalue()


class minipythonParser ( Parser ):

    grammarFileName = "minipython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "OP_1", "OP_2", "OP_3", "NEWLINE", "INT", "WS" ]

    RULE_prog = 0
    RULE_block = 1
    RULE_expr = 2
    RULE_atom = 3

    ruleNames =  [ "prog", "block", "expr", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    OP_1=5
    OP_2=6
    OP_3=7
    NEWLINE=8
    INT=9
    WS=10

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 20
                self.match(minipythonParser.ID)
                self.state = 21
                self.match(minipythonParser.T__0)
                self.state = 22
                self.expr(6)
                pass

            elif la_ == 3:
                self.state = 23
                self.atom()
                pass

            elif la_ == 4:
                self.state = 24
                self.match(minipythonParser.T__1)
                self.state = 25
                self.expr(0)
                self.state = 26
                self.match(minipythonParser.T__2)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 31
                        self.match(minipythonParser.OP_1)
                        self.state = 32
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        self.match(minipythonParser.OP_2)
                        self.state = 35
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        self.match(minipythonParser.OP_3)
                        self.state = 38
                        self.expr(4)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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

        def INT(self):
            return self.getToken(minipythonParser.INT, 0)

        def ID(self):
            return self.getToken(minipythonParser.ID, 0)

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
            self.state = 44
            _la = self._input.LA(1)
            if not(_la==minipythonParser.ID or _la==minipythonParser.INT):
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
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




