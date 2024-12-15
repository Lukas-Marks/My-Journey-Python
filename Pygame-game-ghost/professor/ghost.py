import pygame

LARGURA_TELA = 840
ALTURA_TELA = 480

# classe Ghost herdar as características e funcionalidade da classe Sprite do PyGame
class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        # - carregar a imagem para uso
        self.image = pygame.image.load("data/ghost-x4.gif")
        # - redimensionar a imagem para ocupar um retangulo em 100% 
        self.image = pygame.transform.scale(self.image, [100, 100])
        # - ajustado o retangulo na tela (left, top, width, heigth)
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speedY = 0
        self.accelerationY = 0.1


    def update(self, *args):

        # 2. Movimentação (nx)
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
        elif self.rect.bottom > ALTURA_TELA:
            self.rect.bottom = ALTURA_TELA
            self.speedY = 0

