from random import randrange
from colors import Colors
from mob import Mob
from player import Player
import pygame
from pygame.constants import K_SPACE

width = 511
height = 511
fps = 60

#init pygame and window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Практична робота 9")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player(width, height, bullets, all_sprites)
all_sprites.add(player)
for i in  range(8):
    m = Mob(width, height)
    all_sprites.add(m)
    mobs.add(m)


#game loop
runing = True
while runing:
    #tick rate
    clock.tick(fps)
    #process event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
    #updating
    all_sprites.update()
    #on collission
    hits = pygame.sprite.spritecollide(player, mobs, False)
    if hits:
        runing = False
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob(width, height)
        all_sprites.add(m)
        mobs.add(m)
    #rendering
    screen.fill(Colors.BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()