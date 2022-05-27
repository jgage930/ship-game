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
pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# method for writing text
font = pygame.font.SysFont(None, 20)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# method to place enemies
def gen_enemies(num: int, screen):
    enemy_group = pygame.sprite.Group()
    for i in range(0, num):
        x = random.randint(0, 1300)
        y = random.randint(0, 1300)

        enemy = ChaseEnemy(screen, (x, y))
        enemy_group.add(enemy)

    return enemy_group

# main menu loop
click = False
def main_menu():
    while True:
        screen.fill(black)
        draw_text('main menu', font, black, screen, 20, 20)

        mouse_pos = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        if button_1.collidepoint(mouse_pos):
            if click:
                game()

        pygame.draw.rect(screen, (255, 0, 0), button_1)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(30)

# game loop 
def game():
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

main_menu()