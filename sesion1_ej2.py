import pygame

pygame.init()


ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Mi primer Programa Gráfico")


azul = (0, 0, 255)

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        
        if evento.type == pygame.QUIT:
            corriendo = False
        # Detecta si se presiona una tecla
        if evento.type == pygame.KEYDOWN:
            # Si la tecla es ESC , se cierra el programa
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    ventana.fill(azul)
    pygame.display.update()
pygame.quit()

