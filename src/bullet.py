import pygame
import config

class Bullet(pygame.sprite.Sprite):

    def __init__(self, parent, *groups, color=(0,0,255)):
        super().__init__(groups)

        self.parent = parent
        self.color = color

        self.image = pygame.Surface([5, 5])
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        
        self.position = pygame.Vector2(parent.position)
        self.velocity = pygame.Vector2(parent.direction)*config.bullet_speed

    def update(self, deltaTime):
        self.position += self.velocity*deltaTime
        self.rect.center = self.position

    def draw(self, screen):
        pass
