import networkx as nx
import pygraphviz
import matplotlib.pyplot as plt
from bfs import bfs
from dfs import dfs

# Load graphs from .paj
G_karate = nx.read_pajek('karate.paj')
G_dolphins = nx.read_pajek('dolphins.paj')

# Generate BFS and DFS for both graphs using NetworkX's methods on the first node of each
nx_karate_bfs = [nx.bfs_tree(G_karate, '1'), "karate_bfs_nx.dot"]
nx_karate_dfs = [nx.dfs_tree(G_karate, '1'), "karate_dfs_nx.dot"]
nx_dolphins_bfs = [nx.bfs_tree(G_dolphins, '0'), "dolphins_bfs_nx.dot"]
nx_dolphins_dfs = [nx.dfs_tree(G_dolphins, '0'), "dolphins_dfs_nx.dot"]

# Generate BFS and DFS using our methods on the first node of each
our_karate_bfs = [bfs(G_karate, '1'), "karate_bfs_our.dot"]
our_karate_dfs = [dfs(G_karate, '1'), "karate_dfs_our.dot"]
our_dolphins_bfs = [bfs(G_dolphins, '0'), "dolphins_bfs_our.dot"]
our_dolphins_dfs = [dfs(G_dolphins, '0'), "dolphins_dfs_our.dot"]

# Store NetworkX's results in a tuple for later comparing
NX_results = (nx_karate_bfs, nx_karate_dfs, nx_dolphins_bfs, nx_dolphins_dfs)

# Store our results in another tuple
Our_results = (our_karate_bfs, our_karate_dfs, our_dolphins_bfs, our_dolphins_dfs)

# Save results in AGraph Dot format
for graph in NX_results:
    nx.drawing.nx_agraph.write_dot(graph[0], graph[1])
for graph in Our_results:
    nx.drawing.nx_agraph.write_dot(graph[0], graph[1])

nx.draw_networkx(our_karate_dfs[0])
plt.show()
nx.draw_networkx(our_karate_bfs[0])
plt.show()
