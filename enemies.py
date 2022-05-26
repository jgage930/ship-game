import pygame
import math

# a class for enemies, right now it is just red squares
class ChaseEnemy(pygame.sprite.Sprite):

    def __init__(self, screen, loc: tuple):
        super().__init__()

        self.screen = screen

        self.x, self.y = loc
        
        img = pygame.image.load('art/enemy1_sprite.png')
        self.image = pygame.transform.scale(img, (70, 70))

        self.rect = self.image.get_rect()
        self.rect.center = loc

        # speed
        self.speed = 5

        # rotation stuff
        self.orig_img = self.image

    def draw(self):
        self.rect.center = (self.x, self.y)
        self.screen.blit(self.image, self.rect)

    def chase(self, target:tuple):
        # to rotate and move in the direction of the player 
        tx, ty = target

        angle = -1 * math.atan2(ty - self.y, tx - self.y)
        
        dx = self.speed * math.cos(angle)
        dy = self.speed * math.sin(angle)

        self.x += dx
        self.y -= dy

        # rotate towards the player
        orig_center = self.rect.center
        angle = math.degrees(angle) - 90

        self.image = pygame.transform.rotate(self.orig_img, angle)
        self.rect = self.image.get_rect(center=orig_center)

    def update(self, target:tuple):
        self.draw()
        self.chase(target)
