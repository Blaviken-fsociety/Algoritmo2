from arboles2023 import ArbolBinarioBusqueda

elementos = input("Ingresa los elementos separados por comas: ")

# Convertir la entrada en una lista de elementos
lista_elementos = elementos.split(",")

# Crear un objeto de la clase ArbolBinarioBusqueda
abb = ArbolBinarioBusqueda()

# Insertar cada elemento en el árbol
for elemento in lista_elementos:
    abb.insertar(int(elemento))

# Imprimir el árbol resultante
print(abb)