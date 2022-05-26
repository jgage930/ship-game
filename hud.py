import pygame
from ship import Ship

class Hud:
    def __init__(self, player: Ship, screen) -> None:
        self.player = player
        self.screen = screen
        self.health_bar = pygame.Rect(20, 20, self.player.hp * 2, 50)
        self.bg = self.health_bar.inflate(0.5, 0.5)

    def draw(self):

        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            self.bg
        )
        pygame.draw.rect(
            self.screen, 
            (255, 0, 0),
            self.health_bar
        )

    def update(self):
        self.health_bar = pygame.Rect(20, 20, self.player.hp * 2, 50)
        self.draw()
