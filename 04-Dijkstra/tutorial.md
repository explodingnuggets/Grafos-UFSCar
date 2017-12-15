Encontrar caminhos mínimos utilizando grafos é um problema muito comum no nosso dia-a-dia. Os aplicativos que trabalham com mapas e rotas, na maior parte das vezes, tem que encontrar caminhos mínimos entre dois lugares. Para isso, é possível utilizar o algoritmo de Dijkstra, que nos permite buscar uma árvore de caminhos mínimos em um grafo, partindo de um ponto. Existe também a possibilidade de iniciarmos a busca de caminhos mínimos por mais de um ponto, para diversificar a geração de caminhos.

Iremos então, implementar o algoritmo de Dijkstra multi-origens. Para isso, inicialmente criamos uma função chamada `dijkstra`, que recebe um *grafo* do tipo `networkx.Graph`, assim com um valor *sources*, que determina a quantidade de origens para o algoritmo.

```python
# Função que implementa o algoritmo de Dijkstra.
def dijkstra(graph, sources):

	# Árvore resultante
	tree = nx.DiGraph()

	return tree
```

Em seguida, seguiremos a mesma lógica do algoritmo de Prim, alterando apenas a inicialização dos vértices origem. Portanto, cada vértice tem atributos *cor*, *lambda* e *pi*, elas significando respectivamente, se o vértice foi o visitado, a distância mínima total para aquele vértice encontrado e o pai daquele vértice. Temos então a inicialização dos mesmos:

```python
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
```

Logo depois, selecionamos todos os vértices e suas informações. Utilizando esses dados, criamos o loop principal, que executa enquanto existirem nós não visitados. Dentro desse loop, é necessário escolher qual será o próximo nó a ser visitado. Isso é determinado pelo menor valor de lambda, de um vértice não visitado.

```python
# Enquanto existir um vértice não visitado, continua executando o algortimo
nodes_info = graph.nodes(data=True)
while any(node[1]['color'] == 'white' for node in nodes_info):
    # Seleciona os nós brancos, e em seguida, seleciona o nó com menor lambda que ainda não foi visitado
    white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
    min_node = min(white_nodes, key=lambda x: x[1]['lambda']) 
```

Assim que selecionamos o vértice a ser analisado, iteramos sobre todos os seus vizinhos, checando se é necessário atualizar os valores de lambda e pi. Esse processo é semelhante ao algoritmo de Prim, a única diferença é que lambda nesse caso não é somente o valor da aresta, e sim a distância total do caminho. Portanto, temos:

```python
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
```

Só nos então, montar a árvore resultante da aplicação do algoritmo. Iteramos sobre cada grafo, adicionado-os com a informação de pi, como vértice pai e o peso da aresta entre o pai e o vértice, como o peso da aresta na árvore.

```python
# Itera sobre todos os vértices, adicionado-os a árvore resultante
for node in graph.nodes(data=True):
	if node[1]['pi'] != None:
		edge_weight = graph.get_edge_data(node[0], node[1]['pi'])
		ancestor = node[1]['pi']
		tree.add_weighted_edges_from([[ancestor, node[0], edge_weight]])
```

O algoritmo finalizado é:

```python
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
```

O resultado da aplicação desse algoritmo para o [conjunto de dados](pages/data/wg59_dist.txt), pode ser visto na imagem a seguir (primeira imagem tem source=2, e a segunda tem source=3):
