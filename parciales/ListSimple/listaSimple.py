import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaSimple:
    def __init__(self):
        self.primero = None
        self.actual = None
        self.colores = {
            "circulo": "red",
            "triangulo": "green",
            "cuadrado": "blue"
        }

    def insertar(self, valor):
        nuevo = Nodo(valor)
        if not self.primero:
            self.primero = nuevo
            nuevo.siguiente = nuevo.anterior = nuevo
        else:
            ultimo = self.primero.anterior
            ultimo.siguiente = nuevo
            nuevo.anterior = ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
        self.actual = self.primero

    def siguiente(self):
        if self.actual:
            self.actual = self.actual.siguiente
            if self.actual == self.primero:
                self._cambiar_colores()

    def anterior(self):
        if self.actual:
            self.actual = self.actual.anterior
            if self.actual == self.primero.anterior:
                self._cambiar_colores()

    def get_actual(self):
        return self.actual.valor if self.actual else None

    def get_color(self, figura):
        return self.colores.get(figura, "red")

    def _cambiar_colores(self):
        colores = ["red", "green", "blue"]
        random.shuffle(colores)
        figuras = list(self.colores.keys())
        for i in range(3):
            self.colores[figuras[i]] = colores[i]
