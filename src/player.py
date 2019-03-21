import pygame
import config

class Player(pygame.sprite.Sprite):
    
    def __init__(self, id):
        super().__init__()
        self.keymap = config.keymaps[id]
        self.id = id

        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

    def update(self, keys):
        
        # inputs
        right = keys[self.keymap["right"]]
        left = keys[self.keymap["left"]]
        thrust = keys[self.keymap["thrust"]]
        shoot = keys[self.keymap["shoot"]]