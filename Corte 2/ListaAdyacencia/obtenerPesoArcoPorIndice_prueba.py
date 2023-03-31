from grafos2023_conpesos import GrafoLista

# Creamos un grafo dirigido
g = GrafoLista()

g.agregarVertice("A")
g.agregarVertice("B")
g.agregarVertice("C")
g.agregarVertice("D")

g.agregarArco("A", "B", 2)
g.agregarArco("A", "C", 1)
g.agregarArco("B", "D", 3)
g.agregarArco("C", "D", 1)

# Obtenemos el peso del arco que va de "A" a "B" (índice 0)
peso_arco = g.obtenerPesoArco("A", "B")

# Imprimimos el resultado
print(f"El peso del arco de A a B es: {peso_arco}")