from grafos2023_conpesos import GrafoLista

# Crear un nuevo grafo
grafo = GrafoLista()

# Agregar algunos vertices
grafo.agregarVertice('A')
grafo.agregarVertice('B')
grafo.agregarVertice('C')
grafo.agregarVertice('D')

# Contar los vertices
num_vertices = grafo.contarVertices()
print(f"El grafo tiene {num_vertices} vertices")
