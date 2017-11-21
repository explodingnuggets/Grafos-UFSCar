import numpy as np
import networkx as nx
from networkx.drawing.nx_agraph import write_dot
from dijkstra import dijkstra

# Loads adjacency matrix
adj_matrix = np.loadtxt('wg59_dist.txt')
G = nx.from_numpy_matrix(adj_matrix)

# Generates dot file for k=2 multisource dijkstra
mst_k2 = dijkstra(G, sources=2)
write_dot(mst_k2, 'wg59_k2.dot')

# Generates dot file for k=3 multisource dijkstra
mst_k3 = dijkstra(G, sources=3)
write_dot(mst_k3, 'wg59_k3.dot')
