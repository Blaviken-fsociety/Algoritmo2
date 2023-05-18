from arboles2023 import ArbolBinarioBusqueda, Fraccion

arbol = ArbolBinarioBusqueda()
lista_fracciones = [Fraccion(1, 2), Fraccion(3, 4), Fraccion(1, 6), Fraccion(1, 3), Fraccion(3, 2), Fraccion(4, 5), Fraccion(7, 4)]
arbol.insertarNodosListaFraccionarios(lista_fracciones)
print(arbol)


