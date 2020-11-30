

import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Criando um Jogo')

x =440
y = 200
pos_x = 300
pos_y =  200
velocidade = 10
velocidadeoutros = 15
carro = pygame.image.load('carro.png')
fundo = pygame.image.load('fundo.png')
policia = pygame.image.load('carpol.png')
carrobranco = pygame.image.load('carrobranco.png')



janela_aberta= True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()

   # if comandos[pygame.K_UP]:
      #  y -= velocidade
   # if comandos[pygame.K_DOWN]:
     #   y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade

    if (pos_y <= -200):
        pos_y =  600

    pos_y -= velocidadeoutros


    janela.fill((0,0,0))
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carrobranco,(pos_x,pos_y))
    janela.blit(policia,(150,pos_y))
    pygame.display.update()

pygame.quit()