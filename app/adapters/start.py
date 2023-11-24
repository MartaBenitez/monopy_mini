import pygame
from app.domain.players.player import Player

def draw_start_screen(screen,width,height,font,color):
    inicio = "Bienvenido/a a Mini Monopoly"
    enter = "Presione ENTER para empezar a jugar"
    
    # Configura la fuente
    inicio_surface = font.render(inicio, True, color)
    enter_surface = font.render(enter,True,color)
    
    # Configura la posición
    inicio_rect = inicio_surface.get_rect(center=(width/2, height/2-40))
    enter_rect = enter_surface.get_rect(center=(width/2, height/2+40))
    
    # Dibuja los mensajes en pantalla
    screen.blit(inicio_surface, inicio_rect)
    screen.blit(enter_surface, enter_rect)

def start_game():
    print("Introduzca el nombre del primer jugador")
    #nombre1 = input()
    #print("Introduzca el nombre del segundo jugador")
    #nombre2 = input()
    # Crear jugadores
    #jugador1 = Player(nombre1, "./../../static/images/players/auto.png",750,[],0,False)
    #jugador2 = Player(nombre2, "./../../static/images/players/bote.png",750,[],0,False)
    
    # Crear propiedades
    
    # Crear cartas
    