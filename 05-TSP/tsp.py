import numpy as np
import networkx as nx
import random

def twicearound(graph, source=0):
	# Make MST from original Graph
	mst = nx.minimum_spanning_tree(graph)

	# Only MultiGraphs can have parallel edges
	mst_multi = nx.MultiGraph(mst)
    
	# Double the edges in the MST
	multi_copy = mst_multi.copy()
	for u,v in multi_copy.edges():
		mst_multi.add_edge(u,v)

	# Generate Eulerian Circuit
	euler = list(nx.eulerian_circuit(mst_multi, source))
	cycle = nx.Graph()
	aux = []
	for u,v in euleraux: 
		aux.append(u)
		aux.append(v)
	h = []
	for i in aux: 
		# Remove repeated nodes
		if (i not in h):
			h.append(i)
	h.append(source)
	f_weight = 0
	for i in range (30):
		# Generate resulting Graph
		cycle.add_edge(h[i],h[i+1])
		cycle[h[i]][h[i+1]]['weight'] = graph[h[i]][h[i+1]]['weight']
		f_weight += graph[h[i]][h[i+1]]['weight']
    
	return (cycle, f_weight)

def main():
	matrix = np.loadtxt('ha30_dist.txt')
	graph = nx.from_numpy_matrix(matrix)
	sources = random.sample(graph.nodes, 10)
	results = []
	for source in sources:
		results.append(twicearound(graph, source))
	results_sorted = sorted(results, key=lambda x: x[1])

	print("Melhores 3:")
	for result in results_sorted[:3]:
		print(result[1])

	print("Piores 3:")
	for result in results_sorted[-3:]:
		print(result[1])

if __name__ == '__main__':
	main()
