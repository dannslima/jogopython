import pygame
from random import randint
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption('Criando um Jogo em Python - Danilo Vasconcelos')

x =280  # max 460 -- min 110
y = 150
pos_x = 300
pos_y =  800
pos_y_a = 800
pos_y_c = 800


velocidade = 15
velocidadeoutros = 20
carro = pygame.image.load('carro.png')
fundo = pygame.image.load('fundo.png')
policia = pygame.image.load('carpol.png')
carrobranco = pygame.image.load('carrobranco.png')
carroamarelo = pygame.image.load('carpol.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render('Tempo: ', True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

janela_aberta= True
while janela_aberta:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()


    if comandos[pygame.K_RIGHT] and x <=460:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >=110:
        x -= velocidade

    if (pos_y <= -180) and (pos_y_a <=180) and (pos_y_c <= -180):
        pos_y =  randint(800,1200)
        pos_y_a = randint(800,1200)
        pos_y_c = randint(800,1200)

    pos_y -= velocidadeoutros
    pos_y_a -= velocidadeoutros + 2
    pos_y_c -= velocidadeoutros + 10 #carro policia


    janela.fill((0,0,0))
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(carrobranco,(pos_x,pos_y))
    janela.blit(policia,(pos_x + 160,pos_y_a))
    janela.blit(carroamarelo,(pos_x - 140 , pos_y_c))
    janela.blit(texto,pos_texto)
    pygame.display.update()

pygame.quit()
