#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from background import Background
from const import WIN_WIDTH, WIN_HEIGHT
from enemy import Enemy
from player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position: tuple = None):
        match entity_name:
            case 'LEVEL1BG':
                list_bg = []
                for i in range(5):  # level 1
                    list_bg.append(Background(f'LEVEL1BG{i}', (0, 0)))
                    list_bg.append(Background(f'LEVEL1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'LEVEL2BG':
                list_bg = []
                for i in range(5):  # level 2
                    list_bg.append(Background(f'LEVEL2BG{i}', (0, 0)))
                    list_bg.append(Background(f'LEVEL2BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                # Se passares uma posição específica no nível, ele usa. Se não, usa a padrão atual:
                pos = position if position else (5, WIN_WIDTH / 2 - 30,
                                                 WIN_HEIGHT - 10)  # Nota: verifica se querias mesmo 3 argumentos aqui na tua tupla do Player
                return Player(name='Player', position=pos)

            case 'Enemy1':
                pos = position if position else (WIN_WIDTH + 50, WIN_HEIGHT - 70)
                return Enemy(name='Enemy1', position=pos)

            case 'Enemy2':
                pos = position if position else (WIN_WIDTH + 30, WIN_HEIGHT - 70)
                return Enemy(name='Enemy2', position=pos)

            case 'Enemy3':
                pos = position if position else (WIN_WIDTH + 0, WIN_HEIGHT - 80)
                return Enemy(name='Enemy3', position=pos)
            case 'Enemy4':
                pos = position if position else (WIN_WIDTH + 30, WIN_HEIGHT - 80)
                return Enemy(name='Enemy4', position=pos)
            case 'Enemy5':
                pos = position if position else (WIN_WIDTH + 60, WIN_HEIGHT - 70)
                return Enemy(name='Enemy5', position=pos)