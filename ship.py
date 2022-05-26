import pygame
import math

from bullet import Bullet

class Ship(pygame.sprite.Sprite):

    def __init__(self, start:tuple, screen, bullet_group) -> None:
        super().__init__()

        self.screen = screen

        # position
        self.x, self.y = start

        # dimensions
        self.w = 30
        self.h = 50

        # speed 
        self.speed = 20

        # load image
        img = pygame.image.load('art/ship_sprite.png')
        self.image = pygame.transform.scale(img, (100, 100))
        # hurt box
        self.rect = self.image.get_rect()

        # save original image for rotation
        self.orig_image = self.image

        # bullet group
        self.bullet_group = bullet_group

        # check if player is holding the mouse button
        self.is_holding = False

        self.hp = 100

    def handle_keys(self):
        # handle all key presses in this method
        keys = pygame.key.get_pressed()

        # movement
        if keys[pygame.K_w]:
            if self.y >= self.speed:
                self.y -= self.speed

        if keys[pygame.K_s]:
            if self.y <= 1200 - self.h - self.speed:
                self.y += self.speed

        if keys[pygame.K_a]:
            if self.x >= self.speed:
                self.x -= self.speed

        if keys[pygame.K_d]:
            if self.x <= 1300 - self.speed:
                self.x += self.speed

        # shoot on mouse click make it so the player can't hold downt he mouse and shoot
        left, middle, right = pygame.mouse.get_pressed()
        if left and not self.is_holding:
            self.shoot()
            self.is_holding = True
        
        if not left:
            self.is_holding = False
            
    def draw(self):
        # update rect location
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)

    def rotate(self):
        # rotates ship in the direction of the mouse
        # get mouse pdddstion
        mx, my = pygame.mouse.get_pos()

        dx, dy = mx - self.rect.centerx, self.rect.centery - my
        correction_angle = 90
        angle = -1 * math.degrees(math.atan2(-dy, dx)) - correction_angle
        
        # save original center
        orig_center = self.rect.center

        self.image = pygame.transform.rotate(self.orig_image, angle)
        self.rect = self.image.get_rect(center=orig_center)

    def shoot(self):
        # creates a bullet at the players location and shoots it towards the mouse and adds to bullet group
        target = pygame.mouse.get_pos()
        start = (self.x, self.y)
        
        bullet = Bullet(self.screen, start, target)
        self.bullet_group.add(bullet)

    def get_pos(self):
        return (self.x, self.y)

    def get_hurtbox(self):
        return self.rect

    def damage(self, amount: int):
        self.hp -= amount

    def update(self):
        self.handle_keys()
        self.rotate()
        self.draw()