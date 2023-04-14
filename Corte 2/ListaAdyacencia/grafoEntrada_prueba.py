from grafos2023 import GrafoLista

# Crear un objeto GrafoLista
grafo = GrafoLista()
print("Grafo: ",grafo)

# Agregamos algunos nodos
grafo.adicionarVertice("A")
grafo.adicionarVertice("B")
grafo.adicionarVertice("C")

# Agregamos algunos arcos
grafo.adicionarArco("A", "B")
grafo.adicionarArco("C", "B")
grafo.adicionarArco("B", "C")
grafo.adicionarArco("C", "A")

print("Grafo: ",grafo)

# Probamos la función gradoEntrada para el nodo "C"
grado_entrada = grafo.gradoEntrada("C")#1
print(grado_entrada)
# Debería imprimir 1, ya que hay un arco entrando al nodo "C"

# Probamos la función gradoEntrada para el nodo "B"
grado_entrada = grafo.gradoEntrada("B")#2
print(grado_entrada)
# Debería imprimir 2, ya que hay un arco entrando al nodo "B"