# ⚔️ Tanatos — Mini Jogo em Python (Pygame)

Projeto desenvolvido para a disciplina de **Lógica de Programação e Algoritmos**

<img width="702" height="533" alt="Screenshot 2025-10-26 at 20 38 55" src="https://github.com/user-attachments/assets/288df0ff-3456-4702-bb95-0259fe5e8fee" />

## Sobre o Jogo

**Tanatos** é um mini jogo em 2D feito com **Pygame**, onde o jogador controla o **Reaper**, um guerreiro que enfrenta inimigo fantasma (**Ghost**) em um mapa sombrio.

O jogo possui:
- Sprites animadas (parado, andando, atacando, levando dano)
- Sistema de colisão e dano
- Som de ataque
- Efeitos de invulnerabilidade (piscar após ser atingido)
- Sistema de pontuação e vitória/derrota

## 🎮 Como Jogar

| Ação | Tecla |
|------|-------|
| Mover para a direita | → |
| Mover para a esquerda | ← |
| Atacar | Espaço |
| Sair do jogo | Fechar janela (ou `Ctrl + C` no terminal) |

## Mecânica de Jogo

- **Ataque e Colisão:**  
  Quando o Reaper ataca (`K_SPACE`) e há colisão com o Ghost, o inimigo perde vida.  
  Se o Ghost encosta no Reaper, ele causa dano e o jogador fica **invulnerável por 1,5s**, piscando na tela.

- **Score:**
  - Cada vitória soma ponto para o vencedor.  
  - O placar é exibido na interface.
  - Atualizações de dano apenas no terminal ainda.

## Recursos Utilizados

- **Biblioteca:** [Pygame](https://www.pygame.org/)
- **Linguagem:** Python 3.x
- **Fontes:** Pixeltype.ttf (8-bit style)
- **Sprites:** Adaptadas de bancos de assets gratuitos (itch.io)
- **Som:** Efeito de espada em MP3, Efeito de Hit em wav.

## Possíveis Extensões

- Adicionar múltiplos inimigos com IA simples.
- Implementar sistema de power-ups.
- Adicionar fases e background animado.
- Sistema de HUD com barra de vida.
- Menu inicial com opções de dificuldade.

## Como Executar

1. Instale o Python (versão 3.8 ou superior)
2. Criar o ambiente virtual:
```bash
python -m venv venv
```
3. Ativar o ambiente:
- Windows:
```bash
venv\Scripts\activate
```
- macOS / Linux:
```bash
source venv/bin/activate
```
4. Execute o jogo:
```bash
python3 jogo.py
```
##
- **Nome:** Lis Isabelle Nogueira Marreiros
- **Curso:** Análise e Desenvolvimento de Sistemas  
- **Professor:** Jadson Almeida
- **Instituição:** Uninter  


