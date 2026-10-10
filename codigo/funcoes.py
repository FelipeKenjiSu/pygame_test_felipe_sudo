import pygame
import random

def inicializa():
    pygame.init()
    assets = {}
    assets['fundo'] = pygame.image.load('assets/img/starfield.png')
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    assets['fundo'] = pygame.transform.scale(assets['fundo'], (800, 600))
    assets['nave'] = pygame.transform.scale(assets['nave'], (50, 40))
    janela = pygame.display.set_mode((800,600))
    assets['estrelas'] = []
    for i in range(40):
        x = random.randint(1, 799)
        y = random.randint(1, 599)
        raio = random.randint(1, 3)
    assets['estrelas'].append([x, y, raio])
    pygame.display.set_caption('Jogo do Felipe')
    return janela,assets
def recebe_eventos():
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            return game
    return game
def desenha(window,assets):
    window.blit(assets['fundo'], (0, 0))
    for estrela in assets['estrelas']:
        pygame.draw.circle(window,(255, 255, 255),(estrela[0], estrela[1]),estrela[2])#pygame.draw.circle(janela, cor, centro, raio)
    x = (800 -50)//2 
    y =(600- 40)//2   
    window.blit(assets['nave'],(x,y))
    pygame.display.update()
def game_loop(window,assets):
    game = True
    while game:
        game = recebe_eventos()
        if game == False:
            break
        tela = desenha(window,assets)

