import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start):
    # Make a copy of the original graph to work on
    graph_cpy = graph.copy()

    # Initialize all nodes to white color and no parent
    for node in graph_cpy:
        nx.set_node_attributes(graph_cpy, 'white', 'color')
        nx.set_node_attributes(graph_cpy, None, 'parent')

    # Initialize global time
    global time
    time = 0
   
    # Start the DFS traversal in the graph
    dfs_visit(graph_cpy, start)
    
    # Build the resulting tree
    tree = nx.DiGraph()

    # Insert starting node
    tree.add_node(start)

    # Insert remaining nodes
    for n in graph_cpy:
        tree.add_edge(graph_cpy.node[n]['parent'], n)

    return tree

def dfs_visit(graph, cur):
    # Increment time for each call
    global time
    time += 1
    
    # Set time of discovery for each new node and mark as visited
    nx.set_node_attributes(graph, {cur:time}, 'time_discovery')
    nx.set_node_attributes(graph, {cur:'gray'}, 'color')
    
    # Visit all unvisited neighbouring nodes
    for nbr in nx.all_neighbors(graph, cur):
        if graph.node[nbr]['color'] == 'white':
            nx.set_node_attributes(graph, {nbr:cur}, 'parent')
            dfs_visit(graph, nbr)

    # Mark current node as finished and set time of finish
    nx.set_node_attributes(graph, {cur:'black'}, 'color')
    time += 1
    nx.set_node_attributes(graph, {cur:time}, 'time_finish')

