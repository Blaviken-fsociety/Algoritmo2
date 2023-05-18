from arboles2023 import ArbolBinario

# Creación del primer árbol
raiz1 = ArbolBinario("A")
nodo01 = ArbolBinario("B")
nodo02 = ArbolBinario("C")
nodo03 = ArbolBinario("D")
nodo04 = ArbolBinario("E")
nodo05 = ArbolBinario("F")

raiz1.hijo_izquierdo = nodo01
raiz1.hijo_derecho = nodo02
nodo02.hijo_izquierdo = nodo03
nodo02.hijo_derecho = nodo04
nodo03.hijo_derecho = nodo05

# Visualización del primer árbol
print("Primer árbol:\n", raiz1.verArbol())

# Creación del segundo árbol (similar al primero)
raiz2 = ArbolBinario("A")
nodo11 = ArbolBinario("B")
nodo12 = ArbolBinario("C")
nodo13 = ArbolBinario("D")
nodo14 = ArbolBinario("E")
nodo15 = ArbolBinario("F")

raiz2.hijo_izquierdo = nodo11
raiz2.hijo_derecho = nodo12
nodo12.hijo_izquierdo = nodo13
nodo12.hijo_derecho = nodo14
nodo13.hijo_derecho = nodo15

# Visualización del segundo árbol
print("Segundo árbol:\n", raiz2.verArbol())

# Verificar si los árboles son iguales
if raiz1.sonIguales(raiz2):
    print("Los árboles son iguales.")
else:
    print("Los árboles son diferentes.")
