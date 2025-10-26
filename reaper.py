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

    self.vida = vida
    self.vivo = True
    self.forca = 10

    self.cooldown_ataque = 500
    self.tempo_desde_ataque = 0

  def mover(self, direcao):
    if direcao == "left":
      self.x -= self.velocidade
    
  def atacar(self):
    if self.tempo_desde_ataque >= self.cooldown_ataque:
      print("Reaper atacou!")
      self.estado = "attacking"
      self.tempo_desde_ataque = 0

  def atualizar(self, delta_time):
    self.tempo_desde_ataque += delta_time
    if self.estado == "attacking":
      # Verifica se o tempo do ataque (swing) passou
      if self.tempo_desde_ataque >= self.duracao_ataque:
        self.estado = "idle" # Volta para o estado parado
            
    if self.estado == "idle" or self.estado == "moving":  
      # Pega a imagem atual baseada no estado (usado no get_frame)
      imagem_atual = self.sprites.get(self.estado, self.sprites["idle"])  
      # Calcula o total de frames na spritesheet atual
      total_frames = imagem_atual.get_width() // self.frame_size[0]
      # Avança o frame
      self.anim_frame += self.anim_speed
        
      # Volta ao primeiro frame se tiver completado o ciclo
      if self.anim_frame >= total_frames:
          self.anim_frame = 0

  def get_frame(self, frame_index):
    frame_width, frame_height = self.frame_size
    # escolher o sprite correto baseado no estado
    imagem_atual = self.sprites.get(self.estado, self.sprites["idle"])
    rect = pygame.Rect(frame_index * frame_width, 0, frame_width, frame_height)
    return imagem_atual.subsurface(rect)

  def desenhar(self, tela, scale = 2):
    frame = self.get_frame(int(self.anim_frame))
    scaled_size = int(self.frame_size[0] * scale), int(self.frame_size[1] * scale)
    frame_scaled = pygame.transform.scale(frame, scaled_size)

    frame_final = frame_scaled
    if self.direcao == "left":
      frame_final = pygame.transform.flip(frame_scaled, True, False)
    tela.blit(frame_final, (self.x, self.y))