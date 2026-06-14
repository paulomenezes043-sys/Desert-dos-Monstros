import sys
from datetime import datetime

import pygame
from pygame import surface, Surface, Rect, KEYDOWN
from pygame.constants import K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from DBProxy import DBProxy
from const import WIN_WIDTH, C_BLUE, SCORE_POS, MENU_OPTION, C_WHITE, C_YELLOW, WIN_HEIGHT, C_RED


class Score:

    def __init__(self, window: surface):
        self.window = window
        self.surf = pygame.image.load('./asset/Score.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_WIDTH))
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save(self, game_mode: str, menu_return: str, player_score: list[int]):
        pygame.mixer.music.load('./asset/Score.wav')
        pygame.mixer.music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ""
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'Thanks for Playing!!', C_BLUE, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Save your name! (5characters):'
            self.score_text(20, text, C_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 5:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                        pass
                    else:
                        if len(name) < 5:
                            name += event.unicode
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer.music.load('./asset/Score.wav')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME   SCORE          DATE       ', C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}  {score:06}   {date}', C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def show_game_over(self):
        # Garante que cliques antigos não interfiram na tela de Game Over
        pygame.event.clear()

        while True:
            # 1. Limpa a tela desenhando o fundo do deserto (ou uma tela preta se preferir)
            self.window.blit(self.surf, self.rect)

            # 2. Desenha o texto de derrota de forma imponente
            self.menu_text(60, "GAME OVER", C_RED, (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 50))

            # Instrução em inglês para o jogador saber como voltar
            self.menu_text(20, "Press ESC to Return to Menu", C_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 50))

            pygame.display.flip()

            # 3. Escuta os comandos do jogador
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    # Se apertar ESC, sai do Game Over e volta pro menu principal
                    if event.key == pygame.K_ESCAPE:
                        return

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H:%M')
    current_date = current_datetime.strftime('%d/%m/%Y')
    return f'{current_time} - {current_date}'
