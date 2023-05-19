from arboles2023 import ArbolBinario

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

# Visualización del árbol original
print("Árbol:\n", raiz.verArbol())

# Eliminar nodos hoja
raiz.eliminarNodosHoja()

# Visualización del árbol después de eliminar los nodos hoja
print("Árbol después de eliminar los nodos hoja:\n", raiz.verArbol())