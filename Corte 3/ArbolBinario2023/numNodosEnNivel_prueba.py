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

# Visualización
print("Árbol:\n", raiz.verArbol())

# Ejemplo de uso del método numNodosEnNivel
nivel = 2
num_nodos = raiz.numNodosEnNivel(nivel)
print(f"El número de nodos en el nivel {nivel} es: {num_nodos}")
