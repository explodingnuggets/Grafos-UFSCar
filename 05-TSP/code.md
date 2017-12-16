```python
def twicearound(graph, source=0):
	mst = nx.minimum_spanning_tree(graph) # gero a mst a partir do grafo original
	mst_multi = nx.MultiGraph(mst) # como somente multigrafos aceitam arestas paralelas
    
	multi_copy = mst_multi.copy()
	for u,v in multi_copy.edges():
		mst_multi.add_edge(u,v)     #duplico arestas da mst

	euleraux = list(nx.eulerian_circuit(mst_multi, source)) # gero um circuito euleriano
	cycle = nx.Graph()
	aux = []
	for u,v in euleraux: 
		aux.append(u)
		aux.append(v)
	h = []
	for i in aux: 
		if (i not in h):    # elimino repeticoes
			h.append(i)
	h.append(source)
	f_weight = 0
	for i in range (30):
		cycle.add_edge(h[i],h[i+1]) # gero grafo resultante
		cycle[h[i]][h[i+1]]['weight'] = graph[h[i]][h[i+1]]['weight'] # copiando tambem o peso
		f_weight += graph[h[i]][h[i+1]]['weight']
    
	return (cycle, f_weight)
```

Resultado:
