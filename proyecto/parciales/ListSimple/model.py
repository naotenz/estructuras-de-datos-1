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
        self.colores = {"circulo": "red", "triangulo": "green", "cuadrado": "blue"}

    def insertar(self, valor):
        nodo = Nodo(valor)
        if not self.primero:
            self.primero = nodo
            nodo.siguiente = nodo.anterior = nodo
        else:
            ultimo = self.primero.anterior
            ultimo.siguiente = nodo
            nodo.anterior = ultimo
            nodo.siguiente = self.primero
            self.primero.anterior = nodo
        self.actual = self.primero

    def siguiente(self):
        if self.actual:
            self.actual = self.actual.siguiente
            if self.actual == self.primero:
                self._mezclar_colores()

    def anterior(self):
        if self.actual:
            self.actual = self.actual.anterior
            if self.actual == self.primero.anterior:
                self._mezclar_colores()

    def get_actual(self):
        return self.actual.valor if self.actual else None

    def get_color(self):
        return self.colores.get(self.actual.valor, "red")

    def _mezclar_colores(self):
        colores = ["red", "green", "blue"]
        figuras = list(self.colores.keys())
        random.shuffle(colores)
        for i, figura in enumerate(figuras):
            self.colores[figura] = colores[i]


