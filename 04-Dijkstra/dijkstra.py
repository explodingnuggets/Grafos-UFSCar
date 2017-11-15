#!/bin/python
import matplotlib.pyplot as plt
import networkx as nx

import random

def dijkstra(graph, sources=1):
    # Initializes nodes color (white: unvisited, black: visited)
    nx.set_node_attributes(graph, 'white', 'color')
    # Initializes nodes minimum distance
    nx.set_node_attributes(graph, float('inf'), 'min_dist')
    # Selects n random elements to start (minimum distance = 0)
    nodes = random.sample(graph.nodes, sources)
    for node in nodes:
        nx.set_node_attributes(graph, {node: 0}, 'min_dist')        
    # Initializes nodes ancestors
    nx.set_node_attributes(graph, None, 'ancestor')

    # While exists a node unvisited, continue visiting nodes
    nodes_info = graph.nodes(data=True)
    while any(node[1]['color'] == 'white' for node in nodes_info):
        # Separates white nodes, and gets the one with smallest minimum distance
        white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
        min_node = min(white_nodes, key=lambda x: x[1]['min_dist'])        
    
        # Iterates over neighbors to update minimal distances and parents
        for node in graph.neighbors(min_node[0]):
            node_info = (node, nodes_info[node])
            if node_info[1]['color'] == 'white':
                new_dist = graph.get_edge_data(min_node[0], node_info[0])['weight'] + min_node[1]['min_dist']
                if new_dist < node_info[1]['min_dist']:
                    nx.set_node_attributes(graph, {node_info[0]: new_dist}, 'min_dist')
                    nx.set_node_attributes(graph, {node_info[0]: min_node[0]}, 'ancestor')
        nx.set_node_attributes(graph, {min_node[0]: 'black'}, 'color')
        nodes_info = graph.nodes(data=True)

    # Creates new graph
    tree = nx.Graph()

    for node in graph.nodes(data=True):
        if node[1]['ancestor'] != None:
            edge_weight = graph.get_edge_data(node[0], node[1]['ancestor'])
            ancestor = node[1]['ancestor']
            tree.add_weighted_edges_from([[ancestor, node[0], edge_weight]])

    return tree

def main():
    G = nx.Graph()
    G.add_weighted_edges_from([[1, 2, 2],
                               [1, 3, 8],
                               [1, 6, 14],
                               [2, 3, 6],
                               [2, 5, 5],
                               [3, 4, 3],
                               [4, 5, 5],
                               [4, 6, 6],
                               [5, 6, 8]])

    dijkstra_tree = dijkstra(G, sources=1)

    # Generates dot file for original graph
    nx.drawing.nx_agraph.write_dot(G, 'original.dot')

    # Generates dot file for resulting tree
    nx.drawing.nx_agraph.write_dot(dijkstra_tree, 'dijkstra.dot')

if __name__ == '__main__':
    main()
