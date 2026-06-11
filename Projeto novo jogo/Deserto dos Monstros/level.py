#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys

import pygame
from pygame import Surface
from pygame.font import Font
from pygame.rect import Rect

from const import EVENT_ENEMY, SPAWN_TIME, C_BLACK, WIN_WIDTH, C_BLUE, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from enemy import Enemy
from entity import Entity
from entityFactory import EntityFactory
from entityMediator import EntityMediator
from player import Player


class Level:
    def __init__(self, window:Surface,  name: str , game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode  # modo do jogo
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'BG'))
        player = EntityFactory.get_entity('Player')
        player.shoot_sound = None  # ← importante
        player.score = player_score[0]
        self.entity_list.append(player)
        self.shoot_sound = None
        self.enemy_attack_sound = None


        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)


    def run(self, player_score: list[int]):
        pygame.mixer.music.load(f'./asset/{self.name}.wav')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        try:
         self.shoot_sound = pygame.mixer.Sound(f'./asset/sound_tiro1.wav')
         self.enemy_attack_sound = pygame.mixer.Sound(f'./asset/attack_enemy1.wav')
         self.shoot_sound.set_volume(1.0)
         self.enemy_attack_sound.set_volume(0.7)
         print('Sons Carregados')
        except Exception as e:
            print('Erro ao carregar o som',e)
        for ent in self.entity_list:
            if isinstance(ent, Player):
                ent.shoot_sound = self.shoot_sound


        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if hasattr(ent,'update'):
                    ent.update()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(14, f'Player - Health:{ent.health}|Score:{ent.score}',C_BLUE, (6, 20))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    new_enemy = EntityFactory.get_entity(choice)
                    new_enemy.enemy_attack_sound = self.enemy_attack_sound
                    self.entity_list.append(new_enemy)
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score

                        return  True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False


            self.level_text(14, f'{self.name} - Timeout:{self.timeout / 1000:.1f}s', C_BLACK, (6, 3))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', C_BLACK, (WIN_WIDTH - 108, 1))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', C_BLACK, (WIN_WIDTH - 60, 15))

            pygame.display.flip()
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
