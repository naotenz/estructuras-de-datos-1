import tkinter as tk
from tkinter import ttk

class View:
    def __init__(self, root, on_calcular, on_cerrar):
        self.on_calcular = on_calcular
        self.on_cerrar = on_cerrar
        self._build(root)

    def _build(self, root):
        main = ttk.Frame(root, padding=12)
        main.grid(sticky='nsew')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Entrada y botón calcular
        row0 = ttk.Frame(main)
        row0.grid(row=0, column=0, sticky='ew', pady=(0,8))
        row0.columnconfigure(1, weight=1)
        ttk.Label(row0, text='Expresión (ej: 3*2-1+5):').grid(row=0, column=0, padx=(0,8))
        self.entry = ttk.Entry(row0)
        self.entry.grid(row=0, column=1, sticky='ew')
        ttk.Button(row0, text='Calcular', command=self._click).grid(row=0, column=2, padx=(8,0))

        # Prefijo y resultado
        cards = ttk.Frame(main)
        cards.grid(row=1, column=0, sticky='ew', pady=(0,8))
        for i in range(2):
            cards.columnconfigure(i, weight=1)

        self.pref_var = tk.StringVar(value='')
        self.res_var = tk.StringVar(value='')
        self.nums_var = tk.StringVar(value='[]')
        self.ops_var = tk.StringVar(value='[]')

        ttk.Label(cards, text='Prefijo:').grid(row=0, column=0, sticky='w')
        ttk.Label(cards, textvariable=self.pref_var, anchor='w').grid(row=0, column=1, sticky='w')
        ttk.Label(cards, text='Resultado:').grid(row=1, column=0, sticky='w')
        ttk.Label(cards, textvariable=self.res_var, anchor='w').grid(row=1, column=1, sticky='w')
        ttk.Label(cards, text='Pila números:').grid(row=2, column=0, sticky='w')
        ttk.Label(cards, textvariable=self.nums_var).grid(row=2, column=1, sticky='w')
        ttk.Label(cards, text='Pila operadores:').grid(row=3, column=0, sticky='w')
        ttk.Label(cards, textvariable=self.ops_var).grid(row=3, column=1, sticky='w')

        # Botón cerrar
        ttk.Button(main, text='Cerrar', command=self.on_cerrar).grid(row=2, column=0, pady=(10,0))

    def _click(self):
        self.on_calcular(self.entry.get())

    def set_prefijo(self, texto):
        self.pref_var.set(texto)

    def set_resultado(self, texto):
        self.res_var.set(texto)

    def set_pilas(self, numeros, operadores):
        self.nums_var.set(str(numeros))
        self.ops_var.set(str(operadores))

