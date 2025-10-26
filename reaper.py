import pygame

class Reaper:
  def __init__(self, imagem_parado, imagem_movendo, imagem_atacando, frame_size, pos_inicial, velocidade=5, vida=100):
    self.frame_size = frame_size
    self.anim_frame = 0
    self.anim_speed = 0.1
    self.direcao = "right"
    self.estado = "idle"
    self.sprites = {
      "idle": imagem_parado,
      "moving": imagem_movendo,
      "attacking": imagem_atacando,
    }

    self.x, self.y = pos_inicial
    self.velocidade = velocidade
    self.rect = pygame.Rect(self.x, self.y, frame_size[0], frame_size[1])

    self.vida = vida
    self.vivo = True
    self.forca = 10

    self.cooldown_ataque = 800  # tempo entre ataques
    self.duracao_ataque = 400   # tempo da animação do golpe
    self.tempo_ataque_iniciado = 0

    self.invulneravel = False
    self.tempo_invulneravel = 1000
    self.tempo_ultimo_dano = 0
    self.alpha = 255

  def mover(self, direcao, delta_time):
    deslocamento = self.velocidade * (delta_time / 16)
    if direcao == "right":
      self.x += deslocamento
      self.direcao = "right"
    elif direcao == "left":
      self.x -= deslocamento
      self.direcao = "left"

    self.rect.x = int(self.x)
    if self.estado != "attacking":
      self.estado = "moving"

  def atacar(self):
    tempo_atual = pygame.time.get_ticks()
    if tempo_atual - self.tempo_ataque_iniciado >= self.cooldown_ataque:
      self.estado = "attacking"
      self.tempo_ataque_iniciado = tempo_atual
      print("🗡️ Reaper iniciou ataque")

  def levar_dano(self, dano):
    if not self.invulneravel:
      self.vida -= dano
      print(f"💥 Reaper levou {dano} de dano! Vida restante: {self.vida}")
      self.invulneravel = True
      self.tempo_ultimo_dano = pygame.time.get_ticks()
      deslocamento = 40
      if self.direcao == "right":
        self.x -= deslocamento
      else:
        self.x += deslocamento
      self.rect.x = int(self.x)
      if self.vida <= 0:
        self.vivo = False
        self.estado = "dead"

  def atualizar(self, delta_time):
    tempo_atual = pygame.time.get_ticks()

    # piscar durante invulnerabilidade
    if self.invulneravel:
      if tempo_atual - self.tempo_ultimo_dano < self.tempo_invulneravel:
        self.alpha = 100 if (tempo_atual // 100) % 2 == 0 else 255
      else:
        self.invulneravel = False
        self.alpha = 255

    # controlar o tempo de ataque
    if self.estado == "attacking":
      if tempo_atual - self.tempo_ataque_iniciado > self.duracao_ataque:
        self.estado = "idle"

    # atualizar animação
    imagem_atual = self.sprites.get(self.estado, self.sprites["idle"])
    total_frames = imagem_atual.get_width() // self.frame_size[0]
    self.anim_frame += self.anim_speed
    if self.anim_frame >= total_frames:
      self.anim_frame = 0

  def get_frame(self, frame_index):
    frame_width, frame_height = self.frame_size
    imagem_atual = self.sprites.get(self.estado, self.sprites["idle"])
    rect = pygame.Rect(frame_index * frame_width, 0, frame_width, frame_height)
    return imagem_atual.subsurface(rect)

  def desenhar(self, tela, scale=2):
    frame = self.get_frame(int(self.anim_frame))
    frame_scaled = pygame.transform.scale(frame, (int(self.frame_size[0]*scale), int(self.frame_size[1]*scale)))

    if self.direcao == "left":
      frame_scaled = pygame.transform.flip(frame_scaled, True, False)

    frame_scaled.set_alpha(self.alpha)  # 👈 aplica o piscar
    tela.blit(frame_scaled, self.rect)
