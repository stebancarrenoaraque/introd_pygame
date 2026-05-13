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
gris_claro = (150,150,150)

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
    pygame.draw.rect(ventana,cian,(0,0,1080,620))
    pygame.draw.rect(ventana, verde, (0,450,1080,620))





    # Edificios
    pygame.draw.rect(ventana, gris, (200,200,110,250))
    pygame.draw.rect(ventana, gris, (325,250,110,200))



    # Ventanas
    pygame.draw.rect(ventana, amarillo, (225,215,30,20))
    pygame.draw.rect(ventana, amarillo, (225,250,30,20))
    pygame.draw.rect(ventana, amarillo, (225,285,30,20))
    pygame.draw.rect(ventana, amarillo, (225,320,30,20))
    pygame.draw.rect(ventana, amarillo, (225,355,30,20))
    pygame.draw.rect(ventana, amarillo, (225,390,30,20))
    pygame.draw.rect(ventana, amarillo, (270,215,30,20))
    pygame.draw.rect(ventana, amarillo, (270,250,30,20))
    pygame.draw.rect(ventana, amarillo, (270,285,30,20))
    pygame.draw.rect(ventana, amarillo, (270,320,30,20))
    pygame.draw.rect(ventana, amarillo, (270,355,30,20))
    pygame.draw.rect(ventana, amarillo, (270,390,30,20))

    pygame.draw.rect(ventana, amarillo, (350,265,30,20))
    pygame.draw.rect(ventana, amarillo, (350,300,30,20))
    pygame.draw.rect(ventana, amarillo, (350,335,30,20))
    pygame.draw.rect(ventana, amarillo, (350,370,30,20))
    pygame.draw.rect(ventana, amarillo, (395,265,30,20))
    pygame.draw.rect(ventana, amarillo, (395,300,30,20))
    pygame.draw.rect(ventana, amarillo, (395,335,30,20))
    pygame.draw.rect(ventana, amarillo, (395,370,30,20))


    pygame.draw.rect(ventana, negro, (240,420,45,30))
    pygame.draw.rect(ventana, negro, (365,420,45,30))

    # Rueda 
    pygame.draw.circle(ventana, gris, (700,350), 80,7)
    pygame.draw.line(ventana, gris, (700,350), (780,350),3)
    pygame.draw.line(ventana, gris, (700,350), (755,405),3)
    pygame.draw.line(ventana, gris, (700,350), (700,420),3)
    pygame.draw.line(ventana, gris, (700,350), (645,405),3)
    pygame.draw.line(ventana, gris, (700,350), (620,350),3)
    pygame.draw.line(ventana, gris, (700,350), (645,295),3)
    pygame.draw.line(ventana, gris, (700,350), (755,295),3)
    pygame.draw.line(ventana, gris, (700,350), (700,270),3)
    pygame.draw.rect(ventana, marron, (770,350,25,15))
    pygame.draw.rect(ventana, marron, (745,405,25,15))
    pygame.draw.rect(ventana, marron, (690,420,25,15))
    pygame.draw.rect(ventana, marron, (640,405,25,15))
    pygame.draw.rect(ventana, marron, (610,350,25,15))
    pygame.draw.rect(ventana, marron, (635,295,25,15))
    pygame.draw.rect(ventana, marron, (745,295,25,15))
    pygame.draw.rect(ventana, marron, (690,270,25,15))


    patas = [(670,450),(700,350), (730,450)]
    pygame.draw.lines(ventana, blanco, False, patas,3)

    # Camino
    pygame.draw.rect(ventana, gris_claro, (0, 475, 1080, 50))

    # Circos
    pygame.draw.rect(ventana, rojo, (200,560,120,80))
    pygame.draw.polygon(ventana,blanco,[(200,560),(260,500),(320,560)])
    pygame.draw.rect(ventana, negro, (235,590,50,30))

    pygame.draw.rect(ventana, rojo, (400,560,120,80))
    pygame.draw.polygon(ventana,blanco,[(400,560),(460,500),(520,560)])
    pygame.draw.rect(ventana, negro, (435,590,50,30))

    pygame.draw.rect(ventana, rojo, (400,560,120,80))
    pygame.draw.polygon(ventana,blanco,[(400,560),(460,500),(520,560)])
    pygame.draw.rect(ventana, negro, (435,590,50,30))

    # Pacmans

    pygame.draw.arc(ventana, amarillo, (200,460,50,50), PI/4, 7*PI/4, 100)
    pygame.draw.circle(ventana, negro, (220,470),5,0)

    pygame.draw.arc(ventana, cian, (400,460,50,50), PI/4, 7*PI/4, 100)
    pygame.draw.circle(ventana, negro, (420,470),5,0)

    pygame.draw.arc(ventana, naranja, (600,460,50,50), PI/4, 7*PI/4, 100)
    pygame.draw.circle(ventana, negro, (620,470),5,0)

    # Nubes
    pygame.draw.ellipse(ventana, blanco, (50,45,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (100,25,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (150,35,95,60,),0)

    pygame.draw.ellipse(ventana, blanco, (350,60,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (400,45,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (450,50,95,60,),0)

    pygame.draw.ellipse(ventana, blanco, (650,65,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (700,60,95,60,),0)
    pygame.draw.ellipse(ventana, blanco, (750,75,95,60,),0)

    # sol
    pygame.draw.circle(ventana, dorado, (1080,0),100,0)

    # actualizar visualización de la ventana
    pygame.display.flip()