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
imagem_ghost_machucado = pygame.image.load("./imagens/ghost/ghostHurt-Sheet.png").convert_alpha() 
imagem_ghost_morto = pygame.image.load("./imagens/ghost/ghostDead-Sheet.png").convert_alpha()
posicao_inicial_ghost = (400, 348)
frame_size_ghost = (32, 32)
ghost1 = ghost.Ghost(imagem_ghost, frame_size_ghost, imagem_ghost_machucado, imagem_ghost_morto, posicao_inicial_ghost)

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

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                if reaper1.vivo:
                    reaper1.atacar()
                    som_espada.play()

    teclas = pygame.key.get_pressed()  # pega o estado de todas as teclas do teclado
    if reaper1.estado != "attacking":  # se nao estiver atacando, pode se mover
        reaper1.estado = "idle"  # assume que esta parado
   
    if teclas[pygame.K_RIGHT]:
        reaper1.mover("right", delta_time)
        reaper1.estado = "moving"
        reaper1.direcao = "right"
    elif teclas[pygame.K_LEFT]:
        reaper1.mover("left", delta_time)
        reaper1.estado = "moving"
        reaper1.direcao = "left"

    # atualização dos estados e posições
    reaper1.atualizar(delta_time)
    ghost1.atualizar(delta_time)

    # verificação de colisão
    reaper_rect = reaper1.rect.copy()
    reaper_rect.width *= 0.5  # reduz a largura do retangulo de colisao pela metade
    reaper_rect.height *= 0.8  # reduz a altura do retangulo de colisao
    ghost_rect = ghost1.rect.copy()
    ghost_rect.width *= 0.5
    ghost_rect.height *= 0.8

    # lófica de ataque e dano
        # --- Lógica de ataque e dano ---
    # a) Reaper ataca o Ghost
    if reaper1.vivo and ghost1.vivo and reaper1.estado == "attacking":
        if reaper_rect.colliderect(ghost_rect):
            if ghost1.vivo:
                ghost1.levar_dano(reaper1.forca)
                print(f"🗡️ Reaper atacou o Ghost! Vida do Ghost: {ghost1.vida}")
                # muda sprite para "hurt"
                ghost1.estado = "hurt"
            if not ghost1.vivo:
                ghost1.estado = "dead"
                print("👻 Ghost morreu!")

    # b) Ghost ataca o Reaper
    if reaper1.vivo and ghost1.vivo and reaper1.estado != "attacking":
        if ghost_rect.colliderect(reaper_rect):
            if ghost1.pode_atacar() and not reaper1.invulneravel:
                ghost1.registrar_ataque()
                reaper1.levar_dano(ghost1.forca)
                reaper1.invulneravel = True
                reaper1.tempo_desde_dano = pygame.time.get_ticks()
                print(f"💥 Ghost atacou o Reaper! Vida do Reaper: {reaper1.vida}")

    if reaper1.vivo == False:
        print("Reaper morreu! Fim de jogo.")
    
    # desenha elementos na tela e atualiza ela
    tela.blit(imagem_mapa, (0, 0))
    tela.blit(menuzinho, (10, 10))
    tela.blit(text_surface, (20, 20))
   
    reaper1.desenhar(tela)
    ghost1.desenhar(tela)

    pygame.display.flip()  # atualiza/exibe o conteudo da tela
