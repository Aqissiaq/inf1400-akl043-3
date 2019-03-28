import pygame

class Terrain(pygame.sprite.Sprite):
    """
    The class used to handle terrain objects.
    These are objects that the player can not fly through.
    """
    def __init__(self, position, width, height, color=(255, 255, 255), *groups):
        super().__init__(groups)

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = position