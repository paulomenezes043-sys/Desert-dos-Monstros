#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Score import Score
from const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from level import Level
from menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player_score = [0]
                while True:
                    player_score = [0]  # Reseta o score sempre que o loop recomeçar (Morte com Restart)

                    # ================= FASE 1 =================
                    level = Level(self.window, 'LEVEL1', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return == "RESTART":
                        continue  # Reinicia o loop global: volta para a Fase 1 com score [0]
                    elif level_return is False:
                        break  # Sai do jogo e volta para o Menu Principal

                    # ================= FASE 2 =================
                    # Se o código chegou aqui, significa que level_return foi True (passou da Fase 1)
                    level = Level(self.window, 'LEVEL2', menu_return, player_score)
                    level_return = level.run(player_score)

                    if level_return == "RESTART":
                        continue  # Perde tudo! Volta lá para o início do loop (Fase 1 com score [0])
                    elif level_return is False:
                        break  # Sai do jogo e volta para o Menu Principal
                    elif level_return is True:
                        score.save(MENU_OPTION[0], menu_return, player_score)
                        break  # Jogo finalizado com sucesso, sai do loop



            elif menu_return == MENU_OPTION[1]:
                menu.show_controls()


            elif menu_return == MENU_OPTION[2]:  # exit
                score.show()


            elif menu_return == MENU_OPTION[3]:  # exit
                pygame.quit()  # Close window
                quit()  # end pygame
            else:
                pass

