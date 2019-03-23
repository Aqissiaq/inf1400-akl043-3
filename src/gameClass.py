import pygame
import config
from player import Player
from inputHandler import InputHandler

class GameClass():
    """The game class for the Mayhem game. Handles pygame initialization and the game loop"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.screen_res)
        self.clock = pygame.time.Clock()

        self.inputHandler = InputHandler()
        self.allSprites = pygame.sprite.Group()
        for i in range(0, config.num_players):
            self.allSprites.add(Player(i, self.inputHandler, self.allSprites))

    def start(self):
        """Begin the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.clock.tick(config.fps)
            deltaTime = self.clock.get_time()
            self.screen.fill(config.background_color)
            self.update(deltaTime)
            pygame.display.flip()


    def update(self, deltaTime):
        """Called for each tick of the game loop to update all game objects"""
        self.inputHandler.update()
        self.allSprites.update(deltaTime)
        self.allSprites.draw(self.screen)