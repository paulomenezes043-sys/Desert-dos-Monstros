#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):

        while True:
          # score = Score(self.window)
         #  menu = Menu(self.window)
             menu = Menu(self.window)
             menu_return = menu.run()

             if menu_return == MENU_OPTION[0]:
                 player_score = [0]
                 level = Level(self.window, 'LEVEL1', menu_return, player_score)
                 level_return = level.run(player_score)
                 if level_return:
                   level = Level(self.window, 'LEVEL2', menu_return,player_score)
                   level_return = level.run(player_score)



             elif menu_return == MENU_OPTION[3]: #exit
               pygame.quit()  # Close window
               quit()  # end pygame
             else:
                 pass
            #   pygame.quit()
            #   sys.exit()

