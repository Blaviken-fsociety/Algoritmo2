from grafos_dijkstra2023 import GrafoLista
grafo = GrafoLista()

grafo.adicionarVertice('A')
grafo.adicionarVertice('B')
grafo.adicionarVertice('C')
grafo.adicionarVertice('D')

grafo.adicionarArco('A', 'B')
grafo.adicionarArco("A", "B")
grafo.adicionarArco("A", "C")
grafo.adicionarArco("A", "D")
grafo.adicionarArco("B", "A")
grafo.adicionarArco("B", "C")
grafo.adicionarArco("B", "D")
grafo.adicionarArco("C", "A")
grafo.adicionarArco("C", "B")
grafo.adicionarArco("C", "D")
grafo.adicionarArco("D", "A")
grafo.adicionarArco("D", "B")
grafo.adicionarArco("D", "C")

print(grafo)
print(grafo.esCompleto())