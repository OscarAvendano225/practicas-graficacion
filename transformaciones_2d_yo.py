#Importamos tkinter con el nombre tk para crear la ventana y sus elementos
import tkinter as tk
#Importamos math para convertir ángulos y calcular el seno y el coseno
import math
#librerias que vamos a importar para realizar estas representaciones en 2d

#pasamos a definir las dimensiones del área del dibujo que vamos a usar
ancho = 800 #Ancho del área de dibujo en pixeles
alto = 520 #Alto del área de dibujo en pixeles
unidad = 35 #Tamaño de la unidad de medida en pixeles

#Primera lista de coordenadas
coordenadas_originales = [
    #Este es el primer vértice, ubicado en X = 0 y Y = -2
    [0, -2, 1],
    #Este es el segundo vértice, ubicado en X = 2 y Y = -2
    [2, -2, 1],
    #Este es el tercer vértice, ubicado en X = 2 y Y = 1
    [2, 1, 1],
    #Este es el cuarto vértice, que forma la parte superior de la figura
    [0, 3, 1]
]

#esta linea lo que hace es un tipo de for que recorre
#todos los elementos de la lista de coordenadas originales
#y los copia en una nueva lista llamada puntos
puntos = [p[:] for p in coordenadas_originales]

def transformar(matriz):
    """Multiplica cada vértice por una matriz de transformación 3x3"""

    #Acá indicamos que vamos a actualizar la variable puntos definida fuera de la función
    global puntos

    #nueva lista para almacenar los nuevos puntos transformados
    nuevos = []

    #Primero vamos a poner lo de la matriz. y su recorrido. 

    #Mostramos un separador para identificar cada transformación en la consola
    print("\n========== TRANSFORMACIÓN ==========")
    #Avisamos que a continuación se mostrará la matriz utilizada
    print("Matriz recibida:")
    #Recorremos una por una las filas de la matriz recibida
    for fila in matriz:
        #Mostramos los tres valores de la fila actual
        print(fila)

    #Luego vamos a recorrer todos los puntos de la lista de puntos
    for i, punto in enumerate(puntos):
        #Mostramos el número y las coordenadas del vértice que vamos a transformar
        print(f"\nProcesando vértice P{i + 1}: {punto}")

        #Por lo que entiendo resultado es una lista que va a almacenar los nuevos valores de cada punto transformado
        resultado = []

        #Ahora vamos a recorrer cada fila de la matriz de transformación
        for fila in range(3):
            #Iniciamos en cero la suma que calculará una componente del nuevo punto
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
                    # Esta línea es para mostrar el resultado de la multiplicación y la suma acumulada
                    f"     {a} × {b} = {producto}"
                    #Y esta otra linea es para mostrar la suma acumulada
                    f" | Acumulado: {suma}"
                )

            #Lo que hace esta parte es agregar el valor de la suma a la lista resultado, que representa el nuevo vértice transformado
            resultado.append(suma)

        #Este print es para mostrar el nuevo vértice transformado
        print(f"  Nuevo vértice: {resultado}")
        #Agregamos el nuevo vértice a la lista de nuevos puntos
        nuevos.append(resultado)

    #esto es para actualizar la lista de puntos con los nuevos puntos transformados
    puntos = nuevos

    #Mostramos un encabezado antes de listar los resultados
    print("\nTodos los vértices transformados:")

    #Este for es para mostrar todos los nuevos vértices transformados
    for i, punto in enumerate(puntos):
        #Este print es para mostrar el nuevo vértice transformado
        print(f"  P{i + 1}: {punto}")

    #Una vez transformados todos los puntos, llamamos a la función dibujar() para actualizar la visualización de la figura
    dibujar()

def trasladar(dx, dy):
    """Traslada la figura en dx y dy."""
    # Definimos la matriz de traslación
    matriz = [
        #Acá sumamos dx a la coordenada X para mover la figura horizontalmente
        [1, 0, dx],
        #Acá sumamos dy a la coordenada Y para mover la figura verticalmente
        [0, 1, dy],
        #y esto es nada más por lo auxiliar de la coordenada homogénea
        [0, 0, 1]
    ]
    #definimos la matriz y la pasamos como parámetro a la función para que la función opere con ella
    transformar(matriz)
