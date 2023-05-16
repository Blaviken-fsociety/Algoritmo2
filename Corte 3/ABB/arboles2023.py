#Clase Arbol Binario General
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

#Clase Arbol Binario de Búsqueda (ABB)
class ArbolBinarioBusqueda:
    def __init__(self) -> None:
        self.raiz = None
    
    def estaVacio(self) -> bool:
        return self.raiz == None
    
    def __str__(self) -> str:
        if not self.estaVacio():
            return self.raiz.verArbol()
        return ""
    
    def __repr__(self) -> str:
        return self.__str__()
    
    #Recorrido
    def enOrden(self):
        if not self.estaVacio():
            return self.raiz.enOrden()
        return None

    #Insercion
    def insertar(self, elemento):
        if self.estaVacio():
            self.raiz = ArbolBinario(elemento)
        self.__insertar(self.raiz, elemento)

    def __insertar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is None:
                arbol.hijo_izquierdo = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_izquierdo, elemento)
        else:
            if arbol.hijo_derecho is None:
                arbol.hijo_derecho = ArbolBinario(elemento)
            else:
                self.__insertar(arbol.hijo_derecho, elemento)
    
    #Búsqueda
    def buscar(self, elemento) -> ArbolBinario:
        if not self.estaVacio():
            return self.__buscar(self.raiz, elemento)
        return None
    
    def __buscar(self, arbol:ArbolBinario, elemento):
        if elemento == arbol.valor_nodo:
            return arbol
        if elemento < arbol.valor_nodo:
            if arbol.hijo_izquierdo is not None:
                return self.__buscar(arbol.hijo_izquierdo, elemento)
            else:
                return None
        else:
            if arbol.hijo_derecho is not None:
                return self.__buscar(arbol.hijo_derecho, elemento)
            else:
                return None
    #Eliminar
    def eliminar(self, elemento):
        if not self.estaVacio():
            return self.__eliminar(self.raiz, elemento, None)
        return False
    
    def __eliminar(self, arbol:ArbolBinario, elemento, padre:ArbolBinario):
        if arbol is None:
            return False
        if elemento < arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_izquierdo, elemento, arbol)
        elif elemento > arbol.valor_nodo:
            return self.__eliminar(arbol.hijo_derecho, elemento, arbol)
        else:
            #Caso Nodo hoja
            if arbol.esHoja():
                #Caso Nodo Hoja y Raiz
                if arbol == self.raiz:
                    self.raiz = None
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = None
                else:
                    padre.hijo_derecho = None
                return True
            #Caso Nodo con un hijo
            if arbol.hijo_izquierdo is None and arbol.hijo_derecho is not None:
                #Nodo con hijo derecho únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_derecho
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_derecho
                else:
                    padre.hijo_derecho = arbol.hijo_derecho
                return True
            if arbol.hijo_izquierdo is not None and arbol.hijo_derecho is None:
                #Nodo con hijo izquierdo únicamente
                #Caso Raiz
                if arbol == self.raiz:
                    self.raiz = arbol.hijo_izquierdo
                    return True
                #Actualizacion enlace nodo padre
                if padre.hijo_izquierdo is not None and padre.hijo_izquierdo == arbol:
                    padre.hijo_izquierdo = arbol.hijo_izquierdo
                else:
                    padre.hijo_derecho = arbol.hijo_izquierdo
                return True
            #Caso Nodo interno
            nodo_izquierdo:ArbolBinario = arbol.hijo_izquierdo
            nodo_temporal:ArbolBinario = None            
            while nodo_izquierdo.hijo_derecho is not None:
                nodo_temporal = nodo_izquierdo
                nodo_izquierdo = nodo_izquierdo.hijo_derecho
            arbol.valor_nodo = nodo_izquierdo.valor_nodo
            if nodo_temporal is None:
                arbol.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_izquierdo == nodo_izquierdo:
                nodo_temporal.hijo_izquierdo = nodo_izquierdo.hijo_izquierdo
            elif nodo_temporal.hijo_derecho == nodo_izquierdo:
                nodo_temporal.hijo_derecho = nodo_izquierdo.hijo_izquierdo
            return True
    
    def encontrarPadre(self, elemento):
        if not self.estaVacio():
            return self.__encontrarPadre(self.raiz, elemento, None)
        return None

    def __encontrarPadre(self, arbol: ArbolBinario, elemento, padre: ArbolBinario):
        if arbol is None:
            return None
        if elemento == arbol.valor_nodo:
            return padre
        if elemento < arbol.valor_nodo:
            return self.__encontrarPadre(arbol.hijo_izquierdo, elemento, arbol)
        else:
            return self.__encontrarPadre(arbol.hijo_derecho, elemento, arbol)
    
    def elementos_maxima_profundidad(self):
        if self.estaVacio():
            return []

        max_depth = self.__calcular_maxima_profundidad(self.raiz)
        return self.__obtener_elementos_maxima_profundidad(self.raiz, max_depth, 1)

    def __calcular_maxima_profundidad(self, nodo):
        if nodo is None:
            return 0

        left_depth = self.__calcular_maxima_profundidad(nodo.hijo_izquierdo)
        right_depth = self.__calcular_maxima_profundidad(nodo.hijo_derecho)

        return max(left_depth, right_depth) + 1

    def __obtener_elementos_maxima_profundidad(self, nodo, max_depth, current_depth):
        if nodo is None:
            return []

        if current_depth == max_depth:
            return [nodo.valor_nodo]

        left_elements = self.__obtener_elementos_maxima_profundidad(nodo.hijo_izquierdo, max_depth, current_depth + 1)
        right_elements = self.__obtener_elementos_maxima_profundidad(nodo.hijo_derecho, max_depth, current_depth + 1)

        return left_elements + right_elements
    
    def encontrar_valor_mas_cercano_encima(self, dato):
        if self.estaVacio():
            return None
    
        valor_mas_cercano = None
        nodo_actual = self.raiz

        while nodo_actual is not None:
            if nodo_actual.valor_nodo > dato:
                # Actualizar el valor más cercano si es mayor que el dato y más cercano hasta ahora
                if valor_mas_cercano is None or nodo_actual.valor_nodo < valor_mas_cercano:
                    valor_mas_cercano = nodo_actual.valor_nodo
                nodo_actual = nodo_actual.hijo_izquierdo
            else:
                nodo_actual = nodo_actual.hijo_derecho
    
        return valor_mas_cercano

    def menorNodo(self):
        if not self.estaVacio():
            menor = self.raiz
            return self.__menorNodoRecursivo(self.raiz, menor)
            return None

    def __menorNodoRecursivo(self, arbol: ArbolBinario, menor: ArbolBinario):
        if arbol is None:
            return None
        if arbol.valor_nodo < menor.valor_nodo:
            menor = arbol
        menorIzquierdo = self.__menorNodoRecursivo(arbol.hijo_izquierdo, menor)
        if menorIzquierdo is not None and menorIzquierdo.valor_nodo < menor.valor_nodo:
            menor = menorIzquierdo
        menorDerecho = self.__menorNodoRecursivo(arbol.hijo_derecho, menor)
        if menorDerecho is not None and menorDerecho.valor_nodo < menor.valor_nodo:
            menor = menorDerecho
        return menor

    def mayorNodo(self):
        if not self.estaVacio():
            mayor = self.raiz
            return self.__mayorNodoRecursivo(self.raiz, mayor)
        return None

    def __mayorNodoRecursivo(self, arbol: ArbolBinario, mayor: ArbolBinario):
        if arbol is None:
            return mayor
        if arbol.valor_nodo > mayor.valor_nodo:
            mayor = arbol
        mayorIzquierdo = self.__mayorNodoRecursivo(arbol.hijo_izquierdo, mayor)
        mayorDerecho = self.__mayorNodoRecursivo(arbol.hijo_derecho, mayor)
        if mayorIzquierdo.valor_nodo > mayor.valor_nodo:
            mayor = mayorIzquierdo
        if mayorDerecho.valor_nodo > mayor.valor_nodo:
            mayor = mayorDerecho
        return mayor
    
    def factorEquilibrio(self):
        if self.estaVacio():
            return 0
        return self.__factorEquilibrio(self.raiz)

    def __factorEquilibrio(self, arbol: ArbolBinario):
        if arbol is None:
            return 0
        altura_izquierdo = self.__calcularAltura(arbol.hijo_izquierdo)
        altura_derecho = self.__calcularAltura(arbol.hijo_derecho)
        return altura_izquierdo - altura_derecho

    def __calcularAltura(self, arbol: ArbolBinario):
        if arbol is None:
            return 0
        altura_izquierdo = self.__calcularAltura(arbol.hijo_izquierdo)
        altura_derecho = self.__calcularAltura(arbol.hijo_derecho)
        return max(altura_izquierdo, altura_derecho) + 1