import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from prim import prim

adj_matrix = np.loadtxt('ha30_dist.txt')
G = nx.from_numpy_matrix(adj_matrix)

mst_nx = nx.minimum_spanning_tree(G, algorithm='prim')
mst_out = prim(G)

# Networkx standard Prim implementation
nx.drawing.nx_agraph.write_dot(mst_nx, 'ha30_nx.dot')

# Our Prim implementation
nx.drawing.nx_agraph.write_dot(mst_out, 'ha30_our.dot')
