import pygame
import config
from gauge import Gauge
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    
    def __init__(self, id, inputHandler, *groups):
        super().__init__(groups)

        # rocket sprite from https://opengameart.org/content/rocket
        self.image = pygame.image.load("assets/cohete_bw.png")
        self.image = pygame.transform.scale(self.image, config.player_size)
        self.image.fill(config.player_color[id], special_flags=pygame.BLEND_MULT)
        self.originalImage = self.image.copy()
        self.rect = self.image.get_rect()

        self.keymap = config.keymaps[id]
        self.id = id
        self.inputHandler = inputHandler

        self.angle = 0
        self.direction = pygame.Vector2(0, -1)
        self.position = pygame.Vector2(400, 400)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)

        self.fuel = config.starting_fuel
        self.fuelBar = Gauge(self.fuel, self)
        self.fuelBar.add(self.groups())

    def update(self, deltaTime):
        """Updates player velocity and position based on input.
        deltatime is time since last update"""
        # inputs
        keys = self.inputHandler.getPressed()
        right = keys[self.keymap["right"]]
        left = keys[self.keymap["left"]]
        thrust = keys[self.keymap["thrust"]]
        shoot = keys[self.keymap["shoot"]]

        if shoot:
            self.shoot()
        self.acceleration = (0,0)
        self.updateRotation(left, right, deltaTime)
        self.updateThrust(thrust, deltaTime)
        
        # apply gravity and update velocity vector
        self.acceleration += config.gravity*deltaTime
        self.velocity += self.acceleration*deltaTime
        if self.velocity.length() > config.max_speed:
            self.velocity.scale_to_length(config.max_speed)

        # update position
        self.position += self.velocity*deltaTime
        self.position.x %= config.screen_res[0]
        self.position.y %= config.screen_res[1]
        self.rect.center = self.position

        # check for collisions
        self.checkForCollisions()


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
            self.fuel -= thrust
            self.acceleration += self.direction * thrust * config.player_thrust*deltaTime

    def shoot(self):
        Bullet(self, config.player_color[self.id], self.groups())

    
    def checkForCollisions(self):
        hitList = pygame.sprite.spritecollide(self, self.groups()[0], False)
        for other in hitList:
            if type(other) is Bullet:
                self.killForReal()

    def killForReal(self):
        Player(self.id, self.inputHandler, self.groups())
        self.fuelBar.kill()
        self.kill()