from grafos2023_conpesos import GrafoLista

# Crear un nuevo grafo
grafo = GrafoLista()

grafo.agregarVertice("A")
grafo.agregarVertice("B")
grafo.agregarVertice("C")
grafo.agregarVertice("D")

grafo.agregarArco("A", "B", 2)
grafo.agregarArco("B", "C", 3)
grafo.agregarArco("C", "D", 1)

print(grafo.contarArcos())

