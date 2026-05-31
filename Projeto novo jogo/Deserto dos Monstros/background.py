#!/usr/bin/python
# -*- coding: utf-8 -*-
from const import WIN_WIDTH, ENTETY_SPEED
from entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)



    def move(self, ):
        self.rect.centerx -= ENTETY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
