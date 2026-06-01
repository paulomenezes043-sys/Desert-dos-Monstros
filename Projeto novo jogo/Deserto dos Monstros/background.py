#!/usr/bin/python
# -*- coding: utf-8 -*-
from pygame import transform

from const import WIN_WIDTH, ENTETY_SPEED, BG_HEIGHT, BG_WIDTH
from entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

#REDIMENSIONAR IMAGEM
        if hasattr(self, 'surf') and self.surf is not None:
            self.surf = transform.scale(self.surf, (BG_WIDTH, BG_HEIGHT))

            #atualizar rect com tamanho novo
            self.rect = self.surf.get_rect(topleft=position)



    def move(self, ):
        self.rect.centerx -= ENTETY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
