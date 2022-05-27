import pygame
from ship import Ship
from bullet import Bullet
from enemies import ChaseEnemy
from particles import Particle, Explosion
from hud import Hud
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

# explosion particles
explosions = []

# hud 
hud = Hud(player, screen)

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
    # update hud
    hud.update()

    # check for collisions between bullet and ememies
    hits = pygame.sprite.groupcollide(bullet_group, enemy_group, True, True)
    # iterate through each enmy the bullet hits
    
    for bullet in hits:
        # get the enemy the bullet hits
        enemy = hits[bullet]
        explosions.append(Explosion((enemy[0].x, enemy[0].y)))
        player.score += len(hits[bullet])


    # check for collisions between player and enemies
    hits = pygame.sprite.groupcollide(player_group, enemy_group, False, False)
    if hits:
        player.damage(3)
    
    # draw all explosions
    for explosion in explosions:
        explosion.drawParticles(screen)
    
    print(player.score)
    
    # update
    pygame.display.update()
    clock.tick(30)