import sys
#Clase Arco
class Arco:
    def __init__(self, vertice_inicial, vertice_final, peso:int) -> None:
        self.vertice_inicial = vertice_inicial
        self.vertice_final = vertice_final
        self.peso = peso
    
    def __repr__(self) -> str:
        return "["+str(self.vertice_inicial)+", "+str(self.vertice_final)+"]: "+str(self.peso)
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, Arco):
            return False
        return self.vertice_inicial == otro.vertice_inicial and \
               self.vertice_final == otro.vertice_final and self.peso == otro.peso
    
    def __hash__(self) -> int:
        return hash(str(self))
#Clase Grafo
class GrafoLista:
    def __init__(self) -> None:
        self.__lista_vertices = dict()
    
    def __str__(self) -> str:
        return str(self.__lista_vertices)
    
    def buscarVertice(self, dato_buscar):
        return self.__lista_vertices.get(dato_buscar)
    
    def adicionarVertice(self, dato_nuevo_vertice):
        if self.buscarVertice(dato_nuevo_vertice) is None:
            lista_adyacentes = set()
            self.__lista_vertices[dato_nuevo_vertice] = lista_adyacentes
    
    def verVertices(self):
        return list(self.__lista_vertices.keys())
    
    def adicionarArco(self, vertice_inicial, vertice_final, peso:int = 0):
        busqueda_inicial = self.buscarVertice(vertice_inicial)
        busqueda_final = self.buscarVertice(vertice_final)        
        if busqueda_inicial is None or busqueda_final is None:
            return False
        #Creacion de arco
        arco_nuevo = Arco(vertice_inicial, vertice_final, peso)
        busqueda_inicial.add(arco_nuevo)
    
    def sonAdyacentes(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.buscarVertice(vertice_inicial)
        busqueda_final = self.buscarVertice(vertice_final)
        if busqueda_inicial is None or busqueda_final is None:
            return False
        for arco in busqueda_inicial:
            if arco.vertice_final == vertice_final:
                return True
        return False

    def hayCamino(self, vertice_inicial, vertice_final):
        if self.buscarVertice(vertice_inicial) is None or self.buscarVertice(vertice_final) is None:
            return False
        visitados = set()
        return self.__dfsCamino(visitados, vertice_inicial, vertice_final)
        
    def __dfsCamino(self, visitados:set, vertice_actual, vertice_final):
        visitados.add(vertice_actual)
        if vertice_actual == vertice_final:
            return True
        adyacentes_actual = self.buscarVertice(vertice_actual)
        for arco_ady_actual in adyacentes_actual:
            ady_actual = arco_ady_actual.vertice_final
            if ady_actual not in visitados and self.__dfsCamino(visitados, ady_actual, vertice_final):
                return True
        return False

    def tieneCiclo(self):
        visitados = set()
        pila = []
        for vertice in self.verVertices():
            if vertice not in visitados:
                if self.__tieneCicloUtil(vertice, visitados, pila):
                    return True
        return False
    
    def __tieneCicloUtil(self, vertice_actual, visitados, pila):
        visitados.add(vertice_actual)
        pila.append(vertice_actual)
        adyacentes_actual = self.buscarVertice(vertice_actual)
        for arco_ady_actual in adyacentes_actual:
            ady_actual = arco_ady_actual.vertice_final
            if ady_actual not in visitados:
                if self.__tieneCicloUtil(ady_actual, visitados, pila):
                    return True
            elif ady_actual in pila:
                return True
        pila.remove(vertice_actual)
        return False   
    
    def esFuertementeConexo(self):
        for vertice in self.verVertices():
            visitados = set()
            self.__dfs(list(), visitados, vertice)
            if len(visitados) != len(self.verVertices()):
                return False
        return True
    
    def esCompleto(self):
        # Verificar grafo no dirigido
        num_vertices = len(self.__lista_vertices)
        for vertice in self.verVertices():
            adyacentes = self.buscarVertice(vertice)
            if len(adyacentes) != num_vertices - 1:
                return False
            for otro_vertice in self.verVertices():
                if otro_vertice != vertice and not self.sonAdyacentes(vertice, otro_vertice):
                    return False
        return True
        
        # Verificar grafo dirigido
        for vertice in self.verVertices():
            adyacentes_salida = set()
            adyacentes_entrada = set()
            for arco in self.buscarVertice(vertice):
                adyacentes_salida.add(arco.vertice_final)
                adyacentes_entrada.add(arco.vertice_inicial)
            if len(adyacentes_salida) != num_vertices - 1 or len(adyacentes_entrada) != num_vertices - 1:
                return False
            for otro_vertice in self.verVertices():
                if otro_vertice != vertice and (not self.sonAdyacentes(vertice, otro_vertice) or not self.sonAdyacentes(otro_vertice, vertice)):
                    return False
        return True

    #RECORRIDOS
    #RECORRIDO EN PROFUNDIDAD DFS
    def __dfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        adyacentes_actual = self.buscarVertice(vertice_actual)
        for arco_ady_actual in adyacentes_actual:
            ady_actual = arco_ady_actual.vertice_final
            if ady_actual not in set_visitados:
                list_recorrido, set_visitados = self.__dfs(list_recorrido, set_visitados, ady_actual)
        return list_recorrido, set_visitados

    def recorrerProfundidad(self, vertice_inicial):        
        if self.buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__dfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__dfs(recorrido, visitados, vertice)
        return recorrido
    
    #RECORRIDO EN ANCHURA BFS    
    def __bfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        cola_ady = [vertice_actual]
        while cola_ady:
            vertice_cola = cola_ady.pop(0)        
            adyacentes_actual_cola = self.buscarVertice(vertice_cola)
            for arco_ady_actual in adyacentes_actual_cola:
                ady_actual = arco_ady_actual.vertice_final
                if ady_actual not in set_visitados:
                    list_recorrido.append(ady_actual)
                    set_visitados.add(ady_actual)
                    cola_ady.append(ady_actual)
        return list_recorrido, set_visitados

    def recorrerAnchura(self, vertice_inicial):
        if self.buscarVertice(vertice_inicial) is None:
            return None        
        recorrido, visitados = self.__bfs(list(), set(), vertice_inicial)
        for vertice in self.verVertices():
            if vertice not in visitados:
                recorrido, visitados = self.__bfs(recorrido, visitados, vertice)
        return recorrido
    
    #ALGORITMO DE CAMINOS MINIMOS DIJKSTRA
class Dijkstra:
    def __init__(self, grafo:GrafoLista, vertice_inicial) -> None:    
        self.__vertices_ubicados = set()
        self.__vertices_sin_ubicar = set()
        self.__distancia = dict()
        self.__predecesores = dict()
        self.__vertice_inicial = vertice_inicial
        self.__grafo = grafo
    
    
    #Verifica el valor de la distancia actual a un vertice dado
    def __calcularDistanciaMasCorta(self, vertice):
        distancia_vertice = self.__distancia.get(vertice)
        if distancia_vertice is None:
            return sys.maxsize
        else:
            return distancia_vertice
    
    #Ubica el siguiente vertice a visitar por distancia
    def __buscarMinimo(self, vertices):
        vertice_minimo = None
        for vertice_actual in vertices:
            if vertice_minimo is None:
                vertice_minimo = vertice_actual
            else:
                if self.__calcularDistanciaMasCorta(vertice_actual) < self.__calcularDistanciaMasCorta(vertice_minimo):
                    vertice_minimo = vertice_actual
        return vertice_minimo

    #Actualiza las distancias del algoritmo
    def __buscarDistanciasMinimas(self, vertice):
        adyacentes = self.__grafo.buscarVertice(vertice)
        for arco_ady in adyacentes:
            vertice_ady = arco_ady.vertice_final
            if self.__calcularDistanciaMasCorta(vertice_ady) > self.__calcularDistanciaMasCorta(vertice) + arco_ady.peso:
                self.__distancia[vertice_ady] = self.__calcularDistanciaMasCorta(vertice) + arco_ady.peso
                self.__predecesores[vertice_ady] = vertice
                self.__vertices_sin_ubicar.add(vertice_ady)

    #Inicializar algoritmo
    def verDijkstra(self):
        #Inicializacion
        self.__distancia[self.__vertice_inicial] = 0
        self.__vertices_sin_ubicar.add(self.__vertice_inicial)
        while self.__vertices_sin_ubicar:
            mejor_vertice = self.__buscarMinimo(self.__vertices_sin_ubicar)
            self.__vertices_ubicados.add(mejor_vertice)
            self.__vertices_sin_ubicar.remove(mejor_vertice)            
            self.__buscarDistanciasMinimas(mejor_vertice)

    #Informa de los caminos generados
    def obtenerCamino(self, vertice_final):
        camino_encontrado = []
        vertice_actual = vertice_final
        if self.__predecesores.get(vertice_actual) is None:
            return None
        camino_encontrado.append(vertice_actual)
        while self.__predecesores.get(vertice_actual):
            vertice_actual = self.__predecesores[vertice_actual]
            camino_encontrado.append(vertice_actual)
        camino_encontrado.reverse()
        return camino_encontrado