def rotar(grados):
    """Rota la figura en un ángulo dado en grados."""
    # Convertimos los grados a radianes
    angulo = math.radians(grados)
    # Calculamos el coseno y el seno del ángulo
    c = math.cos(angulo)
    #Calculamos el seno del ángulo en radianes
    s = math.sin(angulo)

    # Definimos la matriz de rotación
    matriz = [
        #Esta fila calcula la nueva X como c por X menos s por Y
        [c, -s, 0],
        #Esta fila calcula la nueva Y como s por X más c por Y
        [s, c, 0],
        #Esta fila conserva la coordenada homogénea con valor 1
        [0, 0, 1]
    ]
    #definimos la matriz y la pasamos como parámetro a la función para que la función opere con ella
    transformar(matriz)

def escalar(sx, sy):
    """Escala la figura en x y y."""
    # Definimos la matriz de escalado
    matriz = [
        #Multiplicamos X por sx para cambiar el tamaño horizontal
        [sx, 0, 0],
        #Multiplicamos Y por sy para cambiar el tamaño vertical
        [0, sy, 0],
        #Esta fila conserva la coordenada homogénea con valor 1
        [0, 0, 1]
    ]
    #definimos la matriz y la pasamos como parámetro a la función para que la función opere con ella
    transformar(matriz)

def reflejar(eje):
    #Comprobamos si se pidió reflejar la figura respecto al eje X
    if eje == "X":
        # Definimos la matriz de reflexión respecto al eje X
        matriz = [
            #Conservamos la coordenada X al reflejar respecto al eje X
            [1, 0, 0],
            #Cambiamos el signo de Y para pasar al otro lado del eje X
            [0, -1, 0],
            #Esta fila conserva la coordenada homogénea con valor 1
            [0, 0, 1]
        ]
    #Si el eje no es X, usamos la reflexión en Y que ofrece el botón
    else:
        # Definimos la matriz de reflexión respecto al eje Y
        matriz = [
            #Cambiamos el signo de X para pasar al otro lado del eje Y
            [-1, 0, 0],
            #Conservamos la coordenada Y al reflejar respecto al eje Y
            [0, 1, 0],
            #Esta fila conserva la coordenada homogénea con valor 1
            [0, 0, 1]
        ]
    #Pasamos la matriz a transformar para aplicarla a todos los vértices
    transformar(matriz)

def reiniciar():
    """Reinicia la figura a su estado original."""
    #Indicamos que vamos a reemplazar la lista de puntos que está fuera de la función
    global puntos
    # Copiamos los puntos originales a la lista de puntos
    puntos = [p[:] for p in coordenadas_originales]
    # Llamamos a la función dibujar() para actualizar la visualización de la figura
    dibujar()

def a_pantalla(x, y):
    """Convierte coordenadas del plano a coordenadas de pantalla."""
    # En el canvas, Y crece hacia abajo; en el plano, hacia arriba.
    # Por lo tanto, invertimos la coordenada Y y la trasladamos al centro del canvas
    return (ancho / 2 + x * unidad, alto / 2 - y * unidad)

