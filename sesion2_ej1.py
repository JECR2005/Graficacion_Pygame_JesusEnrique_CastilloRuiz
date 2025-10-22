import pygame

pygame.init()

# Configuración
ANCHO_VENTANA = 800
ALTO_VENTANA = 800
FILAS = 8
COLUMNAS = 8

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Calcula tamaño de cada casilla (para que ocupe toda la ventana)
TAM_CASILLA = min(ANCHO_VENTANA // COLUMNAS, ALTO_VENTANA // FILAS)

ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Tablero de Ajedrez 8x8")

reloj = pygame.time.Clock()

def dibujar_tablero(superficie):
    for fila in range(FILAS):
        for col in range(COLUMNAS):
            # alternar color según la suma de índices
            if (fila + col) % 2 == 0:
                color = BLANCO
            else:
                color = NEGRO
            rect = pygame.Rect(col * TAM_CASILLA, fila * TAM_CASILLA, TAM_CASILLA, TAM_CASILLA)
            pygame.draw.rect(superficie, color, rect)

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False

    dibujar_tablero(ventana)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()

