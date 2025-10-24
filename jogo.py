import pygame
import sys
import reaper  


pygame.init()  # inicializa os modulos do pygame
clock = pygame.time.Clock()  # cria um relogio para controlar o fps
# cenário
imagem_mapa = pygame.image.load("./imagens/mapa.png")  # carrega uma imagem em url relativa
tela = pygame.display.set_mode(size=(700, 500))  # cria uma tela com largura, altura
imagem_mapa = pygame.transform.scale(imagem_mapa, (700, 500))  # redimensiona a imagem

# reaper 
imagem_reaper = pygame.image.load("./imagens/reaper/PassiveIdleReaper-Sheet.png").convert_alpha()  # carrega uma imagem em url relativa
posicao_inicial_reaper = (100, 325)
frame_size_reaper = (48, 48)
reaper1 = reaper.Reaper(imagem_reaper, frame_size_reaper, posicao_inicial_reaper)


som_espada = pygame.mixer.Sound("./sons/espada.mp3")  # carrega um som, pode ser wav, ogg, mp3 etc.

# loop principal do jogo
while True:
    # delta time (quantos milisegundos se passaram desde o ultimo frame)
    delta_time = clock.tick(120)

    # verifica quais eventos estão acontecendo (teclado, mouse, etc)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # se o jogador clicou no X da janela
            pygame.quit()  # finaliza o pygame
            sys.exit()  # finaliza o programa


    # desenha elementos na tela e atualiza ela
    tela.blit(imagem_mapa, (0, 0)) 
    reaper1.atualizar(delta_time)
    reaper1.desenhar(tela)

    # if cacador_vida > 0:
    #     tela.blit(imagem_cacador, (cacador_x, cacador_y))  # desenha a imagem na tela na posicao x, y
    # if valdemir_esta_direita:
    #     tela.blit(imagem_valdemir_direita, (valdemir_x, valdemir_y))  # desenha a imagem na tela na posicao x, y
    # else:
    #     tela.blit(imagem_valdemir_esquerda, (valdemir_x, valdemir_y))  # desenha a imagem na tela na posicao x, y
        # pygame.display.flip()  # atualiza/exibe o conteudo da tela
    # if cacador_vida > 0:
    #     tela.blit(imagem_cacador, (cacador_x, cacador_y))  # desenha a imagem na tela na posicao x, y
    # if valdemir_esta_direita:
    #     tela.blit(imagem_valdemir_direita, (valdemir_x, valdemir_y))  # desenha a imagem na tela na posicao x, y
    # else:
    #     tela.blit(imagem_valdemir_esquerda, (valdemir_x, valdemir_y))  # desenha a imagem na tela na posicao x, y
    pygame.display.flip()  # atualiza/exibe o conteudo da tela
