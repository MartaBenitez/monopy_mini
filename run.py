import pygame
import sys
from app.adapters.start import start_game, draw_start_screen

# Inicializa Pygame
pygame.init()

# Configura la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Configura el título y el icono
pygame.display.set_caption("Mini Monopoly")
icon = pygame.image.load("./static/images/icon.png")
pygame.display.set_icon(icon)

# Cargar una fuente por defecto
font=pygame.font.Font(pygame.font.get_default_font(), 36)
white = (255, 255, 255)

# Establecer la velocidad del bucle
clock = pygame.time.Clock()

# Bucle que mantiene el programa corriendo hasta que se decide cerrar
running = True
while running:

    clock.tick(5) 
    # Configura el color de fondo de la ventana. RGB
    # Las imágenes se apilan a medida que se lee el código por lo que el fondo va el primero
    screen.fill((0,0,0))
    
    # Pantalla de inicio del juego
    crear_pantalla_inicio(screen,width,height,font,white)
    pygame.display.update()

    # Eventos
    for event in pygame.event.get():
        # Cierra la ventana
        if event.type == pygame.QUIT:
            running = False
        # Eventos al pulsar teclas
        elif event.type == pygame.KEYDOWN:
            # Iniciar el juego al pulsar enter
            if event.key == pygame.K_BACKSPACE:
                # Inicia el juego
                iniciar_juego()
            


    