from grafos2023_conpesos import GrafoLista

# Creamos un grafo dirigido
g = GrafoLista()
g.agregarVertice("A")
g.agregarVertice("B")
g.agregarVertice("C")
g.agregarVertice("D")
g.agregarArco("A", "B", 1)
g.agregarArco("A", "C", 2)
g.agregarArco("B", "D", 3)
g.agregarArco("C", "D", 4)

# Contamos el número de arcos en el grafo
num_arcos = g.contarArcos()

# Imprimimos el resultado
print(f"El número de arcos en el grafo es: {num_arcos}")


