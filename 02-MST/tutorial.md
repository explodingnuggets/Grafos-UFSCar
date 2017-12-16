O algoritmo de Prim é um dos mais utilizados para encontrar árvores mínimas geradoras, ou MSTs, dado um determinado grafo. Nesse tutorial, iremos criar passo à passo uma função que nos retorna uma MST, utilizando Prim.

Inicialmente, criamos uma função chamada prim, que recebe um objeto do tipo `networkx.Graph`. Esse é o grafo que será utilizado para encontrar a árvore mínima geradora. Também iremos adicionar um novo objeto na função, chamado de `mst`, que será retornado no final da execução. Essa será a árvore resultante.

```python
# Função que implementa o algoritmo de Prim. Recebe um nx.Graph e retorna um nx.DiGraph
def prim(graph):

    # Digrafo resultante
    mst = nx.DiGraph()

    return mst
```

O passo seguinte é adicionar as propriedades de *cor (branco se não visitado, preto se foi), lambda (distância mínima encontrada) e pi (pai do vértice)*. Para isso, podemos utilizar os atributos das vértices do próprio grafo recebido pela função. Inicializamos então todos os vértices com a cor branca, todos eles sem pai e todos menos o vértice inicial com a lambda infinito. O lambda do vértice inicial deve receber 0, para que o algoritmo tenha um vértice para começar.

```python
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
```

Em seguida, iremos criar o loop principal, que será executado enquanto existirem vértices com a cor branca (não visitados). Ele deverá selecionar o vértice com menor lambda. Para isso, fazemos o seguinte:

```python
# Enquanto existir um vértice não visitado, continua visitando
nodes_info = graph.nodes(data=True) # nos dá todos os vértices do grafo, junto com seus atributos
while any(node[1]['color'] == 'white' for node in nodes_info):
    # Seleciona apenas os vértices brancos
    white_nodes = [node for node in nodes_info if node[1]['color'] == 'white']
    # Seleciona o vértice com menor lambda
    min_node = min(white_nodes, key=lambda x: x[1]['lambda'])
```

Com o loop principal iniciado, só nós resta adicionar a visita dos vértices vizinhos ao vértice atual. Para isso, utilizamos outros loop, que itera sobre todos os vértices vizinhos, checando se a nova distância é menor que o lambda armazenado. Se for, os valores de lambda e pi são atualizados. Ao final desse loop, só nos resta atualizar a cor do vértice que visitamos nessa iteração e atualizar a lista de nós.

```python
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
```

Assim que o algoritmo é finalizado, e todos os vértices recebem um pai, assim como um lambda representando a distância mínima, o único passo restante é montar a árvore com os dados. Devemos então, iterar sobre todos os nós, adicionando arestas utilizando o valor do nó, o valor de pi como pai e o valor de lambda como peso.

```python
# Adiciona os nós à mst
for node in graph.nodes(data=True):
    if node[1]['pi'] is not None:
        edge_weight = node[1]['lambda']
        parent = node[1]['pi']
        mst.add_weighted_edges_from([[parent, node[0], edge_weight]])
```

O código final para a função `prim` fica:

```python
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
```

O resultado da aplicação desse algoritmo, para esse [conjunto de dados](pages/data/ha30_dist.txt), pode ser visto na imagem a seguir:
