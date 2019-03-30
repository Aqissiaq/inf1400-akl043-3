import pygame

class Explosion(pygame.sprite.Sprite):

    def __init__(self, position, *groups):
        super().__init__(groups)

        self.image = pygame.image.load("assets/explosion.png")
        self.originalSize = (100, 100)
        self.image = pygame.transform.scale(self.image, self.originalSize)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
    
    def update(self, deltaTime):
        self.rect.inflate_ip(-2, -2)
        if self.rect.width <= 0:
            self.kill()
            return
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.rect.center = self.position