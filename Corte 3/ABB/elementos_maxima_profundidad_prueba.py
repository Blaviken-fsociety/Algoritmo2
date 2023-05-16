from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol01 = ArbolBinarioBusqueda()

# Adición de valores
arbol01.insertar(55)
arbol01.insertar(30)
arbol01.insertar(4)
arbol01.insertar(41)
arbol01.insertar(75)
arbol01.insertar(85)

# Impresión del árbol y verificación si está vacío
print("Arbol:", arbol01)
print("Arbol Vacio:", arbol01.estaVacio())

# Recorrido en orden
print("En Orden:", arbol01.enOrden())

# Obtener elementos en la máxima profundidad
elementos_maxima_profundidad = arbol01.elementos_maxima_profundidad()
print("Elementos en la máxima profundidad:", elementos_maxima_profundidad)
