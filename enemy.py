import pygame

# a class for enemies, right now it is just red squares
class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, loc: tuple):
        super().__init__()

        self.screen = screen

        self.x, self.y = loc
        
        img = pygame.image.load('art/enemy1_sprite.png')
        self.image = pygame.transform.scale(img, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = loc

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()