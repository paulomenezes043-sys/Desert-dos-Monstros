#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.mixer

from const import ENTITY_SPEED, ENTITY_SHOOT_DELAY
from enemyShot import EnemyShot
from entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        self.rect.left -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1

        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            print(f'inimigo atirando teem som?{hasattr(self, 'enemy_attack_sound')}')
            if hasattr(self, 'enemy_attack_sound'):
                self.enemy_attack_sound.play()
                print('DEU PLAY NO SOM')
            gun_offset_x = self.rect.width - 7
            gun_offset_y = 33

            shot_x = self.rect.x + gun_offset_x
            shot_y = self.rect.y + gun_offset_y

            return EnemyShot(name=f'{self.name}Shot', position=(shot_x, shot_y))
