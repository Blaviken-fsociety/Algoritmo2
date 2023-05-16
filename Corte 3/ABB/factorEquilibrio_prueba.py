from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol01 = ArbolBinarioBusqueda()

# Adición de valores
arbol01.insertar(40)
arbol01.insertar(20)
arbol01.insertar(60)
arbol01.insertar(10)
arbol01.insertar(30)
arbol01.insertar(50)
arbol01.insertar(70)
arbol01.insertar(45)
arbol01.insertar(55)
arbol01.insertar(75)

# Imprimir el árbol
print("Arbol:", arbol01)
print("Arbol Vacio:", arbol01.estaVacio())
print("En Orden:", arbol01.enOrden())

# Calcular el factor de equilibrio
print("Factor de Equilibrio:", arbol01.factorEquilibrio())