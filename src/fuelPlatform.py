import pygame
from terrain import Terrain

class FuelPlatform(Terrain):

    def __init__(self, position, width, height, color=(0,0,255), *groups):
        super().__init__(position, width, height, color, groups)
        
