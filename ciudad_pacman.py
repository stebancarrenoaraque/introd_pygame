# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

# Librerias
import pygame
import sys
import math

# inicializamos los modulos de la librería

pygame.init()

# Establecer dimensiones de la ventana

ventana = pygame.display.set_mode((1080,620))

# establecer titulo de la ventana

pygame.display.set_caption("Pac-city")

# Definicion de colores

negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = (255,255,255)
cian = (0,255,255)
morado = (128,0,128)
gris = (100,100,100)
dorado = (255,215,0)
marron = (165,42,42)
gris_oscuro = (25,25,25)

# variables auxiliares

PI = math.pi

# Objeto para la gestión del tiempo

clock = pygame.time.Clock()

# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    # ------------------------------
    # Dibujar formas con modulo draw
    # ------------------------------

    # Fondo
    pygame.draw.rect(ventana, gris_oscuro, (0,450,1080,620))
    # Edificios
    pygame.draw.rect(ventana, gris, (200,200,100,250))
    pygame.draw.rect(ventana, gris, (325,250,100,200))
    # Ventanas
    pygame.draw.rect(ventana, amarillo, (215,215,30,20))
    pygame.draw.rect(ventana, amarillo, (215,250,30,20))
    pygame.draw.rect(ventana, amarillo, (215,285,30,20))
    pygame.draw.rect(ventana, amarillo, (215,320,30,20))
    pygame.draw.rect(ventana, amarillo, (215,355,30,20))
    pygame.draw.rect(ventana, amarillo, (215,390,30,20))

    pygame.draw.rect(ventana, amarillo, (215,215,30,20))
    pygame.draw.rect(ventana, amarillo, (215,250,30,20))
    pygame.draw.rect(ventana, amarillo, (215,285,30,20))
    pygame.draw.rect(ventana, amarillo, (215,320,30,20))
    pygame.draw.rect(ventana, amarillo, (215,355,30,20))
    pygame.draw.rect(ventana, amarillo, (215,390,30,20))

    # actualizar visualización de la ventana
    pygame.display.flip()