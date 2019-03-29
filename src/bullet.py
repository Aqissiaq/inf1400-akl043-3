import pygame
import config

class Bullet(pygame.sprite.Sprite):

    def __init__(self, parent, color=(0,0,255), *groups):
        super().__init__(groups)

        self.parent = parent
        self.color = color

        self.image = pygame.image.load("assets/cohete_bw.png")
        self.image = pygame.transform.scale(self.image, (5, 10))
        self.image = pygame.transform.rotate(self.image, parent.angle)
        self.image.fill(self.color, special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect()
        
        self.position = pygame.Vector2(parent.position + (config.player_size[1]+5)*parent.direction)
        self.velocity = pygame.Vector2(parent.direction)*config.bullet_speed

    def update(self, deltaTime):
        self.position += self.velocity*deltaTime
        self.rect.center = self.position
        
        if(self.position.x < 0
            or self.position.x > config.screen_res[0]
            or self.position.y < 0
            or self.position.y > config.screen_res[1]):
            self.kill()

    def increaseScore(self, amount):
        self.parent.increaseScore(amount)