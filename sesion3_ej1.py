import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cuadrado atrapado en ventana")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)

# Posición y velocidad
x, y = 400, 300
velocidad = 2
tamaño = 50

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Verificar colisiones con bordes
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
