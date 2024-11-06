import pygame
from modules.constants import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        super().__init__()
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.type = type

        if self.type == 1:
            self.surface.fill(COLOR_GRAY)
        elif self.type == 2:
            self.surface = pygame.image.load("assets/obstacle.png")
        elif self.type == 3:
            self.surface = pygame.image.load("assets/goal.png")

        self.rect = self.surface.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self, screen):
        screen.blit(self.surface, self.rect)