import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt
#from bfs import bfs
#from dfs import dfs

# Load Graphs from .paj
G_karate = nx.read_pajek('karate.paj')
G_dolphins = nx.read_pajek('dolphins.paj')

# Store NetworkX's results in a tuple for later comparing
NX_res_karate = []
NX_res_dolphins = []
NX_results = (NX_res_karate, NX_res_dolphins)

# Generate BFS and DFS for both Graphs using NetworkX's methods on the first Node of each
karate_bfs = nx.bfs_tree(G_karate, '1')
karate_dfs = nx.dfs_tree(G_karate, '1')

dolphins_bfs = nx.bfs_tree(G_dolphins, '0')
dolphins_dfs = nx.dfs_tree(G_dolphins, '0')

# Store results in each Graph's list
NX_res_karate.append(karate_bfs)
NX_res_karate.append(karate_dfs)

NX_res_dolphins.append(dolphins_bfs)
NX_res_dolphins.append(dolphins_dfs)

# Save results in AGraph Dot format

path = "karate_bfs_nx.dot"
nx.drawing.nx_agraph.write_dot(NX_results[0][0], path)
path = "karate_dfs_nx.dot"
nx.drawing.nx_agraph.write_dot(NX_results[0][1], path)
path = "dolphins_bfs_nx.dot"
nx.drawing.nx_agraph.write_dot(NX_results[1][0], path)
path = "dolphins_dfs_nx.dot"
nx.drawing.nx_agraph.write_dot(NX_results[1][1], path)
