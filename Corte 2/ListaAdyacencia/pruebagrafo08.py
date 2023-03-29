from grafos_dijkstra2023 import GrafoLista
from grafos_dijkstra2023 import Dijkstra
grafo01 = GrafoLista()
#Adicionar vértices
grafo01.adicionarVertice("BOS")
grafo01.adicionarVertice("PVD")
grafo01.adicionarVertice("JFK")
grafo01.adicionarVertice("BWI")
grafo01.adicionarVertice("ORD")
grafo01.adicionarVertice("DFW")
grafo01.adicionarVertice("MIA")
grafo01.adicionarVertice("SFO")
grafo01.adicionarVertice("LAX")
# #Adicionar arcos
grafo01.adicionarArco("BOS", "SFO",2704)
grafo01.adicionarArco("SFO", "BOS",2704)
grafo01.adicionarArco("BOS", "ORD",867)
grafo01.adicionarArco("ORD", "BOS",867)
grafo01.adicionarArco("BOS", "JFK",187)
grafo01.adicionarArco("JFK", "BOS",187)
grafo01.adicionarArco("BOS", "MIA",1258)
grafo01.adicionarArco("MIA", "BOS",1258)
grafo01.adicionarArco("PVD", "JFK",144)
grafo01.adicionarArco("JFK", "PVD",144)
grafo01.adicionarArco("PVD", "ORD",849)
grafo01.adicionarArco("ORD", "PVD",849)
grafo01.adicionarArco("JFK", "ORD",740)
grafo01.adicionarArco("ORD", "JFK",740)
grafo01.adicionarArco("JFK", "BWI",184)
grafo01.adicionarArco("BWI", "JFK",184)
grafo01.adicionarArco("JFK", "MIA",1090)
grafo01.adicionarArco("MIA", "JFK",1090)
grafo01.adicionarArco("JFK", "DFW",1391)
grafo01.adicionarArco("DFW", "JFK",1391)
grafo01.adicionarArco("ORD", "SFO",1846)
grafo01.adicionarArco("SFO", "ORD",1846)
grafo01.adicionarArco("ORD", "DFW",802)
grafo01.adicionarArco("DFW", "ORD",802)
grafo01.adicionarArco("ORD", "BWI",621)
grafo01.adicionarArco("BWI", "ORD",621)
grafo01.adicionarArco("BWI", "MIA",946)
grafo01.adicionarArco("MIA", "BWI",946)
grafo01.adicionarArco("MIA", "DFW",1121)
grafo01.adicionarArco("DFW", "MIA",1121)
grafo01.adicionarArco("MIA", "LAX",2342)
grafo01.adicionarArco("LAX", "MIA",2342)
grafo01.adicionarArco("DFW", "SFO",1464)
grafo01.adicionarArco("SFO", "DFW",1464)
grafo01.adicionarArco("DFW", "LAX",1235)
grafo01.adicionarArco("LAX", "DFW",1235)
grafo01.adicionarArco("SFO", "LAX",337)
grafo01.adicionarArco("LAX", "SFO",337)


print("El grafo es:\n",grafo01, sep="")
# print("Grados:")
# for vertice in grafo01.verVertices():
#     print("Grado",vertice,":",grafo01.verGradoEntrada(vertice),grafo01.verGradoSalida(vertice))
# print("DFS BOS:",grafo01.recorrerProfundidad("BOS"))
# print("DFS SFO:",grafo01.recorrerProfundidad("SFO"))
# print("BFS JFK:",grafo01.recorrerAnchura("JFK"))
print("Caminos Minimos")
algoritmo01 = Dijkstra(grafo01,"BWI")
algoritmo01.verDijkstra()
for vertice in grafo01.verVertices():
    print("Camino: BWI -",vertice,":",algoritmo01.obtenerCamino(vertice))
