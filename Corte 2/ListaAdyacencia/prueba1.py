from grafos2023 import GrafoLista

#Creacion Grafo
grafo01 = GrafoLista()
print("Grafo: ",grafo01)

#Adicion de vertices

grafo01.adicionarVertice("D")
grafo01.adicionarVertice("F")
grafo01.adicionarVertice("K")
grafo01.adicionarVertice("L")
grafo01.adicionarVertice("R")

print("Grafo: ",grafo01)
print("Adyacentes: ",grafo01.buscarVertice("X"))

#Adicion de arcos

grafo01.adicionarArco("R","D")
grafo01.adicionarArco("D","F")
grafo01.adicionarArco("D","K")

print("Grafo: ",grafo01)