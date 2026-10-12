import pygame
import random
largura = 800
altura = 600
#sprite é um objeto de jogo que segue o padrão do Pygame.
class Nave(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)#inicializa a parte de sprite do Pygame
        self.image = assets['nave']
        self.rect = self.image.get_rect()
        self.rect.x = largura//2
        self.rect.y = altura//2
        self.vx = 0
        self.vy = 0
    def atualiza_posicao(self, delta_t):
        self.rect.x= self.rect.x +self.vx*delta_t/ 1000
        self.rect.y=self.rect.y +self.vy*delta_t /1000

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['meteoro']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, largura-51)
        self.rect.y = random.randint(1, altura//4)
        self.vy = 300
    def atualiza_posicao(self, delta_t):
        self.rect.y=self.rect.y +self.vy*delta_t /1000
        if self.rect.y>altura:
            self.rect.y=-50
            self.rect.x=random.randint(0,largura-50)

class TelaInicial:
    def __init__(self, window):
        self.window = window
        self.fonte = pygame.font.Font('assets/font/PressStart2P.ttf', 20)
    def desenha(self):
        self.window.fill((0, 0, 0))
        mensagem =self.fonte.render('Pressione qualquer tecla', True,'white')
        mensagem2= self.fonte.render('para comecar', True,'white')
        sair =self.fonte.render('Q para sair', True,'white')
        self.window.blit(mensagem,(largura//4,altura//3))
        self.window.blit(mensagem2,(largura//4,altura//3+40))
        self.window.blit(sair,(largura//4,altura//3+80))
        pygame.display.update()
    def recebe_eventos(self):
        # 'sair':acaba
        # 'jogar':começa
        # 'inicio':continuar na tela inicial
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'sair'
            if event.type == pygame.KEYDOWN:#tecla pressionada
                if event.key == pygame.K_q:
                    return 'sair'
                else:
                    return 'jogar'
class TelaGameOver:
    def __init__(self, window):
        self.window = window
        self.fonte = pygame.font.Font('assets/font/PressStart2P.ttf', 20)
    def desenha(self):
        self.window.fill((0, 0, 0))
        titulo= self.fonte.render('Game Over', True,'white')
        mensagem= self.fonte.render('Pressione qualquer tecla', True,'white')
        mensagem2= self.fonte.render('para jogar novamente',True,'white')
        sair =self.fonte.render('Q para sair', True,'white')
        self.window.blit(titulo, (largura//4,altura//3))
        self.window.blit(mensagem, (largura//4,altura//3+40))
        self.window.blit(mensagem2, (largura//4, altura//3+80))
        self.window.blit(sair, (largura//4,altura//3+120 ))
        pygame.display.update()

    def recebe_eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'sair'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return 'sair'
                else:
                    return 'jogar'#jogar = comelar novo jogo
class TelaJogo:
    def __init__(self, window, assets):#cria as configs do zero para o proximo loop, no caso do jogador perder ou reiniciar ou qlq que seja o motivo, cria um novo jogo com os stats zerados.
        self.window = window
        self.assets = assets
        self.assets['vidas'] = 3
        self.assets['nave_obj'] = Nave(assets)#configura imagem,retangulo,posição inicial e velocidades zeradas
        self.assets['nave_grupo'] = pygame.sprite.Group()
        self.assets['nave_grupo'].add(self.assets['nave_obj'])
        self.assets['meteoros'] = pygame.sprite.Group()
        for i in range(5):
            meteoro = Meteoro(assets)
            self.assets['meteoros'].add(meteoro)
        self.assets['t0']=pygame.time.get_ticks() #guarda o tempo atual , para calcular o proximo delta t , para nao quebrar a mecanica de fps e outras tb.
    def executar(self):#roda a partida até ela acabar.
        return game_loop(self.window, self.assets)#game looop = responsavel por movimento,mostrar fundo estrelas e etc calcual delta t tb.
class Jogo:
    def __init__(self):
        self.window, self.assets = inicializa()#recebe a tupla de inicializa (window,assets),primeiro indice vai para window e o segundo vai para assets
        self.tela = TelaInicial(self.window)
        self.estado = 'inicio'
    def executar(self):
#         acao = self.tela.recebe_eventos()
#         self.tela objeto da tela atual,  exemplo TelaInicial.
# .recebe_eventos() executa o método dessa tela que verifica teclado e clique no X de sair
# acao : guarda o valor devolvido pelo return dessas coisas.
        while True:
            if self.estado == 'jogo':
                acao = self.tela.executar()
            else:
                self.tela.desenha()
                acao= self.tela.recebe_eventos()
            if acao=='sair':
                break
            if acao =='jogar':
                self.tela=TelaJogo(self.window, self.assets)#tela do jogo
                self.estado='jogo'
            if acao == 'gameover':
                self.tela=TelaGameOver(self.window)
                self.estado='gameover'
        pygame.quit()
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
    assets['nave_obj'] = Nave(assets)
    assets['nave_grupo'] = pygame.sprite.Group()
    assets['nave_grupo'].add(assets['nave_obj'])
    assets['meteoro'] =pygame.transform.scale(assets['meteoro'], (50, 50))
    janela = pygame.display.set_mode((largura,altura))
    assets['som_tiro'] = pygame.mixer.Sound('assets/snd/pew.wav')
    assets['som_tiro'].set_volume(0.15)
    assets['estrelas']= []
    assets['vidas'] = 3
    assets['t0']=pygame.time.get_ticks()#conta o tempo a partir do pygame.init()
    assets['fps'] = 0
    for i in range(40):
        x =random.randint(1, largura-1)
        y =random.randint(1,altura-1)
        raio= random.randint(1, 3)
        assets['estrelas'].append([x, y, raio])
    assets['meteoros']= pygame.sprite.Group()
    for i in range(5):
        meteoro = Meteoro(assets)
        assets['meteoros'].add(meteoro)
    pygame.display.set_caption('Jogo do Felipe')
    return janela,assets
def recebe_eventos(assets):
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN: # se for uma tecla de  pressionar
            if event.key == pygame.K_RIGHT:
                assets['nave_obj'].vx = 350
            if event.key == pygame.K_LEFT:
                assets['nave_obj'].vx = -350
            if event.key == pygame.K_UP:
                assets['nave_obj'].vy = -350
            if event.key == pygame.K_DOWN:
                assets['nave_obj'].vy = 350
            if event.key == pygame.K_SPACE:
                assets['som_tiro'].play()
        if event.type == pygame.KEYUP:  # solta a tecla , ou seja antes voce tava pressionando agora ta soltando ela
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                assets['nave_obj'].vx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                assets['nave_obj'].vy = 0
    return game
def desenha(window,assets):
    window.blit(assets['fundo'], (0, 0))
    for estrela in assets['estrelas']:
        pygame.draw.circle(window,(255, 255, 255),(estrela[0], estrela[1]),estrela[2])#pygame.draw.circle(janela, cor, centro, raio)
        #antes
    # for meteoro in assets['meteoros']:
    #     window.blit(meteoro.image,meteoro.rect)
        #depois
    assets['meteoros'].draw(window)
    window.blit(assets['nave_obj'].image, assets['nave_obj'].rect)#atualizei para x e y de assets para sincronizar
    fonte=pygame.font.Font('assets/font/PressStart2P.ttf',15)
    coracoes = fonte.render(chr(9829)*assets['vidas'],True,'red') #fonte.render -->cria imagem a partir de um texto chr(9829) é os coraçoes , anti aliasing , cor
    window.blit(coracoes, (10,10))
    fps = fonte.render(str(int(assets['fps'])), True,'white')
    window.blit(fps, (largura-50,altura-30))
    pygame.display.update()
def game_loop(window,assets):
    game =True
    while game:
        game = recebe_eventos(assets)
        if game == False:
            return 'sair'
        t1 =pygame.time.get_ticks()
        delta_t =t1 -assets['t0']
        assets['t0']= t1#atualiza o tempo de referencia para o proximo calculo , ou seja delta seria t1(novo) - t1(anterior)
        if delta_t >0:#divisao por zero ferra tudo
            assets['fps']=1000/delta_t
        #velocidade
        #breve explicação: o game funciona em um looping e o delta_t calcula o tempo de cada looping e a diferença entre dois deles , assim quando eu por exemplo apertar a tecla para andar para a direita ele faz o loop e calcula o delta t e multiplica pela velocidade que seria vx ou vy, e multiplica por ela dando k pixels, e soma a posicao. quando eu parar de pressionar a tecla a velocidade vai para 0 e eu paro de movimentar.
        assets['nave_obj'].atualiza_posicao(delta_t)
        #breve explicacao
        # Rect cria a área invisível de colisão dos objetos
        # colliderect verifica se a área da nave bateu na área do meteoro
        # Se bater, tira uma vida e reposiciona o meteoro
        for dados_meteoro in assets['meteoros']:
            dados_meteoro.atualiza_posicao(delta_t)#atualiza o meteoro: faz ele descer e voltar para cima quando sai da tela, criei um método para isso.
        colisoes = pygame.sprite.groupcollide(assets['nave_grupo'],assets['meteoros'],False,False)
            #verifica colisão entre o grupo da nave e o grupo dos meteoros
            #os False fazem com que nave e meteoros não sejam removidos automaticamente
        for nave in colisoes:
            for meteoro in colisoes[nave]:
                assets['vidas']= assets['vidas']-1
                meteoro.rect.y=-50
                meteoro.rect.x=random.randint(0,largura-51)
        if assets['vidas'] <=0:
            return 'gameover'
        tela = desenha(window,assets)
        

