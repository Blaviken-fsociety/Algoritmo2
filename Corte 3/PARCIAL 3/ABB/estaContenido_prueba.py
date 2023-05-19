from arboles2023 import ArbolBinarioBusqueda

arbol01 = ArbolBinarioBusqueda()

arbol01.insertar(5)
arbol01.insertar(4)
arbol01.insertar(1)
arbol01.insertar(3)
arbol01.insertar(7)
arbol01.insertar(6)
arbol01.insertar(9)
arbol01.insertar(8)
arbol01.insertar(10)

arbol02 = ArbolBinarioBusqueda()

arbol02.insertar(7)
arbol02.insertar(6)
arbol02.insertar(9)

if arbol01.estaContenido(arbol02):
    print("arbol02 está contenido en arbol01")
else:
    print("arbol02 no está contenido en arbol01")

arbol03 = ArbolBinarioBusqueda()

arbol03.insertar(3)
arbol03.insertar(2)
arbol03.insertar(4)

if arbol01.estaContenido(arbol03):
    print("arbol03 está contenido en arbol01")
else:
    print("arbol03 no está contenido en arbol01")