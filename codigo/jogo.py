from codigo.funcoes import *
import pygame
pygame.init()
def jogo():
    janela = inicializa()
    return game_loop(janela)
print(jogo())