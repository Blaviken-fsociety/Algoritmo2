from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol = ArbolBinarioBusqueda()
print("Arbol: ", arbol)
print("Arbol Vacio: ", arbol.estaVacio())

# Adición de valores
arbol.insertar(55)
arbol.insertar(30)
arbol.insertar(4)
arbol.insertar(41)
arbol.insertar(75)
arbol.insertar(85)
print("Arbol: ", arbol)
print("Arbol Vacio: ", arbol.estaVacio())
print("En Orden:", arbol.enOrden())

# Obtener el menor nodo
menor = arbol.menorNodo()
if menor is not None:
    print("Menor nodo:", menor.valor_nodo)
else:
    print("El árbol está vacío.")

# Obtener el mayor nodo
mayor = arbol.mayorNodo()
if mayor is not None:
    print("Mayor nodo:", mayor.valor_nodo)
else:
    print("El árbol está vacío.")
