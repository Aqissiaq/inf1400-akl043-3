import pygame
import config
from gauge import Gauge
from bullet import Bullet
from text import Text
from terrain import Terrain
from fuelPlatform import FuelPlatform
from explosion import Explosion

class Player():
    """The handler class for players, keeps track of persistent variables like score and lives"""
    def __init__(self, id, inputHandler, screen, *groups):
        self.rocket = Rocket(id, inputHandler, self, groups)

        self.id = id
        self.score = 0
        self.lives = config.player_lives
        self.dead = False

        self.scoreText = Text(f"Player {id+1} Score:",
                        screen,
                        pygame.font.SysFont(None, 32),
                        config.player_color[id],
                        pygame.Vector2(100 + self.id * 300, config.screen_res[1] - 50)
                        )
        self.livesText = Text("Lives:",
                        screen,
                        pygame.font.SysFont(None, 32),
                        config.player_color[id],
                        pygame.Vector2(250 + self.id * 300, config.screen_res[1] - 50)
                        )

    def increaseScore(self, amount):
        self.score += amount

    def update(self):
        self.scoreText.draw(self.score)
        self.livesText.draw(self.lives)

class Rocket(pygame.sprite.Sprite):
    """Class for drawing a player's rocket to screen. Inherits from pygame.sprite.Sprite"""
    def __init__(self, id, inputHandler, parent, *groups):
        super().__init__(groups)

        # rocket sprite from https://opengameart.org/content/rocket
        self.image = pygame.image.load("assets/cohete_bw.png")
        self.image = pygame.transform.scale(self.image, config.player_size)
        self.image.fill(config.player_color[id], special_flags=pygame.BLEND_MULT)
        self.originalImage = self.image.copy()
        self.rect = self.image.get_rect()

        self.id = id
        self.parent = parent
        self.keymap = config.keymaps[id]
        self.inputHandler = inputHandler

        self.angle = 0
        self.shootDelay = config.shoot_delay
        self.direction = pygame.Vector2(0, -1)
        self.position = pygame.Vector2(config.starting_positions[id])
        self.rect.center = self.position
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.fuel = config.starting_fuel
        self.fuelBar = Gauge(self.fuel, self)
        self.fuelBar.add(self.groups())

    def update(self, deltaTime):
        """
        Updates player velocity and position based on input.
        deltatime is time since last update
        """
        # inputs
        keys = self.inputHandler.getPressed()
        right = keys[self.keymap["right"]]
        left = keys[self.keymap["left"]]
        thrust = keys[self.keymap["thrust"]]
        shoot = keys[self.keymap["shoot"]]

            
        self.acceleration = (0,0)
        self.acceleration += config.gravity*deltaTime
        self.checkForCollisions()

        self.shootDelay += deltaTime
        if shoot and self.shootDelay > config.shoot_delay:
            self.shoot()
        self.updateRotation(left, right, deltaTime)
        self.updateThrust(thrust, deltaTime)
        

        self.velocity += self.acceleration*deltaTime
        if self.velocity.length() > config.max_speed:
            self.velocity.scale_to_length(config.max_speed)
        

        # update position
        self.position += self.velocity*deltaTime
        self.position.x %= config.screen_res[0]
        self.position.y %= config.screen_res[1]
        self.rect.center = self.position



    def updateRotation(self, left, right, deltaTime):
        """Helper function to handle rotation part of player update"""
        newAngle = (config.player_rotation_speed*left - config.player_rotation_speed*right)*deltaTime
        self.angle += newAngle
        self.direction.rotate_ip(-newAngle)
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def updateThrust(self, thrust, deltaTime):
        """Helper function to handle thrust part of player update"""
        if(self.fuel > 0):
            self.fuel -= thrust*.5
            self.acceleration += self.direction * thrust * config.player_thrust*deltaTime

    def shoot(self):
        """Helper function for firing rockets. Spawns a new Bullet object"""
        self.shootDelay = 0
        Bullet(self, config.player_color[self.id], self.groups())

    
    def checkForCollisions(self):
        """Checks for collisions and handles interaction within the sprite group"""
        hitList = pygame.sprite.spritecollide(self, self.groups()[0], False)
        for other in [x for x in hitList if x is not self]:
            otherType = type(other)
            if otherType is Bullet:
                other.increaseScore(config.kill_score)
                other.kill()
                self.killForReal()
            elif otherType is Terrain or otherType is Rocket:
                self.killForReal()
            elif otherType is FuelPlatform:
                self.acceleration = pygame.Vector2(0,0)
                self.velocity = pygame.Vector2(0,0)
                self.fuel += 1
                self.fuel = min(self.fuel, config.starting_fuel)

    def killForReal(self):
        """
        Kills the player object and its fuel gauge.
        Respawns rocket unless player is out of lives
        """
        self.parent.lives -= 1
        if self.parent.lives > 0:
            Rocket(self.id, self.inputHandler, self.parent, self.groups())
        else:
            self.parent.dead = True
        Explosion(self.position, self.groups())
        self.fuelBar.kill()
        self.kill()

    def increaseScore(self, amount):
        self.parent.increaseScore(amount)