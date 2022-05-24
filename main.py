import pygame
from ship import Ship
from bullet import Bullet

size = w,h = (1300, 1300)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()

# bullet sprites
bullet_group = pygame.sprite.Group()

# player
player = Ship((650, 650), screen, bullet_group)
player_group = pygame.sprite.Group(player)

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

    # update
    pygame.display.update()
    clock.tick(30)