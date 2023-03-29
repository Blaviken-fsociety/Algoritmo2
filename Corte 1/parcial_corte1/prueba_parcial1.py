from metodo_parcial1 import *
# Crear una lista
lista = ListaSimple()

# Agregar algunos elementos
lista.insertar_al_comienzo(10)
lista.insertar_al_comienzo(20)
lista.insertar_al_comienzo(30)
lista.insertar_al_comienzo(20)
lista.insertar_al_comienzo(40)
lista.insertar_al_comienzo(20)

# Contar el número de veces que aparece el valor 20 en la lista
numero_de_veces = 3
if lista.contar(80, numero_de_veces):
    print(f"El valor 20 aparece exactamente {numero_de_veces} veces en la lista.")
else:
    print(f"El valor 20 no aparece exactamente {numero_de_veces} veces en la lista.")





