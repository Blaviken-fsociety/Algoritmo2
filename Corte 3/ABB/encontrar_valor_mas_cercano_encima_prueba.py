from arboles2023 import ArbolBinarioBusqueda

# Creación de instancia
arbol01 = ArbolBinarioBusqueda()
print("Arbol:", arbol01)
print("Arbol Vacio:", arbol01.estaVacio())

# Adición de valores
arbol01.insertar(5)
arbol01.insertar(3)
arbol01.insertar(7)
arbol01.insertar(1)
arbol01.insertar(4)
arbol01.insertar(6)
arbol01.insertar(8)

print("Arbol:", arbol01)
print("Arbol Vacio:", arbol01.estaVacio())
print("En Orden:", arbol01.enOrden())

# Utilización del método encontrar_valor_mas_cercano_encima
dato_indicado = 2
valor_mas_cercano = arbol01.encontrar_valor_mas_cercano_encima(dato_indicado)
print(f"El valor más cercano por encima de {dato_indicado} es: {valor_mas_cercano}")