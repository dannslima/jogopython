

import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Criando um Jogo')

x =400
y = 300
velocidade = 5
carro = pygame.image.load('carro.png')
fundo = pygame.image.load('fundo.png')
janela_aberta= True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade


    janela.fill((0,0,0))
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    pygame.display.update()

pygame.quit()