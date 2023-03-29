from grafos2023_conpesos import GrafoLista

# Creamos un grafo vacío
grafo = GrafoLista()

# Agregamos algunos nodos
grafo.agregarVertice('A')
grafo.agregarVertice('B')
grafo.agregarVertice('C')
grafo.agregarVertice('D')

# Agregamos algunos arcos con pesos
grafo.agregarArco('A', 'B', peso=2)
grafo.agregarArco('A', 'C', peso=3)
grafo.agregarArco('B', 'C', peso=1)
grafo.agregarArco('C', 'D', peso=5)

# Imprimimos el grafo
print(grafo)


