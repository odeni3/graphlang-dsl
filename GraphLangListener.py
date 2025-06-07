# Generated from GraphLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphLangParser import GraphLangParser
else:
    from GraphLangParser import GraphLangParser

# This class defines a complete listener for a parse tree produced by GraphLangParser.
class GraphLangListener(ParseTreeListener):

    # Enter a parse tree produced by GraphLangParser#prog.
    def enterProg(self, ctx:GraphLangParser.ProgContext):
        pass

    # Exit a parse tree produced by GraphLangParser#prog.
    def exitProg(self, ctx:GraphLangParser.ProgContext):
        pass


    # Enter a parse tree produced by GraphLangParser#defGraph.
    def enterDefGraph(self, ctx:GraphLangParser.DefGraphContext):
        pass

    # Exit a parse tree produced by GraphLangParser#defGraph.
    def exitDefGraph(self, ctx:GraphLangParser.DefGraphContext):
        pass


    # Enter a parse tree produced by GraphLangParser#nodeList.
    def enterNodeList(self, ctx:GraphLangParser.NodeListContext):
        pass

    # Exit a parse tree produced by GraphLangParser#nodeList.
    def exitNodeList(self, ctx:GraphLangParser.NodeListContext):
        pass


    # Enter a parse tree produced by GraphLangParser#node.
    def enterNode(self, ctx:GraphLangParser.NodeContext):
        pass

    # Exit a parse tree produced by GraphLangParser#node.
    def exitNode(self, ctx:GraphLangParser.NodeContext):
        pass


    # Enter a parse tree produced by GraphLangParser#conn.
    def enterConn(self, ctx:GraphLangParser.ConnContext):
        pass

    # Exit a parse tree produced by GraphLangParser#conn.
    def exitConn(self, ctx:GraphLangParser.ConnContext):
        pass


    # Enter a parse tree produced by GraphLangParser#weight.
    def enterWeight(self, ctx:GraphLangParser.WeightContext):
        pass

    # Exit a parse tree produced by GraphLangParser#weight.
    def exitWeight(self, ctx:GraphLangParser.WeightContext):
        pass



del GraphLangParser