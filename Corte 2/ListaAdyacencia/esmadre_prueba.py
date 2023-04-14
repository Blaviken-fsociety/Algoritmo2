from grafos2023 import GrafoLista

# Crear un objeto GrafoLista
grafo = GrafoLista()
print("Grafo: ",grafo)

grafo.adicionarVertice(1)
grafo.adicionarVertice(2)
grafo.adicionarVertice(3)
grafo.adicionarVertice(4)
grafo.adicionarVertice(5)

# Agregar aristas
grafo.adicionarArco(1, 2)
grafo.adicionarArco(2, 1)
grafo.adicionarArco(2, 3)
grafo.adicionarArco(3, 4)
grafo.adicionarArco(4, 5)
print("Grafo: ",grafo)

# Verificar si existe un camino desde el vertice 1 hacia todos los demas vertices del grafo
print(grafo.esMadre(2))#True
print(grafo.esMadre(1))#True
print(grafo.esMadre(4))#False
print(grafo.esMadre(6))#None