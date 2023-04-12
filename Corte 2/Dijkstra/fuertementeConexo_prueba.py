from grafos_dijkstra2023 import GrafoLista
grafo = GrafoLista()

grafo.adicionarVertice('A')
grafo.adicionarVertice('B')
grafo.adicionarVertice('C')
grafo.adicionarVertice('D')
grafo.adicionarVertice('E')

grafo.adicionarArco('A', 'B')
grafo.adicionarArco('B', 'C')
grafo.adicionarArco('C', 'D')
grafo.adicionarArco('D', 'E')
grafo.adicionarArco('E', 'A')

print(grafo)
print(grafo.esFuertementeConexo())