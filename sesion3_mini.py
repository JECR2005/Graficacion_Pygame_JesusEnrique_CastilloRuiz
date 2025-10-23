import pygame

pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rectángulo con rastro")

# Colores
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)
gris = (120, 120, 255)

# Posición y velocidad
x, y = 400, 300
velocidad = 1   
tamaño = 50

# Lista para guardar los puntos del rastro
rastro = []

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento con teclas
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

    # Agregar la posición actual del centro al rastro
    centro_rect = (x + tamaño // 2, y + tamaño // 2)
    rastro.append(centro_rect)

    # Limitar la cantidad de puntos del rastro
    if len(rastro) > 200:
        rastro.pop(0)

    # Dibujar
    ventana.fill(blanco)

    # Dibujar los pequeños puntos del rastro
    for pos in rastro:
        pygame.draw.circle(ventana, gris, pos, 4)  #  Tamaño del punto reducido

    # Dibujar el rectángulo
    pygame.draw.rect(ventana, color_cuadrado, (x, y, tamaño, tamaño))

    pygame.display.flip()

pygame.quit()
