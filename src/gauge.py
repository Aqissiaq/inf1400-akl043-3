import pygame

class Gauge(pygame.sprite.Sprite):
    """Class for UI gauges such as fuel"""
    def __init__(self, maxValue, parentPlayer, color=(0,255,0)):
        super().__init__()

        self.maxValue = maxValue
        self.fillColor = color
        self.parent = parentPlayer

        self.image = pygame.Surface([maxValue, 10])
        self.image.fill(self.fillColor)
        self.rect = self.image.get_rect()

    def update(self, deltaTime):
        self.rect = self.image.get_rect(center=self.parent.position + (0, 60))
        self.image = pygame.transform.scale(self.image, (self.parent.fuel, 10))

    def draw(self, screen):
        pass