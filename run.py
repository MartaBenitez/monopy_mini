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

# Nuevo estado para controlar si el juego está en curso
game_running = False

# Bucle que mantiene el programa corriendo hasta que se decide cerrar
running = True
while running:
    clock.tick(5) 

    # Eventos
    for event in pygame.event.get():
        # Cierra la ventana
        if event.type == pygame.QUIT:
            running = False
        # Eventos al pulsar teclas
        elif event.type == pygame.KEYDOWN:
            # Iniciar el juego al pulsar space
            if event.key == pygame.K_SPACE:
                 if not game_running:
                    # Cambia el estado del juego
                    game_running = True
    
     # Lógica de juego
    if game_running:
        # Pantalla en negro
        screen.fill((0,0,0))
        # Inicia el juego
        start_game(screen, width, height, font, white)
        # Actualiza
        pygame.display.update()
    else:
        # Pantalla de inicio del juego
        draw_start_screen(screen, width, height, font, white)
        # Actualiza
        pygame.display.update()


    