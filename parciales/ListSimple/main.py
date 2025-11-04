from kivy.app import App
from kivy.properties import ListProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from controller import ListaController

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 40
    spacing: 30

    Widget:
        id: figura_widget
        size_hint_y: 0.8
        canvas.before:
            Clear
            Color:
                rgba: app.color_actual
            Ellipse:
                size: (150, 150) if app.forma_actual == "circulo" else (0, 0)
                pos: self.center_x - 75, self.center_y - 75
            Triangle:
                points: (self.center_x, self.center_y + 80,
                         self.center_x - 80, self.center_y - 80,
                         self.center_x + 80, self.center_y - 80) if app.forma_actual == "triangulo" else (0,0,0,0,0,0)
            Rectangle:
                size: (150, 150) if app.forma_actual == "cuadrado" else (0,0)
                pos: self.center_x - 75, self.center_y - 75

    BoxLayout:
        size_hint_y: None
        height: "60dp"
        spacing: 20

        Button:
            text: "< Back"
            on_press: app.go_back()

        Button:
            text: "Next >"
            on_press: app.go_next()
"""

class ListaApp(App):
    color_actual = ListProperty([1, 0, 0, 1])
    forma_actual = StringProperty("circulo")

    def build(self):
        self.controller = ListaController()
        return Builder.load_string(KV)

    def on_start(self):
        valor, color = self.controller.get_actual()
        self._update_view(valor, color)

    def go_next(self):
        valor, color = self.controller.next()
        self._update_view(valor, color)

    def go_back(self):
        valor, color = self.controller.back()
        self._update_view(valor, color)

    def _update_view(self, valor, color_name):
        self.forma_actual = valor
        colores_rgb = {
            "red": [1, 0, 0, 1],
            "green": [0, 1, 0, 1],
            "blue": [0, 0, 1, 1],
        }
        self.color_actual = colores_rgb.get(color_name, [1, 1, 1, 1])

if __name__ == "__main__":
    ListaApp().run()
