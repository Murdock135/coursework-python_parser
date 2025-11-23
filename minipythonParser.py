# Generated from /home/zayan/Documents/code/mine/coursework-python_parser/minipython.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\t")
        buf.write(" \4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\5\3\20\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\33")
        buf.write("\n\3\f\3\16\3\36\13\3\3\3\2\3\4\4\2\4\2\2!\2\6\3\2\2\2")
        buf.write("\4\17\3\2\2\2\6\7\5\4\3\2\7\b\7\2\2\3\b\3\3\2\2\2\t\n")
        buf.write("\b\3\1\2\n\20\7\b\2\2\13\f\7\3\2\2\f\r\5\4\3\2\r\16\7")
        buf.write("\4\2\2\16\20\3\2\2\2\17\t\3\2\2\2\17\13\3\2\2\2\20\34")
        buf.write("\3\2\2\2\21\22\f\7\2\2\22\23\7\5\2\2\23\33\5\4\3\b\24")
        buf.write("\25\f\6\2\2\25\26\7\6\2\2\26\33\5\4\3\7\27\30\f\5\2\2")
        buf.write("\30\31\7\7\2\2\31\33\5\4\3\6\32\21\3\2\2\2\32\24\3\2\2")
        buf.write("\2\32\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3\2")
        buf.write("\2\2\35\5\3\2\2\2\36\34\3\2\2\2\5\17\32\34")
        return buf.getvalue()


class minipythonParser ( Parser ):

    grammarFileName = "minipython.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "OP_1", "OP_2", 
                      "OP_3", "INT", "WS" ]

    RULE_prog = 0
    RULE_expr = 1

    ruleNames =  [ "prog", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    OP_1=3
    OP_2=4
    OP_3=5
    INT=6
    WS=7

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(minipythonParser.ExprContext,0)


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
            self.state = 4
            self.expr(0)
            self.state = 5
            self.match(minipythonParser.EOF)
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

        def INT(self):
            return self.getToken(minipythonParser.INT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(minipythonParser.ExprContext)
            else:
                return self.getTypedRuleContext(minipythonParser.ExprContext,i)


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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [minipythonParser.INT]:
                self.state = 8
                self.match(minipythonParser.INT)
                pass
            elif token in [minipythonParser.T__0]:
                self.state = 9
                self.match(minipythonParser.T__0)
                self.state = 10
                self.expr(0)
                self.state = 11
                self.match(minipythonParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 15
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 16
                        self.match(minipythonParser.OP_1)
                        self.state = 17
                        self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 19
                        self.match(minipythonParser.OP_2)
                        self.state = 20
                        self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = minipythonParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 22
                        self.match(minipythonParser.OP_3)
                        self.state = 23
                        self.expr(4)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
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
         




