import pygame
import math

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectángulo en trayectoria circular")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Parámetros del movimiento circular
centro_x, centro_y = 400, 300
radio = 200
angulo = 0
velocidad_angular = 0.001  # velocidad de rotación

# Tamaño del rectángulo
tamaño = 50

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Calcular nueva posición con funciones trigonométricas
    x = centro_x + radio * math.cos(angulo)
    y = centro_y + radio * math.sin(angulo)
    angulo += velocidad_angular  # Incrementar ángulo

    # Verificar si toca los bordes
    tocando_borde = False
    if x <= 0:
        x = 0
        tocando_borde = True
    elif x + tamaño >= 800:
        x = 800 - tamaño
        tocando_borde = True

    if y <= 0:
        y = 0
        tocando_borde = True
    elif y + tamaño >= 600:
        y = 600 - tamaño
        tocando_borde = True

    # Cambiar color según si toca borde
    color_cuadrado = rojo if tocando_borde else azul

    # Dibujar
    ventana.fill(blanco)
    pygame.draw.rect(ventana, color_cuadrado, (x, y, tamaño, tamaño))
    pygame.display.flip()

pygame.quit()

