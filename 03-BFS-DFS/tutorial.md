Para o terceiro trabalho, implementamos os algoritmos de DFS e BFS a seguir na linguagem Python:

### DFS
```python
DFS(G, s){
    // Inicialização dos vértices
    para cada u ∈ V{
	u.cor = BRANCO
	predecessor(u) = nil
    }

    tempo = 0 // variável global para armazenar o tempo

    DFS_visit(G, s)
}

# Função recursiva que é chamada sempre que um vértice é descoberto
DFS_visit(G, u){
     tempo++
     u.tempo_descoberto = tempo
     u.cor = CINZA
     // Checa todos os vizinhos de u
     para cada v ∈ N(u){
	if v.color == BRANCO{ // Se existe um vizinho ainda não visitado, visite
	    predecessor(v) = u
	    DFS_visit(G, v) // chamada recursiva
	}
     }
     u.cor = PRETO
     tempo++
     u.finalizado = tempo
}
```

### BFS

```python
BFS(G, s){
     // Inicialização dos vértices
     para todo v ∈ V − {s} {
	  v.cor = BRANCO
	  distancia_minima(v) = infinito
	  predecessor(v) = nil
     }
     // Inicialização do vértice inicial
     s.cor = CINZA
     distancia_minima(s)=0
     predecessor(v) = nil
     // Inicialização da Fila
     Q = []
     insere(Q, s)
     enquanto Q != vazia{
	  u = pop(Q)
	  // para todo vizinho de u
	  for each v ∈ N (u){ 
		// se ainda não passei por aqui, processo vértice v
	        if v.color == BRANCO{
		    // v é descendente de u então distancia + 1
		    distancia_minima(v) = distancia_minima(u) + 1
		    predecessor(v) = u
		    v.cor = CINZA
		    insere(Q, v)  // adiciona v no final da fila
		}
	   }
	   u.cor = PRETO // Após explorar todos vizinhos de u, finalizo u
     }
}
```

### Código 
(colocar bfs() e dfs() aqui)

E então os aplicamos nos grafos Dolphin's Social Network e Zachary's Karate Club:

### Resultados
#### Karate:

#### Dolphins:

