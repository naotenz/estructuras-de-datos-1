import tkinter as tk
from model import Model
from view import View

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('MVC • Prefijo y Resultado')
        self.model = Model()
        self.view = View(self.root, on_calcular=self.on_calcular, on_cerrar=self.on_cerrar)

    def on_calcular(self, expr):
        prefijo = self.model.to_prefix(expr)
        resultado = self.model.evaluate(expr)
        numeros, operadores = self.model.get_pilas()
        self.view.set_prefijo(prefijo)
        self.view.set_resultado(resultado)
        self.view.set_pilas(numeros, operadores)

    def on_cerrar(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

