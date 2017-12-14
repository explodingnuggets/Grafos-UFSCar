import matplotlib.pyplot as plt
import networkx as nx

# Função que implementa o algoritmo de Prim. Recebe um nx.Graph e retorna um nx.DiGraph
def prim(graph):
    # Inicializa as cores dos vértices como branco
    nx.set_node_attributes(graph, 'white', 'color')

    # Inicializa o pi(pai) dos vértices como None
    nx.set_node_attributes(graph, None, 'pi')

    # Inicializa o lambda(distância mínima) dos vértices como infinito
    # O vértice inicial recebe 0
    nx.set_node_attributes(graph, float('inf'), 'lambda')
    for node in graph.nodes:
        nx.set_node_attributes(graph, {node: 0}, 'lambda')
        break   # Executa o loop para apenas um nó

    # Enquanto existir um vértice não visitado, continua visitando
    nodes_info = graph.nodes(data=True) # nos dá todos os vértices do grafo, junto com seus atributos
    while any(node[1]['color'] == 'white' for node in nodes_info):
        # Seleciona apenas os vértices brancos
        white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
        # Seleciona o vértice com menor lambda
        min_node = min(white_nodes, key=lambda x: x[1]['lambda'])

        # Itera sobre todos os vizinhos do vértice, e atualiza os atributos se necessário
        for node in graph.neighbors(min_node[0]):
            node_info = (node, dict(nodes_info)[node])
            if node_info[1]['color'] == 'white':
                new_dist = graph.get_edge_data(min_node[0], node_info[0])['weight']
                # Checa se é necessário atualizar os atributos
                if new_dist < node_info[1]['lambda']:
                    nx.set_node_attributes(graph, {node_info[0]: new_dist}, 'lambda')
                    nx.set_node_attributes(graph, {node_info[0]: min_node[0]}, 'pi')

        nx.set_node_attributes(graph, {min_node[0]: 'black'}, 'color')
        nodes_info = graph.nodes(data=True)

    # Digrafo resultante
    mst = nx.DiGraph()

    # Adiciona os nós à mst
    for node in graph.nodes(data=True):
        if node[1]['pi'] is not None:
            edge_weight = node[1]['lambda']
            parent = node[1]['pi']
            mst.add_weighted_edges_from([[parent, node[0], edge_weight]])

    return mst

def main():
    # Creates test case graph and adds edges
    G = nx.Graph()
    G.add_weighted_edges_from([['a', 'b', 3.0],
                              ['b', 'c', 5.0],
                              ['c', 'd', 1.0],
                              ['d', 'e', 2.0],
                              ['a', 'd', 1.5],
                              ['e', 'f', 3.0],
                              ['e', 'c', 2.0]])
    
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
