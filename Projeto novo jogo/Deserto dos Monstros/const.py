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
    'LEVEL3BG0':1,
    'LEVEL3BG1':0,
    'LEVEL3BG2':0,
    'LEVEL3BG3':0,
    'LEVEL3BG4':0,
    'LEVEL4BG0':1,
    'LEVEL4BG1':1,
    'LEVEL4BG2':0,
    'LEVEL4BG3':0,
    'LEVEL4BG4':0,
    'Player':2,
    'PlayerShot':3,
    'Enemy1':1,
    'Enemy1Shot':3,
    'Enemy2':1,
    'Enemy2Shot':3,
    'Enemy3':2,
    'Enemy3Shot':3,
    'Enemy4':1,
    'Enemy4Shot':3,
    'Enemy5':2,
    'Enemy5Shot':3
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
    'LEVEL3BG0':999,
    'LEVEL3BG1':999,
    'LEVEL3BG2':999,
    'LEVEL3BG3':999,
    'LEVEL3BG4':999,
    'LEVEL4BG0':999,
    'LEVEL4BG1':999,
    'LEVEL4BG2':999,
    'LEVEL4BG3':999,
    'LEVEL4BG4':999,
    'Player': 1200,
    'PlayerShot': 1,
    'Enemy1': 190,
    'Enemy1Shot': 1,
    'Enemy2': 210,
    'Enemy2Shot': 1,
    'Enemy3': 220,
    'Enemy3Shot': 1,
    'Enemy4':235,
    'Enemy4Shot':1,
    'Enemy5':225,
    'Enemy5Shot':2

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
    'LEVEL3BG0':0,
    'LEVEL3BG1':0,
    'LEVEL3BG2':0,
    'LEVEL3BG3':0,
    'LEVEL3BG4':0,
    'LEVEL4BG0':0,
    'LEVEL4BG1':0,
    'LEVEL4BG2':0,
    'LEVEL4BG3':0,
    'LEVEL4BG4':0,
    'Player': 1,
    'PlayerShot': 45,
    'Enemy1': 1,
    'Enemy1Shot':35,
    'Enemy2': 1,
    'Enemy2Shot':40,
    'Enemy3': 1,
    'Enemy3Shot':55,
    'Enemy4':1,
    'Enemy4Shot':60,
    'Enemy5':1,
    'Enemy5Shot':55
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
    'LEVEL3BG0':0,
    'LEVEL3BG1':0,
    'LEVEL3BG2':0,
    'LEVEL3BG3':0,
    'LEVEL3BG4':0,
    'LEVEL4BG0':0,
    'LEVEL4BG1':0,
    'LEVEL4BG2':0,
    'LEVEL4BG3':0,
    'LEVEL4BG4':0,
    'Player': 0,
    'PlayerShot': 0,
    'Enemy1':80,
    'Enemy1Shot':0,
    'Enemy2':100,
    'Enemy2Shot':0,
    'Enemy3':140,
    'Enemy3Shot':0,
    'Enemy4':170,
    'Enemy4Shot':0,
    'Enemy5':190,
    'Enemy5Shot':0
}

ENTITY_SHOOT_DELAY = {
    'Player': 20,
    'Enemy1': 80,
    'Enemy2': 100,
    'Enemy3': 100,
    'Enemy4': 100,
    'Enemy5': 100,
}


#G
GRAVITY = 1.4
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

SPAWN_TIME =2800
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
TIMEOUT_LEVEL = 50000 # = 50 SEGUNDOS