#Definimos la función que vuelve a dibujar el plano y la figura actual
def dibujar():
    #Acá borramos el dibujo anterior para que no se encimen las figuras
    canvas.delete("all")

    # Cuadrícula.
    for x in range(-11, 12):
        #Convertimos X a pixeles y usamos _ para ignorar la Y que no necesitamos
        px, _ = a_pantalla(x, 0)
        #Dibujamos una línea vertical de la cuadrícula con un color claro
        canvas.create_line(px, 0, px, alto, fill="#e2e8f0")

    #Recorremos los valores de Y desde -7 hasta 7 para las líneas horizontales
    for y in range(-7, 8):
        #Convertimos Y a pixeles e ignoramos la X que devuelve la función
        _, py = a_pantalla(0, y)
        #Dibujamos una línea horizontal que ocupa todo el ancho del canvas
        canvas.create_line(0, py, ancho, py, fill="#e2e8f0")

    # Ejes cartesianos.
    canvas.create_line(
        #El eje X va de izquierda a derecha a la mitad de la altura
        0, alto / 2, ancho, alto / 2,
        #Elegimos un color oscuro, grosor de 2 pixeles y una flecha al final
        fill="#334155", width=2, arrow=tk.LAST
    )
    #Acá comenzamos a crear una línea para uno de los ejes cartesianos
    canvas.create_line(
        #El eje Y va desde abajo hacia arriba a la mitad del ancho
        ancho / 2, alto, ancho / 2, 0,
        #Elegimos un color oscuro, grosor de 2 pixeles y una flecha al final
        fill="#334155", width=2, arrow=tk.LAST
    )
    #Escribimos X cerca de la punta del eje horizontal
    canvas.create_text(ancho - 15, alto / 2 + 15, text="X")
    #Escribimos Y cerca de la punta del eje vertical
    canvas.create_text(ancho / 2 + 15, 15, text="Y")

    # Contorno de referencia de la figura original.
    referencia = [
        #Agregamos cada valor de pantalla a la lista: primero X y después Y
        coordenada
        #Recorremos los vértices originales e ignoramos su coordenada homogénea
        for x, y, _ in coordenadas_originales
        #Convertimos cada vértice y recorremos sus dos coordenadas en pixeles
        for coordenada in a_pantalla(x, y)
    ]
    #Acá le pedimos al canvas que dibuje un polígono conectando sus vértices
    canvas.create_polygon(
        #El asterisco separa las coordenadas; dejamos el interior vacío y el borde gris
        *referencia, fill="", outline="#94a3b8",
        #Hacemos el borde discontinuo con 5 pixeles de trazo y 4 de espacio
        dash=(5, 4), width=2
    )

    # Figura transformada.
    figura = [
        #Agregamos cada valor de pantalla a la lista: primero X y después Y
        coordenada
        #Recorremos las coordenadas actuales, que ya pueden estar transformadas
        for x, y, _ in puntos
        #Convertimos cada vértice y recorremos sus dos coordenadas en pixeles
        for coordenada in a_pantalla(x, y)
    ]
    #Acá le pedimos al canvas que dibuje un polígono conectando sus vértices
    canvas.create_polygon(
        #Separamos las coordenadas y dibujamos la figura con relleno azul claro y borde azul
        *figura, fill="#bfdbfe", outline="#2563eb", width=3
    )

    # Vértices y etiquetas.
    for i, (x, y, _) in enumerate(puntos):
        #Convertimos el vértice del plano a su posición en la pantalla
        px, py = a_pantalla(x, y)
        #Creamos un pequeño círculo para señalar dónde está el vértice
        canvas.create_oval(
            #Definimos un cuadro de 8 por 8 pixeles centrado en el vértice
            px - 4, py - 4, px + 4, py + 4,
            #Rellenamos el círculo de rojo y quitamos su borde
            fill="#dc2626", outline=""
        )
        #Acá comenzamos a escribir la etiqueta que identifica al vértice
        canvas.create_text(
            #Colocamos la etiqueta arriba y a la derecha, numerando desde P1
            px + 12, py - 12, text=f"P{i + 1}",
            #Usamos rojo oscuro para que la etiqueta se pueda leer
            fill="#991b1b"
        )

    #Unimos las coordenadas de todos los vértices en un texto separado por barras
    texto = "   |   ".join(
        #Mostramos el nombre del punto y sus coordenadas con dos decimales
        f"P{i + 1}: ({x:.2f}, {y:.2f})"
        for i, (x, y, _) in enumerate(puntos)
    )
    #Actualizamos la etiqueta inferior con las coordenadas actuales
    coordenadas.config(text=texto)


#Acá creamos la ventana principal de la aplicación
ventana = tk.Tk()
#Ponemos el título que aparece en la barra de la ventana
ventana.title("Práctica: transformaciones bidimensionales")

