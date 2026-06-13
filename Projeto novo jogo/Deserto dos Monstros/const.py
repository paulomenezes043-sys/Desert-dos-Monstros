#B ( DIMENSÃO DO CENÁRIO)
import pygame

#B
BG_WIDTH = 576
BG_HEIGHT = 324


#C
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 211, 67)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)
C_BLUE = (0, 0, 255)

#E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED ={
    'LEVEL1BG0':1,
    'LEVEL1BG1':0,
    'LEVEL1BG2':0,
    'LEVEL1BG3':0,
    'LEVEL1BG4':0,
    'LEVEL2BG0':1,
    'LEVEL2BG1':1,
    'LEVEL2BG2':1,
    'LEVEL2BG3':0,
    'LEVEL2BG4':0,
    'Player':2,
    'PlayerShot':3,
    'Enemy1':1,
    'Enemy1Shot':3,
    'Enemy2':1,
    'Enemy2Shot':3,
    'Enemy3':1,
    'Enemy3Shot':3,
    'Enemy4':1,
    'Enemy4Shot':2,
    'Enemy5':1,
    'Enemy5Shot':2
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
    'Player': 3000,
    'PlayerShot': 1,
    'Enemy1': 90,
    'Enemy1Shot': 1,
    'Enemy2': 120,
    'Enemy2Shot': 1,
    'Enemy3': 70,
    'Enemy3Shot': 1,
    'Enemy4':115,
    'Enemy4Shot':1,
    'Enemy5':100,
    'Enemy5Shot':1

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
    'PlayerShot': 30,
    'Enemy1': 1,
    'Enemy1Shot':50,
    'Enemy2': 1,
    'Enemy2Shot':25,
    'Enemy3': 1,
    'Enemy3Shot':75,
    'Enemy4':1,
    'Enemy4Shot':65,
    'Enemy5':1,
    'Enemy5Shot':70
}

ENTITY_SCORE = {
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
    'Player': 0,
    'PlayerShot': 0,
    'Enemy1':100,
    'Enemy1Shot':0,
    'Enemy2':125,
    'Enemy2Shot':0,
    'Enemy3':175,
    'Enemy3Shot':0,
    'Enemy4':200,
    'Enemy4Shot':0,
    'Enemy5':220,
    'Enemy5Shot':0
}

ENTITY_SHOOT_DELAY = {
    'Player': 10,
    'Enemy1': 80,
    'Enemy2': 100,
    'Enemy3': 90,
    'Enemy4': 95,
    'Enemy5': 100,
}


#G
GRAVITY = 1.5
FLOOR_Y = 325




# M
MENU_OPTION = ('NEW GAME', #0
               'MENU',  #1
               'SCORE', #2
               'EXIT') #3



#P
PLAYER_KEY_SHOOT = {'Player': pygame.K_LCTRL,
                    }

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

#S

SPAWN_TIME =3000
SCORE_POS ={'Title': (WIN_WIDTH/2,50),
            'EnterName': (WIN_WIDTH/2,80),
            'Label':(WIN_WIDTH/2,90),
            'Name':(WIN_WIDTH/2,110),
            0:(WIN_WIDTH/2,110),
            1:(WIN_WIDTH/2,130),
            2:(WIN_WIDTH/2,150),
            3:(WIN_WIDTH/2,170),
            4:(WIN_WIDTH/2,190),
            5:(WIN_WIDTH/2,210),
            6:(WIN_WIDTH/2,230),
            7:(WIN_WIDTH/2,250),
            8:(WIN_WIDTH/2,270),
            9:(WIN_WIDTH/2,290),
            }
#T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000 # = 20 SEGUNDOS
