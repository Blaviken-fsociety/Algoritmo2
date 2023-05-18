from arboles2023 import ArbolBinarioBusqueda

# Crear una lista de elementos desordenados
elementos = [40, 20, 60, 10, 30, 50, 70, 45, 55, 54, 75]

# Crear un árbol parcialmente ordenado con los elementos
arbol = ArbolBinarioBusqueda.crearArbolParcialmenteOrdenado(elementos)

# Imprimir el árbol
print("Árbol:")
print(arbol.verArbol())
