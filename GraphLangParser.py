# Generated from GraphLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,49,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,3,1,20,8,1,1,1,1,1,1,2,1,2,1,2,5,2,27,8,2,
        10,2,12,2,30,9,2,1,3,1,3,5,3,34,8,3,10,3,12,3,37,9,3,1,4,1,4,1,4,
        1,4,3,4,43,8,4,1,5,1,5,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,46,0,12,
        1,0,0,0,2,15,1,0,0,0,4,23,1,0,0,0,6,31,1,0,0,0,8,38,1,0,0,0,10,44,
        1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,5,1,0,0,16,
        17,5,2,0,0,17,19,5,3,0,0,18,20,3,4,2,0,19,18,1,0,0,0,19,20,1,0,0,
        0,20,21,1,0,0,0,21,22,5,4,0,0,22,3,1,0,0,0,23,28,3,6,3,0,24,25,5,
        5,0,0,25,27,3,6,3,0,26,24,1,0,0,0,27,30,1,0,0,0,28,26,1,0,0,0,28,
        29,1,0,0,0,29,5,1,0,0,0,30,28,1,0,0,0,31,35,5,11,0,0,32,34,3,8,4,
        0,33,32,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,7,1,
        0,0,0,37,35,1,0,0,0,38,39,5,6,0,0,39,40,5,11,0,0,40,42,5,7,0,0,41,
        43,3,10,5,0,42,41,1,0,0,0,42,43,1,0,0,0,43,9,1,0,0,0,44,45,5,8,0,
        0,45,46,5,11,0,0,46,47,5,9,0,0,47,11,1,0,0,0,4,19,28,35,42
    ]

class GraphLangParser ( Parser ):

    grammarFileName = "GraphLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def'", "'graph'", "'('", "')'", "','", 
                     "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WS", "INT" ]

    RULE_prog = 0
    RULE_defGraph = 1
    RULE_nodeList = 2
    RULE_node = 3
    RULE_conn = 4
    RULE_weight = 5

    ruleNames =  [ "prog", "defGraph", "nodeList", "node", "conn", "weight" ]

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
    WS=10
    INT=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defGraph(self):
            return self.getTypedRuleContext(GraphLangParser.DefGraphContext,0)


        def EOF(self):
            return self.getToken(GraphLangParser.EOF, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = GraphLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.defGraph()
            self.state = 13
            self.match(GraphLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefGraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nodeList(self):
            return self.getTypedRuleContext(GraphLangParser.NodeListContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_defGraph

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefGraph" ):
                listener.enterDefGraph(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefGraph" ):
                listener.exitDefGraph(self)




    def defGraph(self):

        localctx = GraphLangParser.DefGraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defGraph)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.match(GraphLangParser.T__0)
            self.state = 16
            self.match(GraphLangParser.T__1)
            self.state = 17
            self.match(GraphLangParser.T__2)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 18
                self.nodeList()


            self.state = 21
            self.match(GraphLangParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.NodeContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.NodeContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_nodeList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNodeList" ):
                listener.enterNodeList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNodeList" ):
                listener.exitNodeList(self)




    def nodeList(self):

        localctx = GraphLangParser.NodeListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nodeList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.node()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 24
                self.match(GraphLangParser.T__4)
                self.state = 25
                self.node()
                self.state = 30
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphLangParser.INT, 0)

        def conn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GraphLangParser.ConnContext)
            else:
                return self.getTypedRuleContext(GraphLangParser.ConnContext,i)


        def getRuleIndex(self):
            return GraphLangParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = GraphLangParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(GraphLangParser.INT)
            self.state = 35
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==6:
                self.state = 32
                self.conn()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphLangParser.INT, 0)

        def weight(self):
            return self.getTypedRuleContext(GraphLangParser.WeightContext,0)


        def getRuleIndex(self):
            return GraphLangParser.RULE_conn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConn" ):
                listener.enterConn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConn" ):
                listener.exitConn(self)




    def conn(self):

        localctx = GraphLangParser.ConnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(GraphLangParser.T__5)
            self.state = 39
            self.match(GraphLangParser.INT)
            self.state = 40
            self.match(GraphLangParser.T__6)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 41
                self.weight()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeightContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(GraphLangParser.INT, 0)

        def getRuleIndex(self):
            return GraphLangParser.RULE_weight

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeight" ):
                listener.enterWeight(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeight" ):
                listener.exitWeight(self)




    def weight(self):

        localctx = GraphLangParser.WeightContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_weight)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(GraphLangParser.T__7)
            self.state = 45
            self.match(GraphLangParser.INT)
            self.state = 46
            self.match(GraphLangParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





