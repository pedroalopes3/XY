import networkx as nx
import matplotlib.pyplot as plt

class graph:

    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight):
        self.graph.add_edge(node1, node2, weight=weight)

    def plot_graph(self):
        pos = nx.spring_layout(self.graph)  # Positions for all nodes
        nx.draw(self.graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=labels)
        plt.show()

"""
# Example usage
my_graph = graph()

my_graph.add_node('A')
my_graph.add_node('B')
my_graph.add_node('C')
my_graph.add_node('D')

my_graph.add_edge('A', 'B', weight=5)
my_graph.add_edge('B', 'C', weight=3)
my_graph.add_edge('C', 'D', weight=7)
my_graph.add_edge('D', 'A', weight=2)

my_graph.plot_graph()
"""