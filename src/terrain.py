import pygame

class Terrain(pygame.sprite.Sprite):
    """
    The class used to handle terrain objects.
    These are objects that the player can not fly through."
    """
    def __init__(self, groups*):
        super().__init__(groups)
