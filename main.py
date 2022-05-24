import pygame
from ship import Ship
from bullet import Bullet
from enemies import ChaseEnemy
import random

size = w,h = (1300, 1300)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()

# method to place enemies
def gen_enemies(num: int, screen):
    enemy_group = pygame.sprite.Group()
    for i in range(0, num):
        x = random.randint(0, 1300)
        y = random.randint(0, 1300)

        enemy = ChaseEnemy(screen, (x, y))
        enemy_group.add(enemy)

    return enemy_group

# bullet sprites
bullet_group = pygame.sprite.Group()

# player
player = Ship((650, 650), screen, bullet_group)
player_group = pygame.sprite.Group(player)

# enemies
enemy_group = gen_enemies(10, screen)

# game loop
running = True
while running:
    screen.fill(black)

    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # update player sprite
    player.update()
    # update bullet sprites
    bullet_group.update()
    # update enemy sprites
    enemy_group.update(player.get_pos())

    # check for collisions
    pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)

    # update
    pygame.display.update()
    clock.tick(30)