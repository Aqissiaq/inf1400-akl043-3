import pygame
import config
from player import Player

class GameClass():
    """The game class for the Mayhem game. Handles pygame initialization and the game loop"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.screen_res)
        self.clock = pygame.time.Clock()

        self.players = []
        for i in range(0, config.num_players):
            self.players.append(Player(i))

    def start(self):
        """Begin the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            keys = pygame.key.get_pressed()
            self.update(keys)
            self.screen.fill(config.background_color)
            self.clock.tick(config.fps)

    def update(self, keys):
        """Called for each tick of the game loop"""
        for player in self.players:
            player.update(keys)