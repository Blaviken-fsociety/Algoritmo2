from arboles2023 import ArbolBinario

# Creación de Nodos
raiz = ArbolBinario("A")
nodo01 = ArbolBinario("B")
nodo02 = ArbolBinario("C")
nodo03 = ArbolBinario("D")
nodo04 = ArbolBinario("E")
nodo05 = ArbolBinario("F")

# Conexión de nodos
raiz.hijo_izquierdo = nodo01
raiz.hijo_derecho = nodo02
nodo02.hijo_izquierdo = nodo03
nodo02.hijo_derecho = nodo04
nodo03.hijo_derecho = nodo05

# Visualización
print("Arbol:\n", raiz.verArbol())

# Calcular altura del árbol
altura_arbol = raiz.altura()
print("Altura del árbol:", altura_arbol)