import pygame

pygame.init()
ANCHO, ALTO = 1000, 800
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Casa")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VIDRIO = (180, 220, 255)  # color de las ventanas
PUERTA_COLOR = (100, 60, 40)

# Colores disponibles para el cuerpo de la casa
COLORES = {
    pygame.K_r: (200, 30, 30),   # R -> rojo
    pygame.K_b: (30, 80, 200),   # B -> azul
    pygame.K_g: (30, 160, 40),   # G -> verde
    pygame.K_y: (230, 210, 50),  # Y -> amarillo
    pygame.K_w: (240, 240, 240)  # W -> blanco / claro
}

# Color inicial de la casa
color_casa = COLORES[pygame.K_b]

reloj = pygame.time.Clock()
corriendo = True

# Posiciones y tamaños de la casa (centrada horizontalmente)
body_w, body_h = 300, 250
body_x = (ANCHO - body_w) // 2
body_y = 380  # altura desde arriba donde empieza el cuerpo

# Tejado: triángulo encima del cuerpo
roof_height = 140
roof_points = [
    (body_x, body_y),                    # esquina izquierda del cuerpo
    (body_x + body_w, body_y),           # esquina derecha del cuerpo
    (body_x + body_w // 2, body_y - roof_height)  # pico del tejado
]

# Puerta
door_w, door_h = 70, 120
door_x = body_x + (body_w - door_w) // 2
door_y = body_y + body_h - door_h

# Ventanas (círculos)
window_radius = 30
window1_center = (body_x + 80, body_y + 90)
window2_center = (body_x + body_w - 80, body_y + 90)

# Fuente para las instrucciones
fuente = pygame.font.SysFont(None, 22)

def dibujar_instrucciones(surf):
    lines = [
        "Presiona R = Rojo | B = Azul | G = Verde | Y = Amarillo | W = Claro",
        "ESC = Salir",
    ]
    x, y = 10, 10
    for line in lines:
        txt = fuente.render(line, True, NEGRO)
        surf.blit(txt, (x, y))
        y += 24

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
            elif evento.key in COLORES:
                color_casa = COLORES[evento.key]

    ventana.fill(BLANCO)

    # Dibuja césped (solo para estética)
    pygame.draw.rect(ventana, (150, 220, 150), (0, body_y + body_h, ANCHO, ALTO - (body_y + body_h)))

    # Dibuja el cuerpo de la casa
    cuerpo_rect = pygame.Rect(body_x, body_y, body_w, body_h)
    pygame.draw.rect(ventana, color_casa, cuerpo_rect)
    pygame.draw.rect(ventana, NEGRO, cuerpo_rect, 3)  # borde

    # Dibuja el tejado (un triángulo)
    # Hago el color del tejado ligeramente más oscuro que el cuerpo
    roof_shade = tuple(max(0, c - 40) for c in color_casa)
    pygame.draw.polygon(ventana, roof_shade, roof_points)
    pygame.draw.polygon(ventana, NEGRO, roof_points, 3)

    # Dibuja las ventanas (círculos)
    pygame.draw.circle(ventana, VIDRIO, window1_center, window_radius)
    pygame.draw.circle(ventana, NEGRO, window1_center, window_radius, 2)
    pygame.draw.circle(ventana, VIDRIO, window2_center, window_radius)
    pygame.draw.circle(ventana, NEGRO, window2_center, window_radius, 2)

    # Dibuja la puerta
    puerta_rect = pygame.Rect(door_x, door_y, door_w, door_h)
    pygame.draw.rect(ventana, PUERTA_COLOR, puerta_rect)
    pygame.draw.rect(ventana, NEGRO, puerta_rect, 2)
    # Aldaba/Manija
    pygame.draw.circle(ventana, (220, 200, 0), (door_x + door_w - 15, door_y + door_h // 2), 6)

    # Dibujar instrucciones
    dibujar_instrucciones(ventana)

    pygame.display.update()
    reloj.tick(60)  # 60 FPS

pygame.quit()

