#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from const import C_ORANGE, WIN_WIDTH, MENU_OPTION, C_RED, C_WHITE, C_BLUE, C_GREEN, C_BLACK, BG_HEIGHT, BG_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menu.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_WIDTH))
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer.music.load('./asset/menu.wav')
        pygame.mixer.music.play(-1)
        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(45, "DESERT MONSTERS", C_RED, ((WIN_WIDTH / 2), 80))
            #self.menu_text(50, "MONSTERS", C_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], C_BLUE, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]

    def show_controls(self):
        pygame.event.clear()

        while True:
            self.window.blit(self.surf, self.rect)

            # Título principal
            self.menu_text(50, "CONTROLES", C_ORANGE, (WIN_WIDTH / 2, 40))

            # --- COLUNA 1: AS TECLAS (Em Branco ou Amarelo para destacar) ---
            self.menu_text(24, "   ARROW RIGHT   :", C_WHITE, (WIN_WIDTH / 2 - 120, 140))
            self.menu_text(24, "   ARROW LEFT    :", C_WHITE, (WIN_WIDTH / 2 - 120, 180))
            self.menu_text(24, "    ARROW UP     :", C_WHITE, (WIN_WIDTH / 2 - 120, 220))
            self.menu_text(24, "      CTRL       :", C_WHITE, (WIN_WIDTH / 2 - 120, 260))

            # --- COLUNA 2: AS AÇÕES (Em Azul ou outra cor para contrastar) ---
            self.menu_text(24, "  MOVE RIGHT", C_BLUE, (WIN_WIDTH / 2 + 100, 140))
            self.menu_text(24, "  MOVE LEFT", C_BLUE, (WIN_WIDTH / 2 + 100, 180))
            self.menu_text(24, "  JUMP", C_BLUE, (WIN_WIDTH / 2 + 100, 220))
            self.menu_text(24, "  SHOOT", C_BLUE, (WIN_WIDTH / 2 + 100, 260))

            # Linha de instrução para voltar
            self.menu_text(20, "PRESS ESC TO RETURN", C_RED, (WIN_WIDTH / 2, 300))

            pygame.display.flip()

            for event in pygame.event.get():
                # Se clicar no X da janela, aí sim fecha o jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Se apertar ESC ou BACKSPACE (tecla de apagar texto), apenas RETORNA para o menu
                    if event.key in (pygame.K_ESCAPE, pygame.K_BACKSPACE):
                        return  # Sai da tela de controles e o menu principal continua rodando

    def show_game_over(self):
        pygame.event.clear()
        go_option = 0  # 0 = RESTART, 1 = MENU
        OPTIONS = ["RESTART", "MENU PRINCIPAL"]
        pygame.mixer.music.load('./asset/GameOver.wav')
        pygame.mixer.music.play(-5)
        img_game_over = pygame.image.load('./asset/game_over_bg.png')
        img_game_over = pygame.transform.scale(img_game_over,(BG_WIDTH, BG_HEIGHT))
        while True:
            self.window.blit(img_game_over, (0,0))
            # Título chamativo
            self.menu_text(60, "GAME OVER", C_RED, (WIN_WIDTH / 2, 120))

            # Desenha as duas opções
            for i in range(len(OPTIONS)):
                # Se for a opção atual, desenha em VERMELHO, se não, em BRANCO
                cor = C_RED if i == go_option else C_WHITE
                self.menu_text(24, OPTIONS[i], cor, (WIN_WIDTH / 2, 260 + (i * 40)))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if go_option < len(OPTIONS) - 1:
                            go_option += 1

                    elif event.key == pygame.K_UP:
                        if go_option > 0:
                            go_option -= 1

                    elif event.key == pygame.K_RETURN:
                        # Retorna 'RESTART' ou 'MENU' dependendo do que ele escolheu
                        if go_option == 0:
                            return "RESTART"
                        else:
                            return "MENU"

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
