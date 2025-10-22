import pygame
pygame.init()

# Crear ventana
ancho, alto = 800, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Círculos concéntricos")

# Definir colores (R, G, B)
colores = [
    (255, 0, 0),     # Rojo
    (0, 255, 0),     # Verde
    (0, 0, 255),     # Azul
    (255, 255, 0),   # Amarillo
    (255, 0, 255)    # Morado
]

# Coordenadas del centro
centro = (ancho // 2, alto // 2)

# Lista de radios
radios = [20, 40, 60, 80, 100]

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    ventana.fill((255, 255, 255))

    # Dibujar círculos concéntricos
    for i in range(5):
        pygame.draw.circle(ventana, colores[i], centro, radios[i], 3)  # grosor de 3 píxeles


    pygame.display.flip()

pygame.quit()