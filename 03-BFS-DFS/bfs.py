import network as nx
import matplotlib.pyplot as plt

def bfs(G, s):
    # Initialize all nodes to white color, infinite distance and no parent
    nx.set_node_attributes(G, 'color', 'white')
    nx.set_node_attributes(G, 'min_dist', float('inf'))
    nx.set_node_attributes(G, 'parent', None)

    # Initialize starting node to gray color, 0 distance
    nx.set_node_attributes(G, 'color', {s:'gray'})
    nx.set_node_attributes(G, 'min_dist', {s:0})

    # Initialize the queue and push the starting node into it
    Q = []
    Q.append(s)
    while len(Q) > 0:
        c = Q.pop()
        for n in nx.all_neighbors(G, c):
            if G[n]['color'] == 'white':
                nx.set_node_attributes(G, 'min_dist', {n:(G[c]['min_dist'] + 1)})
                nx.set_node_attributes(G, 'parent', {n:c})
                nx.set_node_attributes(G, 'color', {n:'gray'})
                Q.append(n)
            nx.set_node_attributes(G, 'color', {c:'black'}

