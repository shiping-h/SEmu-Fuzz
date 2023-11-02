import networkx as nx

class TransitionGraph():
    def __init__(self):
        self.graph = nx.DiGraph()
        self.nodes = self.graph.nodes
        self.edges = self.graph.edges

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, u, v, data):
        datas = set()
        datas.add(data)
        self.graph.add_edge(u, v, datas=datas)

    def has_node(self, node):
        nodes = self.graph.nodes
        for n in nodes:
            if n.blocks == node.blocks and n.reg_address == node.reg_address:
                return n
        return None

    def has_edge(self, u, v):
        return self.graph.has_edge(u, v)

    def update_edge(self, u, v, data):
        self.graph.edges[u, v]["datas"].add(data)

    def number_of_nodes(self):
        return self.graph.number_of_nodes()
    
    def number_of_edges(self):
        return self.graph.number_of_edges()
    
    def get_edge_data(self, edge):
        return self.graph.get_edge_data(edge[0], edge[1])



    
class StateNode():
    def __init__(self, blocks, reg_address):
        self.blocks = blocks
        self.reg_address = reg_address

    def get_blocks(self):
        return self.blocks
    
    def get_reg_address(self):
        return self.reg_address
    
    # def __eq__(self, other):
    #     if isinstance(other, StateNode):
    #         return self.blocks == other.blocks and self.reg_address == other.reg_address
    #     else:
    #         return False
    
