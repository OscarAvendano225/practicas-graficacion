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

def transformar(matriz):
    """Multiplica cada vértice por una matriz de transformación 3x3"""

    # Recorre todos los puntos y los multiplica por la matriz de transformación
    global puntos

    #nueva lista para almacenar los nuevos puntos transformados
    nuevos = []

    #Primero vamos a poner lo de la matriz. y su recorrido. 

    print("\n========== TRANSFORMACIÓN ==========")
    print("Matriz recibida:")
    for fila in matriz:
        print(fila)

    #Luego vamos a recorrer todos los puntos de la lista de puntos
    for i, punto in enumerate(puntos):
        print(f"\nProcesando vértice P{i + 1}: {punto}")

        #Por lo que entiendo resultado es una lista que va a almacenar los nuevos valores de cada punto transformado
        resultado = []

        #Ahora vamos a recorrer cada fila de la matriz de transformación
        for fila in range(3):
            suma = 0

            #Este print es para mostrar que estamos calculando la componente de la fila actual
            print(f" Calculando componente {fila}:")

            #Ahora vamos a recorrer cada columna de la matriz de transformación
            for columna in range(3):
                #acá lo que hacemos es obtener el valor de la matriz en la posición actual (fila, columna) y el valor del punto en la posición de la columna actual
                a = matriz[fila][columna]
                #y acá lo que hacemos es obtener el valor del punto en la posición de la columna actual
                b = punto[columna]

                #Multiplicamos el valor de la matriz por el valor del punto y lo almacenamos en producto
                producto = a * b
                #Acá lo que hacemos es acumular el valor del producto en la variable suma
                suma = suma + producto

                #Este print es para mostrar el resultado de la multiplicación y la suma acumulada
                print(
                    f"     {a} × {b} = {producto}"
                    f" | Acumulado: {suma}"
                )