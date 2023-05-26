from arboles2023 import ArbolBinario

# Creamos los nodos del árbol
nodo1 = ArbolBinario(1)
nodo2 = ArbolBinario(2)
nodo3 = ArbolBinario(3)
nodo4 = ArbolBinario(4)
nodo5 = ArbolBinario(5)
nodo6 = ArbolBinario(6)

# Establecemos las relaciones entre los nodos
nodo1.hijo_izquierdo = nodo2
nodo1.hijo_derecho = nodo3
nodo2.hijo_izquierdo = nodo4
nodo2.hijo_derecho = nodo5
nodo3.hijo_derecho = nodo6

# Imprimimos el árbol
print(nodo1.verArbol())

# Realizamos el recorrido por niveles
recorrido = nodo1.recorridoPorNiveles()

# Imprimimos los valores visitados en el recorrido por niveles
for nodo in recorrido:
    print(nodo)

