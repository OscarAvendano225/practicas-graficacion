import tkinter as tk
import math
#librerias que vamos a importar para realizar estas representaciones en 2d

#pasamos a definir las dimensiones del área del dibujo que vamos a usar
ancho = 800 #Ancho del área de dibujo en pixeles
alto = 520 #Alto del área de dibujo en pixeles
unidad = 35 #Tamaño de la unidad de medida en pixeles

#Primera lista de coordenadas
coordenadas_originales = [
    [0, -2, 1],
    [2, -2, 1],
    [2, 1, 1],
    [0, 3, 1]
]

#esta linea lo que hace es un tipo de for que recorre
#todos los elementos de la lista de coordenadas originales
#y los copia en una nueva lista llamada puntos
puntos = [p[:] for p in coordenadas_originales]