import pygame
import pygame_textinput

from app.domain.players.player import Player

def draw_start_screen(screen,width,height,font,color):
    inicio = "Bienvenido/a a Mini Monopoly"
    enter = "Presione SPACE para empezar a jugar"
    
    # Configura la fuente
    inicio_surface = font.render(inicio, True, color)
    enter_surface = font.render(enter,True,color)
    
    # Configura la posición
    inicio_rect = inicio_surface.get_rect(center=(width/2, height/2-40))
    enter_rect = enter_surface.get_rect(center=(width/2, height/2+40))
    
    # Dibuja los mensajes en pantalla
    screen.blit(inicio_surface, inicio_rect)
    screen.blit(enter_surface, enter_rect)

def start_game(screen,width,height,font,color):
    jugador1 = "Introduce nombre del primer jugador"
    jugador2 = "Introduce nombre del segundo jugador"
    
    # Input de texto
    text_input = pygame_textinput.TextInputVisualizer()
    
    # Configura la fuente
    jug1_surface = font.render(jugador1, True, color)
    
    # Configura la posición
    jug1_rect = jug1_surface.get_rect(center=(width/2, height/2-40))
    
    # Dibuja los mensajes en pantalla
    screen.blit(jug1_surface, jug1_rect)
    events = pygame.event.get()

    # Feed it with events every frame
    text_input.update(events)
    # Blit its surface onto the screen
    screen.blit(text_input.surface, (10, 10))
    
    # Crear jugadores
    #jugador1 = Player(nombre1, "./../../static/images/players/auto.png",750,[],0,False)
    #jugador2 = Player(nombre2, "./../../static/images/players/bote.png",750,[],0,False)
    
    # Crear propiedades
    
    # Crear cartas
    