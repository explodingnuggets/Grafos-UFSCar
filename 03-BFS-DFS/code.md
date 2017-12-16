```python
def bfs(graph, start):
    # Make a copy of the original graph to work on
    graph_cpy = graph.copy()

    # Initialize all nodes to white color, infinite distance and no parent
    for node in graph_cpy:
        nx.set_node_attributes(graph_cpy, 'white', 'color')
        nx.set_node_attributes(graph_cpy, float('inf'), 'min_dist')
        nx.set_node_attributes(graph_cpy, None, 'parent')

    # Initialize starting node to gray color, 0 distance
    nx.set_node_attributes(graph_cpy, {start:'gray'}, 'color')
    nx.set_node_attributes(graph_cpy, {start:0}, 'min_dist')

    # Initialize the queue and push the starting node into it
    Q = []
    Q.append(start)
    while len(Q) > 0:
        cur = Q.pop()
        for nbr in nx.all_neighbors(graph_cpy, cur):
            if graph_cpy.node[nbr]['color'] == 'white':
                nx.set_node_attributes(graph_cpy, {nbr:graph_cpy.node[cur]['min_dist'] + 1}, 'min_dist')
                nx.set_node_attributes(graph_cpy, {nbr:'gray'}, 'color')
                nx.set_node_attributes(graph_cpy, {nbr:cur}, 'parent')
                Q.append(nbr)
        nx.set_node_attributes(graph_cpy, {cur:'black'}, 'color')
    
    # Build the resulting tree
    tree = nx.DiGraph()

    # Insert starting node
    tree.add_node(start)

    # Insert remaining nodes
    for n in graph_cpy:
        tree.add_edge(graph_cpy.node[n]['parent'], n)

    return tree
```

```python
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
```

Resultados:
