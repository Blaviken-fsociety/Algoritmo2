class GrafoLista:

    def __init__(self):
        self.listaAdyacencia = {}

    def __str__(self):
        string = ""
        for vertice, adyacentes in self.listaAdyacencia.items():
            adyacentes_str = ", ".join([f"({destino}, {peso})" for destino, peso in adyacentes])
            string += f"{vertice}: [{adyacentes_str}]\n"
        return string


    def agregarVertice(self, vertice):
        if vertice not in self.listaAdyacencia:
            self.listaAdyacencia[vertice] = []

    def agregarArco(self, vertice_inicial, vertice_final, peso):
        if vertice_inicial not in self.listaAdyacencia:
            self.listaAdyacencia[vertice_inicial] = []
        self.listaAdyacencia[vertice_inicial].append((vertice_final, peso))

    def obtenerVertices(self):
        return list(self.listaAdyacencia.keys())

    def obtenerAdyacentes(self, vertice):
        return [i[0] for i in self.listaAdyacencia[vertice]]

    def obtenerPesoArco(self, vertice_inicial, vertice_final):
        for ady in self.listaAdyacencia[vertice_inicial]:
            if ady[0] == vertice_final:
                return ady[1]

    def gradoSalida(self, vertice):
        adyacentes = self.buscarVertice(vertice)
        if adyacentes is None:
            return None
        return len(adyacentes)

    def gradoEntrada(self, vertice):
        grado = 0
        for vertice_actual in self.verVertices():
            if self.sonAdyacentes(vertice_actual, vertice):
                grado += 1
        return grado

    def eliminarArco(self, vertice_inicial, vertice_final):
        busqueda_inicial = self.buscarVertice(vertice_inicial)
        busqueda_final = self.buscarVertice(vertice_final)
        if busqueda_inicial is not None and busqueda_final is not None and self.sonAdyacentes(vertice_inicial, vertice_final):
            del busqueda_inicial[vertice_final]
            return True
        else:
            return False

    def eliminarVertice(self, vertice_eliminar):
        if self.buscarVertice(vertice_eliminar) is None:
            return False
        
        del self.__lista_vertices[vertice_eliminar]
        
        for vertice_actual, adyacentes in self.__lista_vertices.items():
            if vertice_eliminar in adyacentes:
                del adyacentes[vertice_eliminar]
        
        return True

    #RECORRIDOS
    #RECORRIDO EN PROFUNDIDAD DFS
    def __dfs(self, list_recorrido:list, set_visitados:set, vertice_actual):
        list_recorrido.append(vertice_actual)
        set_visitados.add(vertice_actual)
        adyacentes_actual = self.buscarVertice(vertice_actual)
        for ady_actual in adyacentes_actual:
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
        for ady_actual in adyacentes_actual_cola:
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
