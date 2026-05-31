#!/usr/bin/python
# -*- coding: utf-8 -*-
from background import Background
from const import WIN_WIDTH


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
