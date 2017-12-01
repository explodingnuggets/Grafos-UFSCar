import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start):
    # Initialize all nodes to white color, infinite distance and no parent
    for node in graph:
        nx.set_node_attributes(graph, 'color', 'white')
        nx.set_node_attributes(graph, 'min_dist', float('inf'))
        nx.set_node_attributes(graph, 'parent', None)

    # Initialize starting node to gray color, 0 distance
    
    nx.set_node_attributes(graph, 'color', {start:'gray'})
    nx.set_node_attributes(graph, 'min_dist', {start:0})

    # Initialize the queue and push the starting node into it
    Q = []
    Q.append(start)
    while len(Q) > 0:
        curr = Q.pop()
        for nbr in nx.all_neighbors(graph, curr):
            if graph.node[nbr]['color'] == 'white':
                nx.set_node_attributes(graph, 'min_dist', {nbr:graph.node[curr]['min_dist'] + 1})
                nx.set_node_attributes(graph, 'color', {nbr:'gray'})
                nx.set_node_attributes(graph, 'parent', {nbr:curr})
                Q.append(nbr)
        nx.set_node_attributes(graph, 'color', {curr:'black'})
    
    # Build the resulting tree
    tree = nx.DiGraph()

    # Insert starting node
    tree.add_node(start)

    # Insert remaining nodes
    for n in graph:
        tree.add_edge(graph.node[n]['parent'], n)

    return tree
