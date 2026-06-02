#B ( DIMENSÃO DO CENÁRIO)
import pygame

BG_WIDTH = 576
BG_HEIGHT = 324


#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 211, 67)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (255, 0, 0)


#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED ={
    'LEVEL1BG0':1,
    'LEVEL1BG1':0,
    'LEVEL1BG2':0,
    'LEVEL1BG3':0,
    'LEVEL1BG4':0,
    'LEVEL1BG5':0,
    'Player':2,
    'Enemy1':1,
}



# M
MENU_OPTION = ('NEW GAME', #0
               'MENU',  #1
               'SCORE', #2
               'EXIT') #3

#S

SPAWN_TIME =4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324