# Checks de estudo de Pygame


Este é um projeto desenvolvido na disciplina Developer Life, do 1o semestre do curso de Ciência da Computação do Insper. O intuito deste projeto é aprender e praticar o uso da biblioteca Pygame para o desenvolvimento de jogos 2D usando Python.

## Descrição do jogo

[ADICIONE AQUI UMA DESCRIÇÃO DO JOGO]

## Como jogar

Para jogar, é necessário ter o Python 3 instalado na máquina. Além disso, você deve instalar a biblioteca pygame com o comando:

```
pip install pygame
```

Após instalar a biblioteca, clone este repositório e execute o arquivo jogo.py, dentro da pasta codigo. O jogo será aberto em uma nova janela e pode ser jogado com as seguintes teclas:

[ADICIONE AQUI AS INSTRUÇÕES DO JOGO]


## COMANDOS

Janela
pygame.init()
pygame.display.set_mode((largura, altura))
pygame.display.set_caption("título")
janela.fill((R, G, B))
pygame.display.update()
pygame.quit()
Relógio e tempo
relogio = pygame.time.Clock()
relogio.tick(60)
pygame.time.get_ticks()
Eventos
pygame.event.get()
event.type == pygame.QUIT
event.type == pygame.MOUSEBUTTONDOWN (event.pos)
pygame.key.get_pressed() (teclas[pygame.K_LEFT])
pygame.K_LEFT, K_RIGHT, K_UP, K_DOWN
Imagem
pygame.image.load("caminho.png")
pygame.transform.scale(imagem, (largura, altura))
janela.blit(imagem, (x, y))
Formas
pygame.draw.circle(janela, cor, (cx, cy), raio)
pygame.draw.rect(janela, cor, rect, espessura)
Texto
fonte = pygame.font.SysFont(None, tamanho)
superficie = fonte.render(str(valor), True, cor)
janela.blit(superficie, (x, y))
Rect e colisão
pygame.Rect(x, y, largura, altura)
rect1.colliderect(rect2)
rect.collidepoint(event.pos)
math.hypot(px - cx, py - cy) <= raio
Aleatório
from random import randint
randint(a, b)
Listas
lista.append(item)
lista.remove(item)
for item in lista[:]:

pygame.draw.rect(janela, cor, (x, y, largura, altura))
pygame.time.get_ticks()
janela.blit(imagem,cordenadas)
pygame.Rect(x, y, largura, altura)
pygame.font.SysFont(none(vira a padrão), tamanho)
              :
              V
fonte.render(texto, antialias, cor)
janela.blit(surface_do_texto, (x, y))

if ret_personagem.colliderect(ret_fruta):
   assets['pontos'] += 1

variavel.coliiderect(outro_ret):
## JOGO.PY
from funcoes import *
import pygame

def jogo():
    janela, assets = inicializa()
    game_loop(janela, assets)
    pygame.quit()
jogo()


## FUNCÃO INICIAL
import pygame


largura =


altura =


def inicializa():
    pygame.init()
    janela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("TITULO")
    assets = {}
    assets['cor_fundo'] = (25, 25, 25)
    assets['relogio'] = pygame.time.Clock()
    return janela, assets
def recebe_eventos():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def atualiza_estado(assets):
    pass

def desenha(janela, assets):
    janela.fill(assets['cor_fundo'])
    pygame.display.update()

def game_loop(janela, assets):
    rodando = True
    while rodando:
        assets['relogio'].tick(60)
        rodando = recebe_eventos()
        atualiza_estado(assets)
        desenha(janela, assets)
    pygame.quit()


## FUNCOES:

# movimentacao


    teclas = pygame.key.get_pressed()
    x_antigo = assets['cords_personagem'][0]
    y_antigo = assets['cords_personagem'][1]
    if teclas[pygame.K_UP]:
        assets['cords_personagem'][1] -= 5
    if teclas[pygame.K_DOWN]:
        assets['cords_personagem'][1] += 5
    if teclas[pygame.K_LEFT]:
        assets['cords_personagem'][0] -= 5
    if teclas[pygame.K_RIGHT]:
        assets['cords_personagem'][0] += 5
    if assets['cords_personagem'][0]>largura-x_personagem or assets['cords_personagem'][0]<0 :
        assets['cords_personagem'][0] = x_antigo
    if assets['cords_personagem'][1]>altura-y_personagem or assets['cords_personagem'][1]<0 :
        assets['cords_personagem'][1] = y_antigo



# colisão

def verifica_colisoes(ret_jogador, ret_objetos):
    indices = []

    for i in range(len(ret_objetos)):
        if ret_jogador.colliderect(ret_objetos[i]):
            indices.append(i)

    return índices

índices daqueles que colidiram(personagem e maça , ele retorna as maças que o personagem coletou).

# temporizador

  na inicializa
intervalo = 3000                      # y segundos x 1000
ultimo = pygame.time.get_ticks()      # instante da última vez

  na gameloop (roda a cada frame)
agora = pygame.time.get_ticks()
if agora - ultimo >= intervalo:
    # faça a coisa (x) aqui
    ultimo = agora                    # reinicia a contagem

