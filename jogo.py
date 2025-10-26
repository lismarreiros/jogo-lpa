import pygame
import sys
import reaper  
import ghost

pygame.init()  # inicializa os modulos do pygame
clock = pygame.time.Clock()  # cria um relogio para controlar o fps
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50) 
# cenário
imagem_mapa = pygame.image.load("./imagens/mapa.png")
menuzinho = pygame.Surface((200,100))
menuzinho.fill((3, 22, 28))

# origin point (0,0) is top-left
tela = pygame.display.set_mode(size=(700, 500))  # cria uma tela com largura, altura
imagem_mapa = pygame.transform.scale(imagem_mapa, (700, 500))  # redimensiona a imagem
text_surface = test_font.render("Tanatos", True, (43, 100, 113)) 

# reaper - player
imagem_reaper_parado = pygame.image.load("./imagens/reaper/HostileIdleReaper-Sheet.png").convert_alpha() 
imagem_reaper_movendo = pygame.image.load("./imagens/reaper/HostileRunningReaper-Sheet.png").convert_alpha() 
imagem_reaper_atacando = pygame.image.load("./imagens/reaper/HostileAttackReaper-Sheet.png").convert_alpha()
posicao_inicial_reaper = (100, 325)
frame_size_reaper = (48, 48)
reaper1 = reaper.Reaper(imagem_reaper_parado, imagem_reaper_movendo, imagem_reaper_atacando, frame_size_reaper, posicao_inicial_reaper)

# ghost - enemy
imagem_ghost = pygame.image.load("./imagens/ghost/ghost-idle.png").convert_alpha()
posicao_inicial_ghost = (400, 348)
frame_size_ghost = (32, 32)
ghost1 = ghost.Ghost(imagem_ghost, frame_size_ghost, posicao_inicial_ghost)


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
    tela.blit(menuzinho, (10, 10))
    tela.blit(text_surface, (20, 20))
    reaper1.atualizar(delta_time)
    reaper1.desenhar(tela)
    ghost1.atualizar(delta_time)
    ghost1.desenhar(tela)

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
