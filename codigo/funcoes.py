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
    assets['x'] = largura//2
    assets['y'] = altura//2
    assets['vx'] = 0
    assets['vy'] = 0
    assets['t0'] = pygame.time.get_ticks()#conta o tempo a partir do pygame.init()
    assets['fps'] = 0
    for i in range(40):
        x = random.randint(1, largura-1)
        y = random.randint(1,altura-1)
        raio = random.randint(1, 3)
        assets['estrelas'].append([x, y, raio])
    pygame.display.set_caption('Jogo do Felipe')
    return janela,assets
def recebe_eventos(assets):
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN: # se for uma tecla de  pressionar
            if event.key == pygame.K_RIGHT:
                assets['vx'] = 200
            if event.key == pygame.K_LEFT:
                assets['vx'] = -200
            if event.key == pygame.K_UP:
                assets['vy'] = -200
            if event.key == pygame.K_DOWN:
                assets['vy'] = 200
        if event.type == pygame.KEYUP:  # solta a tecla , ou seja antes voce tava pressionando agora ta soltando ela
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                assets['vx'] = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                assets['vy'] = 0
    return game
def desenha(window,assets):
    window.blit(assets['fundo'], (0, 0))
    for estrela in assets['estrelas']:
        pygame.draw.circle(window,(255, 255, 255),(estrela[0], estrela[1]),estrela[2])#pygame.draw.circle(janela, cor, centro, raio)
    window.blit(assets['nave'],(assets['x'],assets['y']))#atualizei para x e y de assets para sincronizar
    fonte=pygame.font.Font('assets/font/PressStart2P.ttf',15)
    coracoes = fonte.render(chr(9829)*3,True,'red') #fonte.render -->cria imagem a partir de um texto chr(9829) é os coraçoes , anti aliasing , cor
    window.blit(coracoes, (10,10))
    fps = fonte.render(str(int(assets['fps'])), True,'white')
    window.blit(fps, (largura-50,altura-30))
    pygame.display.update()
def game_loop(window,assets):
    game = True
    while game:
        game = recebe_eventos(assets)
        if game == False:
            break
        t1 = pygame.time.get_ticks()
        delta_t = t1 - assets['t0']
        assets['t0'] = t1#atualiza o tempo de referencia para o proximo calculo , ou seja delta seria t1(novo) - t1(anterior)
        if delta_t > 0:#divisao por zero ferra tudo
            assets['fps'] = 1000 / delta_t
        #velocidade
        #breve explicação: o game funciona em um looping e o delta_t calcula o tempo de cada looping e a diferença entre dois deles , assim quando eu por exemplo apertar a tecla para andar para a direita ele faz o loop e calcula o delta t e multiplica pela velocidade que seria vx ou vy, e multiplica por ela dando k pixels, e soma a posicao. quando eu parar de pressionar a tecla a velocidade vai para 0 e eu paro de movimentar.
        assets['x'] += assets['vx'] * delta_t / 1000
        assets['y'] += assets['vy'] * delta_t / 1000
        tela = desenha(window,assets)
        

