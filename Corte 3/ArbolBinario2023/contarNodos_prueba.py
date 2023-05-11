from arboles2023 import ArbolBinario

# Creación de nodos
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

# Visualización del árbol
print("Árbol:\n", raiz.verArbol())

# Contar el número de nodos
num_nodos = raiz.contarNodos()
print("Número de nodos:", num_nodos)