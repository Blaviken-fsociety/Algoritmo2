from grafos2023 import GrafoLista

grafo = GrafoLista()
print("Grafo: ",grafo)

grafo.adicionarVertice('A')
grafo.adicionarVertice('B')
grafo.adicionarVertice('C')
grafo.adicionarVertice('D')
print("\nGrafo: ",grafo)

grafo.adicionarArco('A', 'B')
grafo.adicionarArco('A', 'C')
grafo.adicionarArco('A', 'D')
grafo.adicionarArco('B', 'A')
grafo.adicionarArco('B', 'C')
grafo.adicionarArco('B', 'D')
grafo.adicionarArco('C', 'A')
grafo.adicionarArco('C', 'B')
grafo.adicionarArco('C', 'D')
grafo.adicionarArco('D', 'A')
grafo.adicionarArco('D', 'B')
grafo.adicionarArco('D', 'C')
print("\nGrafo: ",grafo)

for vertice in grafo.verVertices():
    print(f"\nLos nodos adyacentes a {vertice} son: {grafo.nodosConAdyacente(vertice)}\n")
