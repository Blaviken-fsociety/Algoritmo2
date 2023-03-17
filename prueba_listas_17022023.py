from listas_2022 import *
"""#Prueba Nodos
nodo_01 = NodoSimple("Python")
print(nodo_01)
nodo_02 = NodoSimple("Java")
print(nodo_02)
print(nodo_01 == nodo_02)"""
#Prueba Lista
lista_prueba = ListaSimple()
print("Listas: ",lista_prueba)
lista_prueba.adicionarAlInicio(10)
print("Listas: ",lista_prueba)
lista_prueba.adicionarAlInicio("Casa")
lista_prueba.adicionarAlInicio("557")
print("Listas: ",lista_prueba)
print("Busqueda 01: ",lista_prueba.buscar(50))
print("Busqueda 02: ",lista_prueba.buscar("Casa"))
print("Eliminar Al Inicio 01: ",lista_prueba.eliminarAlInicio())
print("Listas: ",lista_prueba)  