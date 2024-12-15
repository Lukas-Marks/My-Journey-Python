#Imports----------------------------------------------------
import pygame
from ghost import Ghost
from bat import Bat
import random
from shoot import Shoot
from zumbi import Zumbi

#Inicialização-----------------------------------------------
#INICIAR PYGAME
pygame.init()

#iniciar a janela com a configuração de resolução de 840x480

#constante de altura e largura
LarguraTela = 840
AlturaTela = 480

#criar janela
display = pygame.display.set_mode([LarguraTela,AlturaTela])

display.fill('#bcdefe')
#preencher o fundo

pygame.display.set_caption("Game Python Ghost")
#alterar titulo da janela

icone = pygame.image.load("Data\icone.png")
#carrega a imagem

pygame.display.set_icon(icone)
#carregar a imagem do icone



#Elementos de tela --------------------------------------------

#Personagens
#Criar um grupo de imagens para inserir todas as imagens e desenhar de uma unica vez
objectGroup = pygame.sprite.Group()
batGroup = pygame.sprite.Group()
shootGroup = pygame.sprite.Group()

bg = pygame.sprite.Sprite(objectGroup)
bg.image = pygame.image.load("data/bg2.jpg")
bg.image = pygame.transform.scale(bg.image, [840,480])
bg.rect = bg.image.get_rect()


ghost = Ghost(objectGroup)

# bat = Bat(objectGroup, batGroup)

#fontes
scoreFont = pygame.font.Font("data/Pixeltype.ttf", 50)
gameOver_font = pygame.font.Font("data/Pixeltype.ttf", 200)


#Musica

pygame.mixer.music.load("data/openMusic2.mp3")
pygame.mixer.music.play(-1)

#sound (SFX)

attack = pygame.mixer.Sound("data/magic1.wav")
gameOverSound = pygame.mixer.Sound("data\Production_Intro_Theme.wav")
#Variaveis globais --------------------------------------------
gameLoop = True
gameOver = False
timer = 20
pontos = 0
numFase = 1
batList = []

# 4.1 Criar um clock para ajustar os frames por segundo (fps)
clock = pygame.time.Clock()

#Funcao Principal ---------------------------------------------

def main():
    
    
    global gameLoop
    global gameOver
    global clock
    global timer
    global pontos
    global numFase

    while gameLoop:
        # Clock de 60fps
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
                
            # #1 ele capta apenas uma tecla por vez, mesmo se segurar a tela
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if Shoot.numTiros < 5:
                        newShoot = Shoot(objectGroup, shootGroup)
                        newShoot.rect.center = ghost.rect.center
                        attack.play()
                if event.key == pygame.K_r:
                    if gameOver == True:
                        gameOver = False
                        pontos = 0
                        numFase= 1
                        pygame.mixer.music.play(-1)
                        Bat.restartBats()
                        
                                
                    #event.key se ele captar uma tecla e a tecla for igual w ent: 
                
        if not gameOver:
            
            #repita o fundo
            display.fill('#bcdefe')
        
            timer += 1
            if timer > 30 and numFase == 1:
                timer = 0
                if random.random() < 0.45: 
                    newBat = Bat(objectGroup, batGroup)
                if random.random() < 0.25: 
                    newBat = Zumbi(objectGroup, batGroup)
            # Criar varios morcegos
            
            #colisão entre os morcegos com o fantasma
            colisao = pygame.sprite.spritecollide(
                ghost,
                batGroup,
                True,
                pygame.sprite.collide_mask
            )
            
            if colisao or Bat.numBatsOut >= 5:
                gameOver = True
                gameOverSound.play()
                pygame.mixer.music.stop()
                
                
            tiros = pygame.sprite.groupcollide(
                shootGroup,
                batGroup,
                True,
                True,
                pygame.sprite.collide_mask
            )
            if tiros: 
                pontos += 1
                print("Score: ", pontos)
                Shoot.subtrairTiros()
            
            if pontos >= 10:
                numFase = 2

            # Atualizar a posição dos elementos de tela
            objectGroup.update()
            

        #desenhando os grupos na tela
        objectGroup.draw(display)
        
        #Score
        scoreRender = scoreFont.render(f"Score: {pontos}", False, "white")
        display.blit(scoreRender, (650,50))
        
        #Mensagem game over
        if gameOver:
            gameOver_render = gameOver_font.render("Game Over", False, "White") 
            display.blit(gameOver_render, (100,150))
        pygame.display.update()
        

    
if __name__ == "__main__":
    main()