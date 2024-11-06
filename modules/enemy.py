import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, patrol_distance=100, axis='x', speed=2, direction=1):
        super().__init__()

        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Movimiento
        self.starting_pos = (x, y) 
        self.patrol_distance = patrol_distance  
        self.direction = direction
        self.speed = speed
        self.axis = axis

    def move(self):
        if self.axis == 'x':
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.starting_pos[0]) >= self.patrol_distance:
                self.direction *= -1  
        elif self.axis == 'y':
            self.rect.y += self.speed * self.direction
            if abs(self.rect.y - self.starting_pos[1]) >= self.patrol_distance:
                self.direction *= -1 

    def draw(self, screen):
        screen.blit(self.image, self.rect)