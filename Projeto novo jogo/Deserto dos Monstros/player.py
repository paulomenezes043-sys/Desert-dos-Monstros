#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from const import WIN_WIDTH, ENTITY_SPEED, ENTITY_SHOOT_DELAY, PLAYER_KEY_SHOOT, FLOOR_Y, GRAVITY
from entity import Entity
from pLayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
        self.speed_y = 0
        self.on_ground = True
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

    def move(self):

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.right += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_UP]:
             self.jump()

        pass
    def jump(self):
        #Faz o jogador pular se estiver no chão
        if self.on_ground:
            self.speed_y = -26
            self.on_ground = False

    def update(self):
        # Aplica gravidade
        self.speed_y += GRAVITY

        # Move o personagem para cima/baixo
        self.rect.y += int(self.speed_y)

        # Colisão com o chão (ajuste FLOOR_Y!)
        if self.rect.bottom >= FLOOR_Y:
            self.rect.bottom = FLOOR_Y
            self.speed_y = 0
            self.on_ground = True
        else:
            self.on_ground = False


    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                gun_offset_x = self.rect.width - 7
                gun_offset_y = 33

                shot_x = self.rect.x + gun_offset_x
                shot_y = self.rect.y + gun_offset_y

                #SOM DOS TIROS
                if hasattr(self, 'shoot_sound') and self.shoot_sound is not None:
                    self.shoot_sound.play()


                return PlayerShot(name=f'{self.name}Shot', position=(shot_x, shot_y))

            return None
