#!/usr/bin/python
# -*- coding: utf-8 -*-
from const import ENTITY_SPEED, ENTITY_SHOOT_DELAY
from enemyShot import EnemyShot
from entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        self.rect.left -= ENTITY_SPEED[self.name]

    def shoot(self ):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            gun_offset_x = self.rect.width - 7
            gun_offset_y = 33

            shot_x = self.rect.x + gun_offset_x
            shot_y = self.rect.y + gun_offset_y

            return EnemyShot(name=f'{self.name}Shot', position=(shot_x, shot_y))