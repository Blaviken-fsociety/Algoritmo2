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

# Implementación del método agregarElemento
def agregarElemento(self, padre, nuevo_elemento):
    # Buscar el nodo padre en el árbol
    nodo_padre = self.buscarNodo(self, padre)

    if nodo_padre is None:
        print("El nodo padre no existe en el árbol.")
        return

    # Verificar si el padre ya tiene dos hijos
    if nodo_padre.hijo_izquierdo is not None and nodo_padre.hijo_derecho is not None:
        print("El padre ya tiene dos hijos. No se puede agregar el nuevo elemento.")
        return

    # Crear el nuevo nodo con el nuevo elemento
    nuevo_nodo = ArbolBinario(nuevo_elemento)

    # Asignar el nuevo nodo como hijo izquierdo o derecho del padre
    if nodo_padre.hijo_izquierdo is None:
        nodo_padre.hijo_izquierdo = nuevo_nodo
    else:
        nodo_padre.hijo_derecho = nuevo_nodo

    print("Nuevo elemento agregado exitosamente.")

# Agregar un nuevo elemento (G) asociado al padre (D)
agregarElemento(nodo03, "G")

# Intentar agregar un nuevo elemento (H) asociado al padre (D), que ya tiene dos hijos
agregarElemento(nodo03, "H")

# Visualización del árbol después de agregar los elementos
print(raiz.verArbol())
