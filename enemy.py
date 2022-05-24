import pygame

# a class for enemies, right now it is just red squares
class Enemy(pygame.sprite.Sprite):

    def __init__(self, screen, loc: tuple):
        super().__init__()

        self.screen = screen

        self.x, self.y = loc

        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self):
        pygame.draw.rect(
            self.screen,
            color=(255, 0, 0),
            rect=self.rect
        )

    def update(self):
        self.draw()