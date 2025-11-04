from listaSimple import ListaSimple

class ListaController:
    def __init__(self):
        self.modelo = ListaSimple()
        # Insertar figuras por defecto
        for figura in ["circulo", "triangulo", "cuadrado"]:
            self.modelo.insertar(figura)

    def get_actual(self):
        valor = self.modelo.get_actual()
        color = self.modelo.get_color(valor)
        return valor, color

    def next(self):
        self.modelo.siguiente()
        return self.get_actual()

    def back(self):
        self.modelo.anterior()
        return self.get_actual()
