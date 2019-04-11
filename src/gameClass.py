import pygame
import config
from player import Player
from terrain import Terrain
from fuelPlatform import FuelPlatform
from inputHandler import InputHandler
from random import choice

class GameClass():
    """The game class for the Mayhem game. Handles pygame initialization and the game loop"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.screen_res)
        self.clock = pygame.time.Clock()

        self.inputHandler = InputHandler()
        self.allSprites = pygame.sprite.RenderUpdates()
        self.playerList = []
        
        self.constructLevel(config.level)

        for i in range(0, config.num_players):
            newPlayer = Player(i, self.inputHandler, self.screen, self.allSprites)
            self.playerList.append(newPlayer)
            self.allSprites.add(newPlayer.rocket)



    def start(self):
        """Begin the game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.clock.tick()
            deltaTime = self.clock.get_time()
            self.screen.fill(config.background_color)
            self.update(deltaTime)

            if(len(self.playerList) == 1):
                print(f"Player {self.playerList[0].id+1} wins!")
                break


    def update(self, deltaTime):
        """Called for each tick of the game loop to update all game objects"""
        self.inputHandler.update()
        self.allSprites.update(deltaTime)
        self.allSprites.draw(self.screen)
        for player in self.playerList:
            player.update()
            if player.dead:
                self.playerList.remove(player)
        pygame.display.update()

    def constructLevel(self, input):
        """Constructs the level from the input in the config file"""
        lines = input.split("\n")[1:-1]
        blockHeight = int(config.screen_res[1] / len(lines))
        blockWidth = int(config.screen_res[0] / len(lines[0]))
        terrainColor = choice(config.terrain_colors)

        for x in range(0, len(lines[0])):
            for y in range(0, len(lines)):
                if lines[y][x] == "@":
                    self.allSprites.add(Terrain((x*blockWidth, y*blockHeight),
                                        blockWidth,
                                        blockHeight,
                                        terrainColor,
                                        self.allSprites
                                        )
                                )
                elif lines[y][x] == "#":
                    self.allSprites.add(FuelPlatform((x*blockWidth, y*blockHeight),
                                        blockWidth,
                                        blockHeight*.5,
                                        config.fuelplatform_color,
                                        self.allSprites
                                        )
                                )