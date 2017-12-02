import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start):
    # Make a copy of the original graph to work on
    graph_cpy = graph.copy()

    # Initialize all nodes to white color, infinite distance and no parent
    for node in graph_cpy:
        nx.set_node_attributes(graph_cpy, 'color', 'white')
        nx.set_node_attributes(graph_cpy, 'min_dist', float('inf'))
        nx.set_node_attributes(graph_cpy, 'parent', None)

    # Initialize starting node to gray color, 0 distance
    nx.set_node_attributes(graph_cpy, 'color', {start:'gray'})
    nx.set_node_attributes(graph_cpy, 'min_dist', {start:0})

    # Initialize the queue and push the starting node into it
    Q = []
    Q.append(start)
    while len(Q) > 0:
        cur = Q.pop()
        for nbr in nx.all_neighbors(graph_cpy, cur):
            if graph_cpy.node[nbr]['color'] == 'white':
                nx.set_node_attributes(graph_cpy, 'min_dist', {nbr:graph_cpy.node[cur]['min_dist'] + 1})
                nx.set_node_attributes(graph_cpy, 'color', {nbr:'gray'})
                nx.set_node_attributes(graph_cpy, 'parent', {nbr:cur})
                Q.append(nbr)
        nx.set_node_attributes(graph_cpy, 'color', {cur:'black'})
    
    # Build the resulting tree
    tree = nx.DiGraph()

    # Insert starting node
    tree.add_node(start)

    # Insert remaining nodes
    for n in graph_cpy:
        tree.add_edge(graph_cpy.node[n]['parent'], n)

    return tree
