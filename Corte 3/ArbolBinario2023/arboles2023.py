#Clase Arbol
class ArbolBinario:
    def __init__(self, dato, arbol_izquierdo = None, arbol_derecho = None) -> None:
        self.valor_nodo = dato
        self.hijo_izquierdo = arbol_izquierdo
        self.hijo_derecho = arbol_derecho     

    def esHoja(self):
        return self.hijo_izquierdo == None and self.hijo_derecho == None
    
    def __str__(self) -> str:
        return str(self.valor_nodo)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, ArbolBinario):
            return False
        return self.valor_nodo == otro.valor_nodo

    #Visualización Arbol      
    def verArbol(self) -> str: 
        return self.__verArbol(self,"")
    
    def __verArbol(self, arbol:"ArbolBinario", recorrido:str, nivel = 0) -> str:
        espaciado = "\t" * nivel        
        if arbol is None:
            return ""
        recorrido =  espaciado + str(arbol.valor_nodo) + "\n" \
            + str(self.__verArbol(arbol.hijo_izquierdo, recorrido, nivel+1)) + \
            str(self.__verArbol(arbol.hijo_derecho, recorrido, nivel + 1)) + recorrido
        return recorrido        
    
    def nodosHoja(self):
        hojas = []
        self.__nodosHoja(self, hojas)
        return hojas

    def __nodosHoja(self, arbol, hojas):
        if arbol is not None:
            if arbol.esHoja():
                hojas.append(arbol)
            self.__nodosHoja(arbol.hijo_izquierdo, hojas)
            self.__nodosHoja(arbol.hijo_derecho, hojas)

    def contarNodos(self):
        return self.__contarNodos(self)

    def __contarNodos(self, arbol):
        if arbol is None:
            return 0
        return 1 + self.__contarNodos(arbol.hijo_izquierdo) + self.__contarNodos(arbol.hijo_derecho)

    def altura(self):
        return self.__altura(self)
    
    def __altura(self, arbol):
        if arbol is None:
            return 0
        altura_izq = self.__altura(arbol.hijo_izquierdo)
        altura_der = self.__altura(arbol.hijo_derecho)
        return max(altura_izq, altura_der) + 1
    
    def numNodosEnNivel(self, nivel):
        return self.__numNodosEnNivel(self, nivel, 0)
    
    def __numNodosEnNivel(self, arbol, nivel_actual, nivel_actual_actual):
        if arbol is None:
            return 0
        
        if nivel_actual == nivel_actual_actual:
            return 1
        
        return self.__numNodosEnNivel(arbol.hijo_izquierdo, nivel_actual, nivel_actual_actual + 1) + \
               self.__numNodosEnNivel(arbol.hijo_derecho, nivel_actual, nivel_actual_actual + 1)

    def esCompleto(self):
        return self.__esCompleto(self)

    def __esCompleto(self, arbol):
        if arbol is None:
            return True

        if arbol.hijo_izquierdo is None and arbol.hijo_derecho is not None:
            return False

        if arbol.hijo_izquierdo is not None and arbol.hijo_derecho is None:
            return False

        return (
            self.__esCompleto(arbol.hijo_izquierdo) and
            self.__esCompleto(arbol.hijo_derecho)
        )
    
    #RECORRIDOS
    #Preorden
    def preOrden(self):
        visitados = list()
        self.__preOrden(self, visitados)
        return visitados
    
    def __preOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados.append(arbol)
            visitados = self.__preOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__preOrden(arbol.hijo_derecho, visitados)
        return visitados
    #EnOrden
    def enOrden(self):
        visitados = list()
        self.__enOrden(self, visitados)
        return visitados
    
    def __enOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__enOrden(arbol.hijo_izquierdo, visitados)
            visitados.append(arbol)
            visitados = self.__enOrden(arbol.hijo_derecho, visitados)
        return visitados
    #PosOrden
    def posOrden(self):
        visitados = list()
        self.__posOrden(self, visitados)
        return visitados
    
    def __posOrden(self, arbol:"ArbolBinario", visitados:list):
        if arbol is not None:
            visitados = self.__posOrden(arbol.hijo_izquierdo, visitados)
            visitados = self.__posOrden(arbol.hijo_derecho, visitados)
            visitados.append(arbol)
        return visitados