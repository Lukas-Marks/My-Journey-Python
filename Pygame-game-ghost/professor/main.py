# Pygame:
# - Instalar a biblioteca no terminal: pip install pygame

# 1. IMPORTS --------------------------------------------------------------------------
import pygame

# do arquivo importe a Classe
from ghost import Ghost


# 2. INICIALIZAÇÃO --------------------------------------------------------------------

# 2.1 Iniciar o Pygame
pygame.init()

# 2.2 Iniciar a janela com a configuração de resolução de 840 x 480

# 2.2.1 Constantes de largura e altura da tela
LARGURA_TELA = 840
ALTURA_TELA = 480

# 2.2.2 Criar a janela (quadro)
display = pygame.display.set_mode([LARGURA_TELA, ALTURA_TELA])

# 2.2.3 Preencher o fundo da janela com cor RGB (red, green, blue)
# display.fill([235, 189, 52])

# 2.2.4 Preencher o fundo da janela com cor HEX (#123456)
display.fill('#ebbd34')

# 2.2.5 Mudar o títula da janela
pygame.display.set_caption("Game SENAI - Python 536")

# 2.2.6 Carregar uma imagem do icone e mudar o icone na janela
icone = pygame.image.load("data/icone.png")
pygame.display.set_icon(icone)

# 3. ELEMENTOS DE TELA ----------------------------------------------------------------

# 3.1 Personagens

# Criar um grupo de imagens para inserir todas as imagens e desenhar de uma unica vez
objectGroup = pygame.sprite.Group()

# Criar o personagem Fantasma
# - criar o objeto Sprite para carregar a imagem do fantasma e colocar no grupo de objetos
ghost = Ghost(objectGroup)

# 4. VARIÁVEIS GLOBAIS ----------------------------------------------------------------
gameLoop = True


# 4.1 Criar um clock para ajustar os frames por segundo (fps)
clock = pygame.time.Clock()



# 5. FUNÇÃO PRINCIPAL ------------------------------------------------------------------
def main():
    # Chamada das variáveis globais
    global gameLoop
    global clock

    # Game Loop
    while gameLoop:

        # Clock de 60fps
        clock.tick(60)

        # Event Loop - Verificar os eventos possíveis (click mouse, acionar tecla...)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            # 1. Tiros, pulos (1x)
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         print("Apertou a tecla W")

        
        # Repitar o fundo
        display.fill('#ebbd34')

        # Atualizar a posição dos elementos de tela
        objectGroup.update()

        # Desenhando os grupos na tela
        objectGroup.draw(display)

        pygame.display.update()

if __name__ == "__main__":
    main()
