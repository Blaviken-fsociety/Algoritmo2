from grafos2023 import GrafoLista

#Creacion Grafo
grafo02 = GrafoLista()
print("Grafo: ",grafo02)

#Adicion de vertices

grafo02.adicionarVertice("D")
grafo02.adicionarVertice("B")
grafo02.adicionarVertice("C")
grafo02.adicionarVertice("H")
grafo02.adicionarVertice("T")
grafo02.adicionarVertice("A")

#Adicion de arcos

grafo02.adicionarArco("D","B")
grafo02.adicionarArco("D","C")
grafo02.adicionarArco("C","R")
grafo02.adicionarArco("R","H")
grafo02.adicionarArco("H","T")
grafo02.adicionarArco("H","A")
grafo02.adicionarArco("B","H")
grafo02.adicionarArco("H","D")

print("Grafo: ",grafo02)
print("Recorrido: ",grafo02.recorrerProfundidad("D"))

