from grafos2023 import GrafoLista

# Crear un objeto GrafoLista
grafoEjemplo = GrafoLista()
print("Grafo: ",grafoEjemplo)

# Agregar algunos vértices

grafoEjemplo.adicionarVertice('A')
grafoEjemplo.adicionarVertice('B')
grafoEjemplo.adicionarVertice('C')

# Agregar algunos arcos

grafoEjemplo.adicionarArco('A', 'B')
grafoEjemplo.adicionarArco('B', 'C')

# Imprimimos el grafo antes de eliminar el arco

print("\nGrafo antes de eliminar el arco:\n")
print(grafoEjemplo)

# Eliminamos el arco ('A', 'B')

grafoEjemplo.eliminarArco('A', 'B')

# Imprimimos el grafo después de eliminar el arco

print("\nGrafo después de eliminar el arco:\n")
print(grafoEjemplo)