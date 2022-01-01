from abc import abstractproperty
from typing import Any, Collection, List
import pygame
from pygame.scrap import set_mode
from colors import Colors
from bullet import Bullet
from pygame.sprite import Group

class Player(pygame.sprite.Sprite):
    def __init__(self, window_width: int, window_height: int, bullets: Group, all_sprites: Group, *groups: abstractproperty) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((11,60))
        self.image.fill(Colors.RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = window_width / 2
        self.rect.bottom = window_height - 10
        self.speedx = 0
        self.horizontal_speed = 8
        self.window_width = window_width
        self.window_height = window_height
        self.bullets = bullets
        self.all_sprites = all_sprites

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = self.horizontal_speed * -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.horizontal_speed
        self.rect.x += self.speedx
        if self.rect.right > self.window_width:
            self.rect.right = self.window_width
        if self.rect.left < 0:
            self.rect.left = 0
        return super().update(*args, **kwargs)
    
    def shoot(self) -> None:
        bullet = Bullet(self.rect.centerx, self.rect.top)
        self.all_sprites.add(bullet)
        self.bullets.add(bullet)
