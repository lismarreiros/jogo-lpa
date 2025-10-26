import pygame

class Ghost:
  def __init__(self, imagem_idle, frame_size, imagem_hurt, imagem_dead, posicao_inicial, velocidade=60, vida=100):
    # spritesheets
    self.sprites = {
      "idle": imagem_idle,
      "hurt": imagem_hurt,
      "dead": imagem_dead,
    }
    self.frame_size = (int(frame_size[0]), int(frame_size[1]))
    self.estado = "idle"
    self.anim_frame = 0.0
    self.anim_speed = 6.0  # frames por segundo
    # posição e colisão
    self.x, self.y = float(posicao_inicial[0]), float(posicao_inicial[1])
    self.x_inicial = float(posicao_inicial[0])
    self.rect = pygame.Rect(int(self.x), int(self.y), self.frame_size[0], self.frame_size[1])

    # movimento
    self.velocidade = velocidade  # px por segundo
    self.direcao_movimento = 1

    # combate
    self.vida = vida
    self.vivo = True
    self.forca = 10
    self.ultimo_ataque = 0
    self.cooldown_ataque = 1500  # ms

  def pode_atacar(self):
    return (pygame.time.get_ticks() - self.ultimo_ataque) >= self.cooldown_ataque

  def registrar_ataque(self):
    self.ultimo_ataque = pygame.time.get_ticks()

  def levar_dano(self, dano):
    if not self.vivo:
      return
    self.vida -= dano
    if self.vida <= 0:
      self.vivo = False
      self.estado = "dead"
    else:
      # ao levar dano, troca para "hurt" e reinicia animação
      self.estado = "hurt"
      self.anim_frame = 0.0

  def atualizar(self, delta_time):
    """
    delta_time: milissegundos desde o último frame
    """
    # delta em segundos
    dt = delta_time / 1000.0

    # movimento só se vivo
    if self.vivo:
      self.x += self.velocidade * self.direcao_movimento * dt
      # limites (ajuste conforme seu mapa)
      max_x = 700 - self.frame_size[0]  # assume width da tela 700
      if self.x > max_x:
        self.x = max_x
        self.direcao_movimento = -1
      if self.x < self.x_inicial:
        self.x = self.x_inicial
        self.direcao_movimento = 1

    # atualizar rect
    self.rect.topleft = (int(self.x), int(self.y))

    # animação: calcula total de frames da spritesheet do estado atual
    img = self.sprites.get(self.estado, self.sprites["idle"])
    sheet_w = img.get_width()
    frame_w = self.frame_size[0]
    total_frames = max(1, sheet_w // frame_w)

    # avança frame com base em anim_speed (frames por segundo)
    self.anim_frame += self.anim_speed * dt
    # evita overflow: mantém no intervalo [0, total_frames)
    if self.anim_frame >= total_frames:
      # para sprites como "hurt" talvez queira permanecer no último frame por um tempo.
      # aqui repetimos o ciclo normalmente. Se quiser outro comportamento, ajustamos.
      self.anim_frame %= total_frames
      if self.estado == "hurt" and (pygame.time.get_ticks() - self.ultimo_ataque) > 400:
          self.estado = "idle"

  def get_frame(self):
    """Retorna Surface do frame atual do estado."""
    img = self.sprites.get(self.estado, self.sprites["idle"])
    frame_w, frame_h = self.frame_size
    total_frames = max(1, img.get_width() // frame_w)
    idx = int(self.anim_frame) % total_frames
    src_rect = pygame.Rect(idx * frame_w, 0, frame_w, frame_h)
    return img.subsurface(src_rect).copy()

  def desenhar(self, tela, scale=1.5):
    frame = self.get_frame()
    if scale != 1:
        frame = pygame.transform.scale(frame, (int(self.frame_size[0] * scale), int(self.frame_size[1] * scale)))
    # desenhar na posição (x, y) atual
    tela.blit(frame, (int(self.x), int(self.y)))
    # (rect já atualizado em atualizar)
