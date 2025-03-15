import pygame
import random

from constants import *

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3,3)
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)