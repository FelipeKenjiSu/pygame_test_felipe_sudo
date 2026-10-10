from funcoes import *
import pygame

def jogo():
    janela, assets = inicializa()
    game_loop(janela, assets)
    pygame.quit()
jogo()