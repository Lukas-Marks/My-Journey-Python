import pygame


class Shoot(pygame.sprite.Sprite):
    
    numTiros = 0
    
    @staticmethod
    def somarTiros():
        Shoot.numTiros += 1
    
    @staticmethod    
    def subtrairTiros():
        Shoot.numTiros -= 1
    
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load("data/shot.png")
        self.image = pygame.transform.scale(self.image, [50,50])
        self.rect = self.image.get_rect()
        
        self.speed = 4
        Shoot.somarTiros()
        
    def update(self,*args):
        
        self.rect.x += self.speed
        
        if self.rect.left > 840:
            self.kill()
            Shoot.subtrairTiros()