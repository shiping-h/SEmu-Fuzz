from semu_fuzz.drl.transition_graph import StateNode
import networkx as nx

blocks = set([1,2,34,5])
address = 123456
node1 = StateNode(blocks, address)
node2 = StateNode(set([1,2,34,5]), address)

graph = nx.DiGraph()

graph.add_node(node1)

print(graph.has_node(node1))
print(node1.blocks == node2.blocks)