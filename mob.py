from abc import abstractproperty
from typing import Any
import pygame
import random
from colors import Colors

class Mob(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, *groups: abstractproperty) -> None:
        super().__init__(*groups)
        self.image = pygame.Surface((30, 40))
        self.image.fill(Colors.BLUE)
        self.rect = self.image.get_rect()        
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 8)
        self.speed_x = random.randrange(-3, 3)
        self.screen_height = screen_height
        self.screen_width = screen_width

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top > self.screen_height + 10 or self.rect.left < -25 or self.rect.right > self.screen_width + 20:
            self.rect.x = random.randrange(self.screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed_y = random.randrange(1,8)
        return super().update(*args, **kwargs)