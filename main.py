import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from GraphLangLexer import GraphLangLexer
from GraphLangParser import GraphLangParser

GRAPH_TEMPLATE = '''\
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {{node: [] for node in nodes}}  # lista de adjacência: (dest, peso)
        self.node_index = {{node: idx for idx, node in enumerate(nodes)}}
        self.size = len(nodes)
        self.adj_matrix = [[0]*self.size for _ in range(self.size)]

    def add_edge(self, u, v, weight=1):
        self.adj[u].append((v, weight))
        # Atualiza matriz
        i, j = self.node_index[u], self.node_index[v]
        self.adj_matrix[i][j] = weight

    def print_adj_list(self):
        print("Lista de adjacência:")
        for node in self.nodes:
            edges_str = ', '.join(f"({{dest}}, peso={{peso}})" for dest, peso in self.adj[node])
            print(f"{{node}}: [{{edges_str}}]")

    def print_adj_matrix(self):
        print("\\nMatriz de adjacência (0 significa sem ligação):")
        print("   " + " ".join(str(n) for n in self.nodes))
        for i, row in enumerate(self.adj_matrix):
            print(f"{{self.nodes[i]}}: " + " ".join(str(x) for x in row))

    def draw_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(self.nodes)
        
        # Dicionário para armazenar labels customizados para arestas bidirecionais
        custom_edge_labels = {{}}
        
        for u in self.adj:
            for v, w in self.adj[u]:
                G.add_edge(u, v, weight=w)
                
                # Verifica se há aresta reversa para criar label bidirecional
                reverse_weight = None
                for dest, peso in self.adj.get(v, []):
                    if dest == u:
                        reverse_weight = peso
                        break
                
                # Cria label apropriado
                if reverse_weight is not None and (v, u) not in custom_edge_labels:
                    # Aresta bidirecional - mostra ambos os pesos
                    custom_edge_labels[(u, v)] = f"{{w}}/{{reverse_weight}}"
                elif (v, u) not in custom_edge_labels:
                    # Aresta unidirecional
                    custom_edge_labels[(u, v)] = str(w)

        pos = nx.spring_layout(G, seed=42)  # seed para layout consistente
        
        # Desenha o grafo
        nx.draw(G, pos, with_labels=True, node_color='lightgreen', 
                node_size=700, arrowsize=20, font_size=16, font_weight='bold')
        
        # Adiciona labels das arestas
        nx.draw_networkx_edge_labels(G, pos, edge_labels=custom_edge_labels, font_size=12)
        
        plt.title("Visualização do Grafo Direcionado com Pesos")
        plt.show()

if __name__ == "__main__":
    nodes = {nodes}
    edges = {edges}  # formato: {{u: [(v, peso), ...], ...}}

    graph = Graph(nodes)

    for u in edges:
        for v, w in edges[u]:
            graph.add_edge(u, v, w)

    graph.print_adj_list()
    graph.print_adj_matrix()
    graph.draw_graph()
'''

class MyErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.has_error = False
        
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.has_error = True
        print(f"Erro de parsing na linha {line}, coluna {column}: {msg}")
        if offendingSymbol:
            print(f"Token problemático: '{offendingSymbol.text}' (tipo: {offendingSymbol.type})")

def extract_graph_info(tree):
    nodes = []
    edges = {}
    defGraph = tree.getChild(0)
    nodeList = defGraph.getChild(3) if defGraph.getChildCount() > 4 else None
    if nodeList:
        for i in range(nodeList.getChildCount()):
            node_child = nodeList.getChild(i)
            if node_child.getChildCount() >= 1:
                node_val = int(node_child.getChild(0).getText())
                if node_val not in nodes:
                    nodes.append(node_val)
                edges.setdefault(node_val, [])
                for c_i in range(1, node_child.getChildCount()):
                    conn = node_child.getChild(c_i)
                    dest = int(conn.getChild(1).getText())
                    peso = 1
                    if conn.getChildCount() == 4:
                        weight_node = conn.getChild(3)
                        peso = int(weight_node.getChild(1).getText())
                    if dest not in nodes:
                        nodes.append(dest)
                    edges[node_val].append((dest, peso))
    return nodes, edges

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GraphLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphLangParser(stream)
    
    # Adicionar listener de erro personalizado
    error_listener = MyErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.prog()
    
    # Se houve erro de parsing, não continuar
    if error_listener.has_error:
        print("Erro no parsing. Abortando...")
        return
    
    print("Parsing bem-sucedido!")
    print(f"Árvore: {tree.toStringTree(recog=parser)}")

    nodes, edges = extract_graph_info(tree)
    nodes_str = str(nodes)
    edges_str = str(edges)

    code = GRAPH_TEMPLATE.format(nodes=nodes_str, edges=edges_str)

    with open("generated_graph.py", "w", encoding="utf-8") as f:
        f.write(code)

    print("Arquivo 'generated_graph.py' gerado com sucesso!")
    print(f"Nós: {nodes_str}")
    print(f"Arestas: {edges_str}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py arquivo.tl")
    else:
        main(sys.argv)
