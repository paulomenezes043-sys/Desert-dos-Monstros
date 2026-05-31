#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from const import C_ORANGE, WIN_WIDTH, MENU_OPTION, C_RED, C_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/Menu.wav')
        pygame.mixer.music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50,"Deserto", C_ORANGE, ((WIN_WIDTH / 2), 40))
            self.menu_text(50, "Dos", C_ORANGE, ((WIN_WIDTH / 2), 80))
            self.menu_text(50, "Monstros", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_RED, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                   self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
