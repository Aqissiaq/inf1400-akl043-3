import pygame
import config
from terrain import Terrain

class Bullet(pygame.sprite.Sprite):
    """
    This class is for bullets shot by either player.
    The parent argument should be the shooting player to attribute score
    """
    def __init__(self, parent, color=(0,0,255), *groups):
        super().__init__(groups)

        self.parent = parent
        self.color = color

        self.image = pygame.image.load("assets/cohete_bw.png")
        self.image = pygame.transform.scale(self.image, (10, 20))
        self.image = pygame.transform.rotate(self.image, parent.angle)
        self.image.fill(self.color, special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect()
        
        self.position = pygame.Vector2(parent.position + (config.player_size[1]+5)*parent.direction)
        self.velocity = pygame.Vector2(parent.direction)*config.bullet_speed
        self.rect.center = self.position

        self.killed = False

    def update(self, deltaTime):
        """Moves the bullet"""
        self.checkForTerrainCollision()
        if self.killed:
            self.kill()
        self.position += self.velocity*deltaTime
        self.rect.center = self.position
        self.position.x %= config.screen_res[0]
        self.position.y %= config.screen_res[1]


    def increaseScore(self, amount):
        self.parent.increaseScore(amount)

    def checkForTerrainCollision(self):
        """Helper function to handle collisions with terrain"""
        if(self.groups()):
            hitlist = pygame.sprite.spritecollide(self, self.groups()[0], False)
            for other in hitlist:
                if type(other) is Terrain:
                    self.killed = True