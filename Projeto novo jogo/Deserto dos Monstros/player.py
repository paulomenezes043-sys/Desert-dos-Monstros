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
        self.up_pressed = False
    pass

    def move(self):

        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.right += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_UP]:
            if not self.up_pressed:
                self.jump()
                self.up_pressed = True
        else:
            self.up_pressed = False

        pass
    def jump(self):
        self.sound_jump = pygame.mixer.Sound('asset/jump_player.wav')
        self.sound_jump.set_volume(1.0)
        #Faz o jogador pular se estiver no chão
        if self.on_ground:
            self.speed_y = -22
            self.on_ground = False
            self.sound_jump.play()

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

        if self.shot_delay > 0:
            self.shot_delay -= 1

        #  Captura o estado da tecla
        pressed_key = pygame.key.get_pressed()
        is_shooting_now = pressed_key[PLAYER_KEY_SHOOT[self.name]]

        #  Só atira se o delay estiver zerado E a tecla acabou de ser apertada
        if self.shot_delay == 0 and is_shooting_now and not self.shot_pressed_last_frame:

            # Reinicia o delay (cooldown)
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

            # Lógica do tiro
            gun_offset_x = self.rect.width - 7
            gun_offset_y = 33
            shot_x = self.rect.x + gun_offset_x
            shot_y = self.rect.y + gun_offset_y

            # Som
            if hasattr(self, 'shoot_sound') and self.shoot_sound is not None:
                self.shoot_sound.play()

            # Atualiza o estado da tecla para não atirar continuamente
            self.shot_pressed_last_frame = is_shooting_now
            return PlayerShot(name=f'{self.name}Shot', position=(shot_x, shot_y))

        # 4. Atualiza o estado da tecla para o próximo frame
        self.shot_pressed_last_frame = is_shooting_now
        return None
