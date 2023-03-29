class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.cabeza = None
        self.longitud = 0
    
    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.longitud += 1
    
    def eliminar_ultimo(self):
        if self.cabeza is None:
            raise ValueError("La lista está vacía")
        if self.cabeza.siguiente is None:
            self.cabeza = None
        else:
            actual = self.cabeza
            while actual.siguiente.siguiente:
                actual = actual.siguiente
            actual.siguiente = None
        self.longitud -= 1
    
    def apariciones(self, dato):
        contador = 0
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                contador += 1
            actual = actual.siguiente
        return contador
    
    def elemento_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.longitud:
            raise ValueError("Posición inválida")
        actual = self.cabeza
        for i in range(posicion):
            actual = actual.siguiente
        return actual.dato
    
    def ultimo_elemento(self):
        if self.cabeza is None:
            raise ValueError("La lista está vacía")
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        return actual.dato
    
    def eliminar_en_posicion(self, posicion):
        if posicion < 0 or posicion >= self.longitud:
            raise ValueError("Posición inválida")
        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            for i in range(posicion - 1):
                actual = actual.siguiente
            actual.siguiente = actual.siguiente.siguiente
        self.longitud -= 1