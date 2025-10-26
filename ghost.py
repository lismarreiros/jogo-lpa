import pygame

class Ghost:
  def __init__(self, imagem, frame_size, posicao_inicial, velocidade=15, vida=100):
    self.imagem = imagem
    self.frame_size = frame_size
    self.anim_frame = 0
    self.anim_speed = 0.1
    self.direcao = "idle"
    self.x, self.y = posicao_inicial
    self.x_inicial = posicao_inicial[0]
    self.velocidade = velocidade
    # controla a direção do movimento: 1 para direita, -1 para esquerda
    self.direcao_movimento = 1
 
    self.vida = vida
    self.vivo = True
    self.forca = 10

    self.estado = "idle"

  def levar_dano(self, dano):
    self.vida -= dano
    if self.vida <= 0:
        self.vivo = False
        self.estado = "dead"
    else:
        self.estado = "hit"

  def atualizar(self, delta_time):
    total_frames = self.imagem.get_width() // self.frame_size[0]
    self.anim_frame += self.anim_speed
    if self.anim_frame >= total_frames:
      self.anim_frame = 0

    movimento = self.velocidade * self.direcao_movimento * (delta_time / 1000)
    self.x += movimento 
    
    # se bateu na borda direita da tela, inverte a direção
    if self.x > 690:
      self.x = 690
      self.direcao_movimento = -1  
    elif self.x <= self.x_inicial:
      self.x = self.x_inicial
      self.direcao_movimento = 1


  def get_frame(self, frame_index):
    frame_width, frame_height = self.frame_size
    rect = pygame.Rect(frame_index * frame_width, 0, frame_width, frame_height)
    return self.imagem.subsurface(rect)

  def desenhar(self, tela, scale = 1.5):
    frame = pygame.transform.scale(self.get_frame(int(self.anim_frame)), (self.frame_size[0]*scale, self.frame_size[1]*scale))
    tela.blit(frame, (self.x, self.y))
