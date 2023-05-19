from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol01 = ArbolBinarioBusqueda()

# Adición de valores
arbol01.insertar(5)
arbol01.insertar(4)
arbol01.insertar(1)
arbol01.insertar(3)
arbol01.insertar(7)
arbol01.insertar(6)
arbol01.insertar(9)
arbol01.insertar(8)
arbol01.insertar(10)

print("Árbol antes de eliminar los nodos hoja con padre de un único hijo:")
print(arbol01)

# Eliminar nodos hoja con padre de un único hijo
arbol01.eliminar_nodos_hoja_padre_un_hijo()

print("Árbol después de eliminar los nodos hoja con padre de un único hijo:")
print(arbol01)

print("En Orden:", arbol01.enOrden())