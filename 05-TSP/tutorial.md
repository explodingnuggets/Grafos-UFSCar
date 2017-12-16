# O Problema do Caixeiro Viajante

Para este problema, implementamos o algoritmo Twice Around em Python:

### Twice Around

  Ler grafo G = (V, E, p)
  H ← vazia

* Passo1. T ← MST(G) // Aplicando o algoritmo de Kruskal
	Para cada e ∈ T {
	T ← T + e (Duplique aresta e)
* Passo 2. Encontre um circuito Euleriano L em T // Aplicando Fleury
* Passo 3. Enquanto L != vazio:
	Escolha sequencialmente lk ∈ L
	Se lk ∉ H então
	H ← H U {lk}
	L ← L – {lk}

### Código

(código)

E então, iniciando o algoritmo sempre com vértices aleatórios rodamos ele 10 vezes para poder listar os melhores e piores 3 resultados obtidos.

(código da main)

## Resultados:

(imagem dos resultados)

Como visto, existe uma discrepância notável entre o melhor(529.0) e o pior resultado(622.0), e isso se deve ao fato do Twice Around ser um algoritmo guloso, o que faz com que ele só avalie as melhores opções locais e não globais, podendo haver bastante diferença dependendo de onde é iniciado o algoritmo. 
Um bom jeito de amenizar essas discrepâncias é escolher um bom ponto inicial, por exemplo.
