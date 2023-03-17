from tallerclase2 import *
lista = ListaSimple()

# Agregar elementos a la lista
lista.agregar_elemento(10)
lista.agregar_elemento(20)
lista.agregar_elemento(30)
lista.agregar_elemento(40)

# Imprimir la lista y su longitud
actual = lista.cabeza
while actual:
    print(actual.dato, end=' ')
    actual = actual.siguiente
print("Longitud:", lista.longitud)

# Eliminar el último elemento de la lista
lista.eliminar_ultimo()

# Imprimir la lista y su longitud después de eliminar el último elemento
actual = lista.cabeza
while actual:
    print(actual.dato, end=' ')
    actual = actual.siguiente
print("Longitud:", lista.longitud)

# Contar el número de apariciones de un dato en la lista
apariciones = lista.apariciones(20)
print("Apariciones de 20:", apariciones)

# Obtener el elemento en una posición indicada de la lista
elemento = lista.elemento_en_posicion(2)
print("Elemento en posición 2:", elemento)

# Obtener el último elemento de la lista
ultimo = lista.ultimo_elemento()
print("Último elemento:", ultimo)

# Eliminar un elemento en una posición indicada de la lista
lista.eliminar_en_posicion(1)

# Imprimir la lista y su longitud después de eliminar un elemento
actual = lista.cabeza
while actual:
    print(actual.dato, end=' ')
    actual = actual.siguiente
print("Longitud:", lista.longitud)
