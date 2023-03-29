class Lista(list):
    def dato_mas_comun(self):
        if len(self) == 0:
            return None
        elif len(self) == 1:
            return self[0]
        else:
            # Inicializamos un diccionario para contar las ocurrencias de cada elemento
            contador = {}
            for dato in self:
                if dato in contador:
                    contador[dato] += 1
                else:
                    contador[dato] = 1
            
            # Encontramos el dato más común y la cantidad de veces que aparece
            mas_comun = None
            mas_comun_cuenta = 0
            for dato, cuenta in contador.items():
                if cuenta > mas_comun_cuenta:
                    mas_comun = dato
                    mas_comun_cuenta = cuenta
            
            # Verificamos si hay un solo elemento o si no hay elementos repetidos
            if mas_comun_cuenta == 1:
                return "No hay un elemento que se repita más que los demás."
            else:
                return mas_comun

    def cuenta_elementos(self, dato):
        cuenta = 0
        for elemento in self:
            if elemento == dato:
                cuenta += 1
        return cuenta