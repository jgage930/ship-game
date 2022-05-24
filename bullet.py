import pygame
import math

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, start: tuple, target: tuple):
        super().__init__()

        self.screen = screen

        # load image
        img = pygame.image.load('art/bullet_sprite.png')
        self.image = pygame.transform.scale(img, (100, 100))

        # hitbox
        self.rect = self.image.get_rect()

        # position
        self.x, self.y = start

        # target
        tx, ty = target

        # set center
        self.rect.center = start

        # speed 
        self.speed = 40

        # calculate direction
        angle = -1 * math.atan2((ty - self.y), (tx - self.x))

        # set speed in x and y
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def draw(self):
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)

    def off_screen(self) -> bool:
        # returns true if the bullet is off the screen
        if 0 < self.x < 1300 and 0 < self.y < 1300:
            return True
        return False

    def update(self):
        self.x += self.dx
        self.y -= self.dy

        self.rect.center = (self.x, self.y)
        self.draw()