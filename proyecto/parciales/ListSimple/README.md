# Lista Simple Circular con Kivy - MVC

Este proyecto es una implementación de una **lista circular simple** con **interfaz gráfica usando Kivy**, siguiendo el patrón **MVC (Modelo-Vista-Controlador)**.  

Las figuras (`círculo`, `triángulo`, `cuadrado`) se muestran en la ventana, con **colores dinámicos** (rojo, verde, azul) que se mezclan cuando se llega al final de la lista.  

## Funcionalidades

- Navegar entre elementos con **Next >** y **< Back**.  
- Cada figura tiene un color asignado.  
- Al volver al inicio, los colores se mezclan aleatoriamente entre las figuras.  
- Se muestra la forma real (círculo, triángulo, cuadrado) en la pantalla.  

## Estructura MVC

ListSimple/
├── main.py # Ejecutable principal
├── model.py # Modelo: ListaCircular y lógica de colores
├── controller.py # Controlador: maneja Next y Back
└── view.py # Vista: interfaz Kivy y dibujo de figuras


## Requisitos

- Python 3.13+
- Kivy 2.3.1  

Instalar Kivy:

```bash
pip install kivy