#Creamos una etiqueta para mostrar un texto dentro de la ventana
tk.Label(
    #Indicamos que esta etiqueta pertenece a la ventana principal
    ventana,
    #Definimos el texto del encabezado de la aplicación
    text="Transformaciones 2D mediante matrices",
    #Elegimos la fuente Arial, tamaño 16 y en negritas
    font=("Arial", 16, "bold")
#Terminamos la etiqueta y la colocamos con 10 pixeles de espacio vertical
).pack(pady=10)

#Creamos una etiqueta para mostrar un texto dentro de la ventana
tk.Label(
    #Indicamos que esta etiqueta pertenece a la ventana principal
    ventana,
    #Mostramos una explicación del efecto de los botones de reflexión
    text="Media casa: en Y cambia de lado; en X el techo queda hacia abajo."
#Terminamos la etiqueta y la colocamos dentro de la ventana
).pack()

#Creamos el área donde se van a dibujar la cuadrícula y las figuras
canvas = tk.Canvas(
    #Le asignamos la ventana, las dimensiones definidas antes y un fondo blanco
    ventana, width=ancho, height=alto, bg="white"
)
#Colocamos el canvas dejando 10 pixeles de espacio a su alrededor
canvas.pack(padx=10, pady=10)

#Creamos un contenedor para organizar los botones de las transformaciones
controles = tk.Frame(ventana)
#Colocamos el contenedor de botones debajo del área de dibujo
controles.pack()

#Guardamos parejas de texto y acción; lambda permite ejecutar la acción al pulsar
botones = [
    #Este botón resta una unidad a X para mover la figura hacia la izquierda
    ("← Izquierda", lambda: trasladar(-1, 0)),
    #Este botón suma una unidad a X para mover la figura hacia la derecha
    ("Derecha →", lambda: trasladar(1, 0)),
    #Este botón suma una unidad a Y para mover la figura hacia arriba
    ("↑ Arriba", lambda: trasladar(0, 1)),
    #Este botón resta una unidad a Y para mover la figura hacia abajo
    ("↓ Abajo", lambda: trasladar(0, -1)),
    #Este botón gira 15 grados en sentido antihorario alrededor del origen
    ("Girar +15°", lambda: rotar(15)),
    #Este botón gira 15 grados en sentido horario alrededor del origen
    ("Girar -15°", lambda: rotar(-15)),
    #Multiplicamos X y Y por 1.25 para aumentar la figura respecto al origen
    ("Aumentar ×1.25", lambda: escalar(1.25, 1.25)),
    #Multiplicamos X y Y por 0.8 para reducir la figura respecto al origen
    ("Reducir ×0.8", lambda: escalar(0.8, 0.8)),
    #Al pulsarlo cambiamos el signo de Y para reflejar respecto al eje X
    ("Reflejar en X", lambda: reflejar("X")),
    #Al pulsarlo cambiamos el signo de X para reflejar respecto al eje Y
    ("Reflejar en Y", lambda: reflejar("Y")),
    #Guardamos la función sin paréntesis para llamarla solamente al pulsar el botón
    ("Reiniciar", reiniciar)
]

#Recorremos las parejas de la lista y usamos el índice para organizar los botones
for i, (texto, accion) in enumerate(botones):
    #Acá creamos un botón para la transformación que estamos recorriendo
    tk.Button(
        #Asignamos su contenedor, texto, función al pulsar y ancho en caracteres
        controles, text=texto, command=accion, width=18
    #La división entera elige la fila y el residuo la columna, formando filas de 4 botones
    ).grid(row=i // 4, column=i % 4, padx=4, pady=4)

#Creamos la etiqueta de coordenadas y limitamos su ancho para que el texto pueda saltar de línea
coordenadas = tk.Label(ventana, font=("Arial", 9), wraplength=ancho - 20)
#Colocamos la etiqueta con 12 pixeles de separación vertical
coordenadas.pack(pady=12)

#Dibujamos la figura y actualizamos sus coordenadas en la ventana
dibujar()
#Mantenemos la ventana abierta y escuchamos los clics hasta que el usuario la cierre
ventana.mainloop()
