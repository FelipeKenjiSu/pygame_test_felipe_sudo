import pygame
import random
largura = 800
altura = 600
def inicializa():
    pygame.init()
    pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(loops = -1)
    assets = {}
    assets['fundo']= pygame.image.load('assets/img/starfield.png')
    assets['nave'] =pygame.image.load('assets/img/playerShip1_orange.png')
    assets['meteoro'] = pygame.image.load('assets/img/meteorBrown_med1.png')
    assets['fundo']= pygame.transform.scale(assets['fundo'], (largura,altura))
    assets['nave']=pygame.transform.scale(assets['nave'], (50, 40))
    assets['meteoro'] =pygame.transform.scale(assets['meteoro'], (50, 50))
    janela = pygame.display.set_mode((largura,altura))
    assets['som_tiro'] = pygame.mixer.Sound('assets/snd/pew.wav')
    assets['som_tiro'].set_volume(0.15)
    assets['estrelas']= []
    assets['x'] =largura//2
    assets['y']= altura//2
    assets['vx']= 0
    assets['vy']= 0
    assets['vidas'] = 3
    assets['t0']=pygame.time.get_ticks()#conta o tempo a partir do pygame.init()
    assets['fps'] = 0
    for i in range(40):
        x =random.randint(1, largura-1)
        y =random.randint(1,altura-1)
        raio= random.randint(1, 3)
        assets['estrelas'].append([x, y, raio])
    assets['meteoros'] =[]
    for i in range(5):
        dados_meteoro ={'x':random.randint(1, largura-51),'y':random.randint(1, altura//4),'vy':100}
        assets['meteoros'].append(dados_meteoro)
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
            if event.key == pygame.K_SPACE:
                assets['som_tiro'].play()
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
    for dados_meteoro in assets['meteoros']:
        window.blit(assets['meteoro'], (dados_meteoro['x'],dados_meteoro['y']))
    window.blit(assets['nave'],(assets['x'],assets['y']))#atualizei para x e y de assets para sincronizar
    fonte=pygame.font.Font('assets/font/PressStart2P.ttf',15)
    coracoes = fonte.render(chr(9829)*assets['vidas'],True,'red') #fonte.render -->cria imagem a partir de um texto chr(9829) é os coraçoes , anti aliasing , cor
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
        assets['x']+=assets['vx']*delta_t / 1000
        assets['y']+=assets['vy']*delta_t / 1000
        #breve explicacao
        # Rect cria a área invisível de colisão dos objetos
        # colliderect verifica se a área da nave bateu na área do meteoro
        # Se bater, tira uma vida e reposiciona o meteoro
        for dados_meteoro in assets['meteoros']:
            dados_meteoro['y']+=dados_meteoro['vy']*delta_t/ 1000
            if dados_meteoro['y']>altura:
                dados_meteoro['y']=-50
                dados_meteoro['x']=random.randint(0,largura- 50)
            nave_rect=pygame.Rect(assets['x'],assets['y'],100,80)
            meteoro_rect=pygame.Rect(dados_meteoro['x'],dados_meteoro['y'],50,50)
            if nave_rect.colliderect(meteoro_rect):
                assets['vidas'] =assets['vidas'] - 1
                dados_meteoro['y']=-50
                dados_meteoro['x']=random.randint(0,largura- 50)
            if assets['vidas'] <=0:
                game = False
        tela = desenha(window,assets)
        

