from grafos_dijkstra2023 import GrafoLista
grafo = GrafoLista()

grafo.adicionarVertice("A")
grafo.adicionarVertice("B")
grafo.adicionarVertice("C")
grafo.adicionarVertice("D")
grafo.adicionarVertice("E")
grafo.adicionarVertice("F")

grafo.adicionarArco("A", "B")
grafo.adicionarArco("B", "C")
grafo.adicionarArco("C", "D")
grafo.adicionarArco("B", "D")
grafo.adicionarArco("D", "E")
grafo.adicionarArco("E", "F")

print(grafo)
print(grafo.hayCamino("A", "F")) # Devuelve True
print(grafo.hayCamino("B", "A")) # Devuelve False