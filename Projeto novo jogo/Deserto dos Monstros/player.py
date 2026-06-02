#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED
from entity import Entity

class Player(Entity):

    def __init__(self, name:str , position):
        super().__init__(name, position)

    #     try:
    #         # Carrega a imagem
    #         self.spritesheet = pygame.image.load('./asset/player.png').convert_alpha()
    #
    #         # Configuração do spritesheet
    #         self.frame_width = 90
    #         self.frame_height = 128
    #         self.num_frames = 6
    #
    #         self.frames = []
    #         for i in range(self.num_frames):
    #             frame = self.spritesheet.subsurface(
    #                 pygame.Rect(i * self.frame_width, 0, self.frame_width, self.frame_height)
    #             )
    #             frame_scaled = pygame.transform.scale(frame, (75, 125))
    #             self.frames.append(frame_scaled)
    #
    #         self.current_frame = 0
    #         self.surf = self.frames[0]
    #         self.rect = self.surf.get_rect()
    #
    #         # Posição inicial - Canto esquerdo (ajustado)
    #         self.rect.left = -20
    #         self.rect.bottom = WIN_HEIGHT - 10
    #
    #         # Variáveis de movimento e animação
    #         self.velocidade_y = 0
    #         self.no_chao = True
    #         self.direcao = 1  # 1 = direita, -1 = esquerda
    #         self.animation_time = 0
    #         self.animation_speed = 0.12
    #
    #         print("✅ Personagem carregado com sucesso!")
    #
    #     except Exception as e:
    #         print(f"❌ Erro ao carregar: {e}")
    #
    #         # ====================== MOVIMENTAÇÃO ======================
    #
    # def update(self, dt=0.016):
    #     # Gravidade
    #     self.velocidade_y += 1.5
    #     self.rect.y += self.velocidade_y
    #
    #     # Colisão com o chão
    #     if self.rect.bottom >= WIN_HEIGHT - 45:
    #         self.rect.bottom = WIN_HEIGHT - 45
    #         self.velocidade_y = 0
    #         self.no_chao = True
    #
    #     # Animação
    #     self.animation_time += dt
    #     if self.animation_time >= self.animation_speed:
    #         self.animation_time = 0
    #         self.current_frame = (self.current_frame + 1) % self.num_frames
    #         self.surf = self.frames[self.current_frame]
    #
    # def mover_esquerda(self):
    #     self.rect.x -= 7
    #     self.direcao = -1
    #
    # def mover_direita(self):
    #     self.rect.x += 7
    #     self.direcao = 1
    #
    # def pular(self):
    #     if self.no_chao:
    #         self.velocidade_y = -26  # Força do pulo
    #         self.no_chao = False

    pass


    def move(self, ):

       pressed_key = pygame.key.get_pressed()
       if pressed_key[pygame.K_RIGHT]  and self.rect.right < WIN_WIDTH:
           self.rect.right += ENTITY_SPEED[self.name]

       if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
           self.rect.left -= ENTITY_SPEED[self.name]

       pass
