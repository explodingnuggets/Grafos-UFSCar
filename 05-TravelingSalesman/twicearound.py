import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def twice_around(G, origin = 0):
    H = nx.minimum_spanning_tree(G) # gero a mst a partir do grafo original
    H = nx.MultiGraph(H) # como somente multigrafos aceitam arestas paralelas
    
    H_copy = H.copy()
    for u,v in H_copy.edges():
        H.add_edge(u,v)     #duplico arestas da mst
    
    euleraux = list(nx.eulerian_circuit(H, origin)) # gero um circuito euleriano
    I = nx.Graph()
    aux = []
    for u,v in euleraux: 
        aux.append(u)
        aux.append(v)
    h = []
    for i in aux: 
        if (i not in h):    # elimino repeticoes
            h.append(i)
    h.append(origin)
    for i in range (30):
        I.add_edge(h[i],h[i+1]) # gero grafo resultante
        I[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight'] # copiando tambem o peso
    
    return I

k = nx.complete_graph(10)
#nx.draw(k)
M = np.loadtxt('./Documents/graph/ha30_dist.txt')
G = nx.from_numpy_matrix(M)
#nx.draw(G)
T = twice_around(G)
nx.draw_networkx(T)
plt.show()
