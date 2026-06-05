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
    'Player':1,
    'PlayerShot':3,
    'Enemy1':1,
    'Enemy1Shot':3,
    'Enemy2':1,
    'Enemy2Shot':3
}

ENTITY_HEALTH = {
    'LEVEL1BG0':999,
    'LEVEL1BG1':999,
    'LEVEL1BG2':999,
    'LEVEL1BG3':999,
    'LEVEL1BG4':999,
    'LEVEL2BG0':999,
    'LEVEL2BG1':999,
    'LEVEL2BG2':999,
    'LEVEL2BG3':999,
    'LEVEL2BG4':999,
    'Player': 300,
    'PlayerShot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,

}

ENTITY_DAMAGE = {
    'LEVEL1BG0':0,
    'LEVEL1BG1':0,
    'LEVEL1BG2':0,
    'LEVEL1BG3':0,
    'LEVEL1BG4':0,
    'LEVEL2BG0':0,
    'LEVEL2BG1':0,
    'LEVEL2BG2':0,
    'LEVEL2BG3':0,
    'LEVEL2BG4':0,
    'Player': 1,
    'PlayerShot': 25,
    'Enemy1': 1,
    'Enemy1Shot':20,
    'Enemy2': 1,
    'Enemy2Shot':15
}

ENTITY_SCORE = {

    'Player': 0,
    'PlayerShot': 0,
    'Enemy1':100,
    'Enemy1Shot':0,
    'Enemy2':125,
    'Enemy2Shot':0,
}

ENTITY_SHOOT_DELAY = {
    'Player': 10,
    'Enemy1': 80,
    'Enemy2': 100,
}

# M
MENU_OPTION = ('NEW GAME', #0
               'MENU',  #1
               'SCORE', #2
               'EXIT') #3



#P
PLAYER_KEY_SHOOT = {'Player': pygame.K_LCTRL,
                    }


#S

SPAWN_TIME =4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324