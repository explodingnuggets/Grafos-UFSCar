import matplotlib.pyplot as plt
import networkx as nx

def prim(graph):
    # Initializes color on vertices (white: non-visited, black: visited)
    nx.set_node_attributes(graph, 'white', 'color')
    # Initializes minimum distance to infinite
    nx.set_node_attributes(graph, float('inf'), 'min_dist')
    for node in graph:
        nx.set_node_attributes(graph, {node: 0}, 'min_dist')
        break
    # Initializes parents to None
    nx.set_node_attributes(graph, None, 'parent')
    
    # While exists a node unvisited, continue visiting nodes
    nodes_info = graph.nodes(data=True)
    while any(node[1]['color'] == 'white' for node in nodes_info):
        # Separates white nodes and get the one with smaller lambda
        white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
        min_node = min(white_nodes, key=lambda x: x[1]['min_dist'])

        # Iterates over neighbors to update minimal distances and parents
        for node in graph.neighbors(min_node[0]):
            node_info = (node, nodes_info[node])
            if node_info[1]['color'] == 'white':
                new_dist = graph.get_edge_data(min_node[0], node_info[0])['weight']
                # Checks if new weight is smaller than previous one, if it is, update data
                if new_dist < node_info[1]['min_dist']:
                    nx.set_node_attributes(graph, {node_info[0]: new_dist}, 'min_dist')
                    nx.set_node_attributes(graph, {node_info[0]: min_node[0]}, 'parent')
        nx.set_node_attributes(graph, {min_node[0]: 'black'}, 'color')
        nodes_info = graph.nodes(data=True)

    # Creates minimum spanning tree graph
    mst = nx.DiGraph()

    # Adds all nodes to the new mst graph
    for node in graph.nodes(data=True):
        if node[1]['parent'] != None:
            edge_weight = node[1]['min_dist']
            parent = node[1]['parent']
            mst.add_weighted_edges_from([[parent, node[0], edge_weight]])

    return mst
        

def main():
    # Creates test case graph and adds edges
    G = nx.Graph()
    G.add_weighted_edges_from([[1, 2, 3.0],
                              [2, 3, 5.0],
                              [3, 4, 1.0],
                              [4, 5, 2.0],
                              [1, 4, 1.5],
                              [5, 6, 3.0],
                              [6, 3, 2.0]])
    
    # Applies prim on graph
    mst = prim(G)

    # Plot and shows graph
    pos = nx.spring_layout(G)
    weight_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx(G, pos, with_labels=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels)
    plt.show()

    # Plot and shows minimum spanning tree
    pos = nx.spring_layout(mst)
    weight_labels = nx.get_edge_attributes(mst, 'weight')
    nx.draw_networkx(mst, pos, with_labels=True)
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=weight_labels)
    plt.show()

if __name__ == '__main__':
    # Test case
    main()
