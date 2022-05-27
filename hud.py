from multiprocessing import set_forkserver_preload
import pygame
from ship import Ship

class Hud:
    def __init__(self, player: Ship, screen) -> None:
        self.player = player
        self.screen = screen

        # health bar
        self.health_bar = pygame.Rect(20, 20, self.player.hp * 2, 50)
        self.bg = self.health_bar.inflate(0.5, 0.5)

    def draw(self):
        # Health bar
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

        # score text
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(
            f'Score:  {self.player.score}', 
            True, 
            (255, 255, 255),
            (0, 0, 0)
        )
        text_rect = text.get_rect()
        text_rect.center = (90, 90)
        self.screen.blit(text, text_rect)

        self.draw()
