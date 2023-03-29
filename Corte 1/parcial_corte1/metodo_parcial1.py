class ListaSimple:
    def __init__(self):
        self.head = None
        self.length = 0

    def insertar_al_comienzo(self, valor):
        nodo = Nodo(valor)
        nodo.siguiente = self.head
        self.head = nodo
        self.length += 1

    def eliminar_por_valor(self, valor):
        if self.head is None:
            return

        if self.head.valor == valor:
            self.head = self.head.siguiente
            self.length -= 1
            return

        nodo_actual = self.head
        while nodo_actual.siguiente is not None:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                self.length -= 1
                return
            nodo_actual = nodo_actual.siguiente

    def contar(self, valor, cantidad):
        contador = 0
        nodo_actual = self.head
        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador == cantidad

class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None  