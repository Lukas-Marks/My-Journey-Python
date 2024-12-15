import pygame
LarguraTela = 840
Altura = 480

#Ghost herda as caracteristicas e funcionalidade da classe sprite do Pygame
class Ghost(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        
        self.image = pygame.image.load("data/ghost-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedY = 0
        self.accelerationY = 0.25

    def update(self, *args):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speedY -= self.accelerationY
        elif keys[pygame.K_s]:
            self.speedY += self.accelerationY
        else:
            self.speedY *= 0.95

        self.rect.y += self.speedY

        # Definir os limites de tela
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedY = 0
        elif self.rect.bottom > Altura:
            self.rect.bottom = Altura
            self.speedY = 0