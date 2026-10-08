import pygame

def inicializa():
    pygame.init()
    assets = {'assets/img/playerShip1_orange.png'}
    janela = pygame.display.set_mode((300,200))
    pygame.display.set_caption('Jogo do Felipe')
    return janela,assets
def recebe_eventos():
    game = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            return game
    return game
def desenha(window):
    janela = window.fill((0,0,0))
    pygame.display.update()
    return janela
def game_loop(assets):
    print(assets)
    game = True
    while game:
        game = recebe_eventos()
        if game == False:
            break
        tela = desenha(assets)

