import pygame


pygame.init()


ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer Programa Gráfico")


azul = (0, 0, 255)


corriendo = True

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Contador de frames
contador_frames = 0

while corriendo:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            corriendo = False

        # Cierra con la tecla ESC
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False

    ventana.fill(azul)


    pygame.display.update()

    # Controla la velocidad de fotogramas
    reloj.tick(60)

    # Incrementa el contador de frames
    contador_frames += 1
    print(contador_frames)
    # Si llega a 300 frames , se detiene
    if contador_frames >= 300:
        corriendo = False


pygame.quit()

