from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol = ArbolBinarioBusqueda()

# Adición de valores
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(17)
arbol.insertar(2)
arbol.insertar(4)

# Verificar si es un árbol AVL
print("Arbol:")
print(arbol)
es_avl = arbol.esAVL()
print("Es AVL:", es_avl)
