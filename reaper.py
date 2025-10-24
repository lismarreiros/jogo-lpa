import pygame

class Reaper:
  def __init__(self, imagem, frame_size, pos_inicial, velocidade=5, vida=100):
    self.imagem = imagem
    self.frame_size = frame_size
    self.anim_frame = 0
    self.anim_speed = 0.1
    self.direcao = "idle"

    self.x, self.y = pos_inicial
    self.velocidade = velocidade
    self.dx = 0
    self.dy = 0

    self.vida = vida
    self.vivo = True
    self.forca = 10

    self.estado = "idle"
    self.cooldown_ataque = 500
    self.tempo_desde_ataque = 0

  def mover(self, direcao):
    if direcao == "left":
      self.x -= self.velocidade
    elif direcao == "right":
      self.x += self.velocidade
    elif direcao == "up":
      self.y -= self.velocidade
    elif direcao == "down":
      self.y += self.velocidade
    self.direcao = direcao
    self.estado = "moving"

  def atacar(self):
    if self.tempo_desde_ataque >= self.cooldown_ataque:
      print("Reaper atacou!")
      self.estado = "attacking"
      self.tempo_desde_ataque = 0

  def levar_dano(self, dano):
    self.vida -= dano
    if self.vida <= 0:
        self.vivo = False
        self.estado = "dead"
    else:
        self.estado = "hit"

  def atualizar(self, delta_time):
    self.tempo_desde_ataque += delta_time
    total_frames = self.imagem.get_width() // self.frame_size[0]
    self.anim_frame += self.anim_speed
    if self.anim_frame >= total_frames:
      self.anim_frame = 0

  def get_frame(self, frame_index):
    frame_width, frame_height = self.frame_size
    rect = pygame.Rect(frame_index * frame_width, 0, frame_width, frame_height)
    return self.imagem.subsurface(rect)

  def desenhar(self, tela, scale = 2):
    frame = pygame.transform.scale(self.get_frame(int(self.anim_frame)), (self.frame_size[0]*scale, self.frame_size[1]*scale))
    tela.blit(frame, (self.x, self.y))
