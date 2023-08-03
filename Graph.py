import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create an empty weighted graph
G = nx.Graph()

# Step 2: Add nodes to the graph
G.add_nodes_from(['Node1', 'Node2', 'Node3', 'Node4'])

# Step 3: Add weighted edges to the graph
edges = [('Node1', 'Node2', 5), ('Node2', 'Node3', 3), ('Node3', 'Node4', 7), ('Node4', 'Node1', 2)]
G.add_weighted_edges_from(edges)

# Step 4: Accessing the weights of edges
weight_1_2 = G['Node1']['Node2']['weight']
weight_2_3 = G['Node2']['Node3']['weight']
weight_3_4 = G['Node3']['Node4']['weight']
weight_4_1 = G['Node4']['Node1']['weight']

# Step 5: Visualizing the graph
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()