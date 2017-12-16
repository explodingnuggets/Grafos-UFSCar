#!/bin/python
import matplotlib.pyplot as plt
import networkx as nx

import random

# Função que implementa o algoritmo de Dijkstra.
def dijkstra(graph, sources):
	# Inicializa a cor dos vértices (white: não visitado, black: visitado)
	nx.set_node_attributes(graph, 'white', 'color')
	# Inicializa a lambda (distância mínima total dos vértices) como infinito
	nx.set_node_attributes(graph, float('inf'), 'lambda')
	# Seleciona 'n' elementos para iniciar o algoritmo (minimum distance = 0)
	nodes = random.sample(graph.nodes, sources)
	for node in nodes:
		nx.set_node_attributes(graph, {node: 0}, 'lambda')
	# Inicializa os o pai dos vértices como None
	nx.set_node_attributes(graph, None, 'pi')

	# Enquanto existir um vértice não visitado, continua executando o algortimo
	nodes_info = graph.nodes(data=True)
	while any(node[1]['color'] == 'white' for node in nodes_info):
		# Seleciona os nós brancos, e em seguida, seleciona o nó com menor lambda que ainda não foi visitado
		white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
		min_node = min(white_nodes, key=lambda x: x[1]['lambda']) 

		# Itera sobre todos os vizinhos nó vértice selecionado.
		for node in graph.neighbors(min_node[0]):
			node_info = (node, nodes_info[node])
			if node_info[1]['color'] == 'white':
				new_dist = graph.get_edge_data(min_node[0], node_info[0])['weight'] + min_node[1]['lambda']
				# Checa se é necessário atualizar os valores lambda e pi
				if new_dist < node_info[1]['lambda']:
					nx.set_node_attributes(graph, {node_info[0]: new_dist}, 'lambda')
					nx.set_node_attributes(graph, {node_info[0]: min_node[0]}, 'pi')
		nx.set_node_attributes(graph, {min_node[0]: 'black'}, 'color')
		nodes_info = graph.nodes(data=True)

	# Árvore resultante
	tree = nx.DiGraph()

	# Itera sobre todos os vértices, adicionado-os a árvore resultante
	for node in graph.nodes(data=True):
		if node[1]['pi'] != None:
			edge_weight = graph.get_edge_data(node[0], node[1]['pi'])
			ancestor = node[1]['pi']
			tree.add_weighted_edges_from([[ancestor, node[0], edge_weight]])

	return tree

def main():
    G = nx.Graph()
    G.add_weighted_edges_from([['a', 'b', 2],
                               ['a', 'c', 8],
                               ['a', 'f', 14],
                               ['b', 'c', 6],
                               ['b', 'e', 5],
                               ['c', 'd', 3],
                               ['c', 'e', 5],
                               ['d', 'f', 6],
                               ['e', 'f', 8]])

    dijkstra_tree = dijkstra(G, sources=1)

    # Generates dot file for original graph
    nx.drawing.nx_agraph.write_dot(G, 'original.dot')

    # Generates dot file for resulting tree
    nx.drawing.nx_agraph.write_dot(dijkstra_tree, 'dijkstra.dot')

if __name__ == '__main__':
    main()
