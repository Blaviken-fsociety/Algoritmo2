from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol01 = ArbolBinarioBusqueda()
print("Arbol: ", arbol01)
print("Arbol Vacio: ", arbol01.estaVacio())

# Adición de valores
arbol01.insertar(55)
arbol01.insertar(30)
arbol01.insertar(4)
arbol01.insertar(41)
arbol01.insertar(75)
arbol01.insertar(85)

print("Arbol: ", arbol01)
print("Arbol Vacio: ", arbol01.estaVacio())
print("En Orden:", arbol01.enOrden())

# Ejemplo de uso del método encontrarPadre()
elemento = 41
padre = arbol01.encontrarPadre(elemento)
if padre:
    print(f"El padre del elemento {elemento} es: {padre.valor_nodo}")
else:
    print(f"No se encontró el elemento {elemento} en el árbol.")


