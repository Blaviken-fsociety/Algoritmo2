class Nodo:
    def __init__(self, pregunta=None, animal=None):
        self.pregunta = pregunta
        self.animal = animal
        self.izquierda = None
        self.derecha = None
        self.padre = None

class JuegoAdivinar:
    def __init__(self):
        self.raiz = None
        self.actual = None

    def jugar(self):
        while True:
            print("Menú de Categorías:")
            print("1. Animales")
            print("2. Personajes")
            print("3. Flores")
            print("4. Salir")

            opcion = input("Digite opción: ")
            if opcion == "1":
                self.inicializar_animales()
                self.jugar_juego()
            elif opcion == "2":
                self.inicializar_personajes()
                self.jugar_juego()
            elif opcion == "3":
                self.inicializar_flores()
                self.jugar_juego()
            elif opcion == "4":
                break
            else:
                print("Opción inválida. Intente de nuevo.")

    def jugar_juego(self):
        self.actual = self.raiz

        while self.actual and self.actual.pregunta:
            respuesta = input(self.actual.pregunta + " (si/no): ")
            self.actual = self.actual.izquierda if respuesta.lower() == "si" else self.actual.derecha

        if self.actual is None:
            print("No tengo suficiente información para adivinar.")
            return

        if self.actual.animal:
            animal = input("Ya sé, es un(a) " + self.actual.animal + ". ¿He adivinado? (si/no): ")
            if animal.lower() == "no":
                diferencia = input("¿Cuál es tu Animal? ")
                pregunta = input("¿Qué diferencia a un(a) " + self.actual.animal + " de un(a) " + diferencia + "? ")

                nuevo_animal = Nodo(animal=diferencia)
                nueva_pregunta = Nodo(pregunta=pregunta)

                if respuesta.lower() == "si":
                    nueva_pregunta.izquierda = nuevo_animal
                    nueva_pregunta.derecha = self.actual
                else:
                    nueva_pregunta.derecha = nuevo_animal
                    nueva_pregunta.izquierda = self.actual

                if self.actual == self.raiz:
                    self.raiz = nueva_pregunta
                else:
                    padre = self.actual.padre
                    nueva_pregunta.padre = padre
                    if padre.izquierda == self.actual:
                        padre.izquierda = nueva_pregunta
                    else:
                        padre.derecha = nueva_pregunta

                nuevo_animal.padre = nueva_pregunta
                self.actual.padre = nueva_pregunta

            else:
                print("¡¡He adivinado!!")
        else:
            print("No tengo suficiente información para adivinar.")

    def inicializar_animales(self):
        self.raiz = Nodo(pregunta="¿Es mamífero?")
        self.actual = self.raiz

        self.raiz.izquierda = Nodo(pregunta="¿Tiene plumas?", animal="Pájaro")
        self.raiz.derecha = Nodo(pregunta="¿Tiene pelo?", animal="Perro")

        self.raiz.izquierda.izquierda = Nodo(animal="Avestruz")
        self.raiz.izquierda.derecha = Nodo(pregunta="¿Vuela?", animal="Murciélago")

        self.raiz.derecha.izquierda = Nodo(pregunta="¿Ronronea?", animal="Gato")
        self.raiz.derecha.derecha = Nodo(pregunta="¿Es acuático?", animal="Ballena")

    def inicializar_personajes(self):
        self.raiz = Nodo(pregunta="¿Es real?")
        self.actual = self.raiz

        self.raiz.izquierda = Nodo(pregunta="¿Tiene poderes?", animal="Superhéroe")
        self.raiz.derecha = Nodo(pregunta="¿Es de ficción?", animal="Personaje de libro")

        self.raiz.izquierda.izquierda = Nodo(animal="Superman")
        self.raiz.izquierda.derecha = Nodo(animal="Spiderman")

        self.raiz.derecha.izquierda = Nodo(animal="Harry Potter")
        self.raiz.derecha.derecha = Nodo(animal="Sherlock Holmes")

    def inicializar_flores(self):
        self.raiz = Nodo(pregunta="¿Tiene pétalos?")
        self.actual = self.raiz

        self.raiz.izquierda = Nodo(pregunta="¿Es una flor silvestre?", animal="Margarita")
        self.raiz.derecha = Nodo(pregunta="¿Se usa como decoración?", animal="Rosa")

        self.raiz.izquierda.izquierda = Nodo(animal="Orquídea")
        self.raiz.izquierda.derecha = Nodo(animal="Tulipán")

        self.raiz.derecha.izquierda = Nodo(animal="Lirio")
        self.raiz.derecha.derecha = Nodo(animal="Girasol")

# Crear instancia del juego y jugar
juego = JuegoAdivinar()
juego.jugar()



