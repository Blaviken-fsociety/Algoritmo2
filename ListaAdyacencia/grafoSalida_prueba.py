from grafos2023 import GrafoLista

# Crear un objeto GrafoLista
grafo = GrafoLista()
print("Grafo: ",grafo)

# Agregar algunos vértices
grafo.adicionarVertice('A')
grafo.adicionarVertice('B')
grafo.adicionarVertice('C')
grafo.adicionarVertice('D')

# Agregar algunos arcos
grafo.adicionarArco('A', 'B')
grafo.adicionarArco('B', 'C')
grafo.adicionarArco('B', 'D')
grafo.adicionarArco('C', 'D')

print("Grafo: ",grafo)

# Obtener el grado de salida de 'B'

grado_b = grafo.gradoSalida('B')

print(grado_b) # Debería imprimir 2
