import pygame

pygame.init()


ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer Programa Gráfico")

# Colores
azul = (0, 0, 255)
blanco = (255, 255, 255)

# Color inicial
color_actual = azul


corriendo = True
while corriendo:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            corriendo = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            # Cambiar a blanco con C
            elif evento.key == pygame.K_c:
                if color_actual == azul:
                    color_actual = blanco
                else:
                    color_actual = azul  # permite alternar entre azul y blanco

    # Rellenar la ventana con el color actual
    ventana.fill(color_actual)
    pygame.display.update()

pygame.quit()

