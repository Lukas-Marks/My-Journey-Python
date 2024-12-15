import pygame
import random

class Bat(pygame.sprite.Sprite):
    
    numBatsOut = 0
    
    @staticmethod
    def somarBatsOut():
        Bat.numBatsOut += 1
        
    @staticmethod
    def restartBats():
        Bat.numBatsOut = 0        
        
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load("data/bat-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(900, 240, 100, 100)
        
        self.rect.x = 840 + random.randint(1,400)
        self.rect.y = 1 + random.randint(1,400)
        
        self.speed = 1 + random.random() * 2
        
    def update(self, *args):
        
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.somarBatsOut()
            self.kill()