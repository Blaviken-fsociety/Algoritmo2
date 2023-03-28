from grafos2023 import GrafoLista

# Creamos un grafo de ejemplo

grafo = GrafoLista()
print("Grafo: ",grafo)

# Añadimos algunos vértices

grafo.adicionarVertice('A')
grafo.adicionarVertice('B')
grafo.adicionarVertice('C')
grafo.adicionarVertice('D')

# Añadimos algunos arcos

grafo.adicionarArco('A', 'B')
grafo.adicionarArco('B', 'C')
grafo.adicionarArco('C', 'D')
grafo.adicionarArco('D', 'A')

# Imprimimos el grafo antes de eliminar un vértice

print("\nGrafo: ",grafo)

# Eliminamos el vértice 'C'

grafo.eliminarVertice('C')

# Imprimimos el grafo después de eliminar el vértice

print("\nGrafo después de eliminar 'C':\n")
print(grafo)
