import pygame
from modules.constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Cargar imagen
        self.image = pygame.image.load("assets/player.png").convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Posicion default
        self.default_x = x
        self.default_y = y
        
        # Flags movimiento
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.delta_x = 0
        self.delta_y = 0

        # Atributos
        self.speed = 3
        self.alive = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)
     
    def move(self):
        self.delta_x = 0
        self.delta_y = 0

        if self.moving_left and self.rect.left > 0:
            self.delta_x -= self.speed
        if self.moving_right and self.rect.right < SCREEN_WIDTH:
            self.delta_x += self.speed
        if self.moving_up and self.rect.top > 0:
            self.delta_y -= self.speed
        if self.moving_down and self.rect.bottom < SCREEN_HEIGHT:
            self.delta_y += self.speed

        # Actualizar posicion
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y
    
    def dead(self):
        self.alive = False
        self.image = pygame.image.load("assets/player_dead.png").convert()
    
    def reset(self):
        self.alive = True
        self.image = pygame.image.load("assets/player.png").convert()
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.rect.center = (self.default_x, self.default_y)

    
           