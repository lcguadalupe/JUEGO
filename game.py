import pygame
import random
import math
import sys 
import os

#inicializar pygame
pygame.init()

#establece el tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
    
#cargar imagen de fondo 
asset_background = resource_path('assets/images/background.png')
background = pygame.image.load(asset_background)

#cargar icono de ventana
asset_icon = resource_path('assets/images/ufo.png')
icon = pygame.image.load(asset_icon)

#cargar sonido de fondo
asset_sound = resource_path('assets/audio/background_music.mp3')
background_sound = pygame.mixer.music.load(asset_sound)

#cargar imagen del jugador
asset_playerimg = resource_path('assets/images/space-invaders.png')
playerimg = pygame.image.load(asset_playerimg)

#cargar imagen de la bala
asset_bulletimg = resource_path('assets/images/bullet.png')
bulletimg = pygame.image.load(asset_bulletimg)

#cargar fuente para texto de game over
asset_over_font = resource_path('assets/fonts/RAVIE.TTF')
over_font = pygame.font.Font(asset_over_font)

#cargar fuente para texto de puntuaje
asset_font = resource_path('assets/fonts/comicbd.ttf')
font = pygame.font.Font(asset_font)

#establecer titulo de ventana
pygame.display.set_caption("Space's Pochu_$")

#establecer icono de ventana 
pygame.display.set_icon(icon)

#reproducir sonido de fondo en loop
pygame.mixer.music.play(-1)

#crear reloj para controlar velocidad del juego
clock = pygame.time.Clock()

#posicion inicial del jugador 
playerX = 370
playerY = 470
player_change = 0
player_change = 0


#lista para almacenar pocisiones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 10

#se inicializan las variables para guadar las pocisiones de los enemigos 
for i in range(no_of_enemies):
    #se carga la imagen del enemigo1
    enemy1 = resource_path('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy1))

    #se carga la imagen del enemigo2
    enemy2 = resource_path('assets/images/enemy1.png')
    enemyimg.append(pygame.image.load(enemy2))

    #se asigna una posicion aleatoria en X y Y para el enemigo
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(0,150))

    #se establece la velocidad de movimiento del enemigo en X e Y
    
