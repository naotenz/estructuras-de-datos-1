from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty, BooleanProperty
from kivy.uix.widget import Widget
from controller import ListaController

KV = """
BoxLayout:
    orientation: "vertical"
    padding: 40
    spacing: 30

    FiguraWidget:
        id: figura_widget
        size_hint_y: 0.8

    BoxLayout:
        size_hint_y: None
        height: 60
        spacing: 20

        Button:
            text: "< Back"
            on_press: app.go_back()
        Button:
            text: "Next >"
            on_press: app.go_next()
"""

class FiguraWidget(Widget):
    forma = StringProperty("circulo")
    color_actual = ListProperty([1,0,0,1])

    def on_forma(self, *args):
        self.canvas.ask_update()

    def on_color_actual(self, *args):
        self.canvas.ask_update()

    def on_size(self, *args):
        self.canvas.ask_update()

    def on_pos(self, *args):
        self.canvas.ask_update()

    def on_kv_post(self, base_widget):
        self.bind(pos=self.update_canvas, size=self.update_canvas,
                  forma=self.update_canvas, color_actual=self.update_canvas)
        self.update_canvas()

    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            from kivy.graphics import Color, Ellipse, Rectangle, Triangle
            Color(*self.color_actual)

            cx, cy = self.center
            size = 150

            if self.forma == "circulo":
                Ellipse(pos=(cx - size/2, cy - size/2), size=(size, size))
            elif self.forma == "triangulo":
                Triangle(points=[cx, cy + size/2, cx - size/2, cy - size/2, cx + size/2, cy - size/2])
            elif self.forma == "cuadrado":
                Rectangle(pos=(cx - size/2, cy - size/2), size=(size, size))

class ListaView(App):
    figura_actual = StringProperty("circulo")
    color_actual = ListProperty([1,0,0,1])

    def build(self):
        self.controller = ListaController()
        self.root_widget = Builder.load_string(KV)
        self.figura_widget = self.root_widget.ids.figura_widget
        return self.root_widget

    def on_start(self):
        figura, color = self.controller.get_actual()
        self._update_view(figura, color)

    def go_next(self):
        figura, color = self.controller.next()
        self._update_view(figura, color)

    def go_back(self):
        figura, color = self.controller.back()
        self._update_view(figura, color)

    def _update_view(self, figura, color_name):
        self.figura_actual = figura
        colores_rgb = {"red":[1,0,0,1], "green":[0,1,0,1], "blue":[0,0,1,1]}
        self.color_actual = colores_rgb.get(color_name, [1,1,1,1])

        self.figura_widget.forma = self.figura_actual
        self.figura_widget.color_actual = self.color_actual

