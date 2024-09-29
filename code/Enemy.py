#!/usr/bin/python

# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


# Implementação do Enemy3 com lógica de movimento diferente
class Enemy3(Enemy):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.speed_y = 2  # Velocidade vertical básica
        self.moving_up = True  # Indica se o inimigo está subindo

    def move(self):
        # Movimento horizontal: da direita para a esquerda
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical: sobe e desce
        if self.moving_up:
            self.rect.centery -= self.speed_y
            if self.rect.top <= 0:  # Se bater na borda superior
                self.moving_up = False  # Começa a descer
        else:
            self.rect.centery += self.speed_y * 2  # Desce com o dobro da velocidade
            if self.rect.bottom >= WIN_HEIGHT:  # Se bater na borda inferior
                self.moving_up = True  # Começa a subir novamente


