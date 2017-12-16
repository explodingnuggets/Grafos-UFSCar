import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def twice_around(G, origin = 0):
    # Make MST from original Graph
    H = nx.minimum_spanning_tree(G) 
    H = nx.MultiGraph(H)
    
    # Double the edges in the MST
    H_copy = H.copy()
    for u,v in H_copy.edges():
        H.add_edge(u,v)
    
    # Generate Eulerian Circuit
    euler = list(nx.eulerian_circuit(H, origin))

    I = nx.Graph()
    aux = []
    for u,v in euler: 
        aux.append(u)
        aux.append(v)
    h = []
    # Remove repeating nodes
    for i in aux: 
        if (i not in h):
            h.append(i)
    h.append(origin)

    for i in range (30):
        I.add_edge(h[i],h[i+1])
        I[h[i]][h[i+1]]['weight'] = G[h[i]][h[i+1]]['weight']
    
    return I

def main():
    M = np.loadtxt('./ha30_dist.txt')
    G = nx.from_numpy_matrix(M)
    T = twice_around(G)
    nx.draw_networkx(T)
    plt.savefig('twice_around.png')

main()
