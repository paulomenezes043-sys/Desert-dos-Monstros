#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from background import Background
from const import WIN_WIDTH, WIN_HEIGHT
from enemy import Enemy
from player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'LEVEL1BG':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'LEVEL1BG{i}', (0, 0)))
                    list_bg.append(Background(f'LEVEL1BG{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player('Player',(5,WIN_WIDTH / 2 -30, WIN_HEIGHT -10 ))
            case 'Enemy1':
                return Enemy('Enemy1', (WIN_WIDTH +50, WIN_HEIGHT -70))
