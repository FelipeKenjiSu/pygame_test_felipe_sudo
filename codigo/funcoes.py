import pygame
import random
largura = 800
altura = 600
def inicializa():
    pygame.init()
    assets = {}
    assets['fundo'] = pygame.image.load('assets/img/starfield.png')
    assets['nave'] = pygame.image.load('assets/img/playerShip1_orange.png')
    assets['fundo'] = pygame.transform.scale(assets['fundo'], (largura,altura))
    assets['nave'] = pygame.transform.scale(assets['nave'], (50, 40))
    janela = pygame.display.set_mode((largura,altura))
    assets['estrelas'] = []
    assets['t0'] = pygame.time.get_ticks()#conta o tempo a partir do pygame.init()
    assets['fps'] = 0
    for i in range(40):
        x = random.randint(1, largura-1)
        y = random.randint(1,altura-1)
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
    x = (largura -50)//2 
    y =(altura- 40)//2   
    window.blit ( assets['nave'], (x,y))
    fonte=pygame.font.Font('assets/font/PressStart2P.ttf',15)
    coracoes = fonte.render(chr(9829)*3,True,'red') #fonte.render -->cria imagem a partir de um texto chr(9829) é os coraçoes , anti aliasing , cor
    window.blit(coracoes, (10,10))
    fps = fonte.render(str(int(assets['fps'])), True,'white')
    window.blit(fps, (largura-50,altura-30))
    pygame.display.update()
def game_loop(window,assets):
    game = True
    while game:
        game = recebe_eventos()
        if game == False:
            break
        t1 = pygame.time.get_ticks()
        delta_t = t1 - assets['t0']
        assets['t0'] = t1#atualiza o tempo de referencia para o proximo calculo , ou seja delta seria t1(novo) - t1(anterior)
        if delta_t > 0:#divisao por zero ferra tudo
            assets['fps'] = 1000 / delta_t
        tela = desenha(window,assets)
        

